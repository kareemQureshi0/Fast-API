# endpoints 
# /create
# /view/ patient_id
# /update /patient_id
# /delete /patient_id

from fastapi import FastAPI
import json

def load_data():
    with open('patients.json','r') as f:
        data = json.load(f)
        return data
    
app = FastAPI()

@app.get("/view")
def view():
    data = load_data()
    return data


