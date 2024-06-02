from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from typing import Annotated, List
from fastapi.middleware.cors import CORSMiddleware
import models
from database import SessionLocal, engine
import pandas
import io
import contextlib
import traceback
import scipy

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:5173"
]

# CORS middleware setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Pydantic models
class ExecutionBase(BaseModel):
    code: str
    output: str = ""

class ExecuteModel(ExecutionBase):
    id: int

    class Config:
        orm_mode = True

def get_db():
    # starts sqlite session
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

# Ensure database models are created
models.Base.metadata.create_all(bind=engine)

# API endpoint for code execution
@app.post("/submit/", response_model=ExecuteModel)
async def create_execution(execution: ExecutionBase, db: db_dependency):
    print(execution.code)
    local_vars = {}
    stdout_capture = io.StringIO()
    
    try:
        with contextlib.redirect_stdout(stdout_capture):
            exec(execution.code, {"pandas": pandas, "scipy": scipy}, {})
        execution.output = stdout_capture.getvalue()
    except Exception as e:
        execution.output = ''.join(traceback.format_exception(None, e, e.__traceback__))
        raise HTTPException(status_code=400, detail=execution.output)

    db_execution = models.Execute(**execution.model_dump())
    db.add(db_execution)
    db.commit()
    db.refresh(db_execution)
    return db_execution

@app.post("/test/")
async def create_execution(execution: ExecutionBase):
    print(execution.code)
    local_vars = {}
    stdout_capture = io.StringIO()
    
    try:
        with contextlib.redirect_stdout(stdout_capture):
            exec(execution.code, {"pandas": pandas, "scipy": scipy}, {})
        execution.output = stdout_capture.getvalue()
    except Exception as e:
        execution.output = ''.join(traceback.format_exception(None, e, e.__traceback__))
        raise HTTPException(status_code=400, detail=execution.output)

    return execution

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "ok"}

