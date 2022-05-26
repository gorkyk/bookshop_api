#This is the manual for using bookshop_api

##There are several steps to use and test it

###1.You should create the database entering at the project directory:
python .\backend\create_engine.py  
###2.You should create the test database if you need entering at the project directory:
python .\backend\test_db_creation.py

###3.Run the app from **backend** directory
cd backend

uvicorn main:app --reload