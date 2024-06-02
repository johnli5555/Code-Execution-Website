This is an a Code Execution Website built by Jun Yao(John) Li. The frontend is built using React Vite and Tailwind CSS, 
the backend is built using Python FastAPI and the database used is SQLlite.

This website allows the user to execute python code and view its results using the test function. 
It also allows users to store the results of the execution to a database via the submit button.

To run this application, you must first start a web server for the backend:

uvicorn main:app --reload

Then you can start the react application:

npm run dev

This should get the app up and running
When submitted, the code submitted and the result will be stored to /Backend/codesubmission.db

Note: Python dependencies are stored in requirements.txt. To install them, run

pip install -r requirements.txt
