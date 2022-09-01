from typing import Union
from COURSE.MODULE5.exo import get_database
from fastapi import FastAPI

app = FastAPI()

# MongoDB
# Get the database
dbname = get_database()
# # get collection 
collection_name = dbname["contacts_items"]

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/db")
def get_db_info():
    return {"db": f"{dbname}"}

@app.get("/count-contacts")
def count_contacts():
    return {"n_contacts": collection_name.count_documents({}) }


valid_keys = ['name', 'phone', 'email', 'address', 'latlng', 'salary', 'age', 'latlon', 'currency', 'conv_to_xof', 'country', 'flag']

@app.get("/all-contacts")
def get_all_contacts():

    list_contacts = list(collection_name.find())
    return {"contacts": [ {k:list_contacts[i][k] for k in valid_keys} for i in range(len(list_contacts))] }

