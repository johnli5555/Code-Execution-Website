from database import Base
from sqlalchemy import Column, Integer, String

# creates table inhereited from declarative_base
class Execute(Base):
    __tablename__ = 'Execution_History'

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String)
    output = Column(String)