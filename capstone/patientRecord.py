# endpoints 
# /create
# /view/ patient_id
# /update /patient_id
# /delete /patient_id

from fastapi import FastAPI, Path, HTTPException, Query
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

@app.get("/patient/{patient_id}")
def view_patient(patient_id:str = Path(..., description = "ID of the patient in DB",example="P001")):
    data = load_data()
    
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404,detail='Patient Not found')

@app.get("/sort")
def sort_patient(sort_by:str=Query(...,description="Sort on the basis of height,weight,bmi"),order:str=Query('asc',description='Sort in ascending or descending order')):
    
    valid_fields = ['height','weight','bmi']
    
    if sort_by not in valid_fields:
        raise HTTPException(status_code = 400,description = f"Invlaid field Select from {valid_fields} ")

    if order not in ['asc','desc']:
        raise HTTPException(status_code=400,detail = "Invalid order select between ascending and descending")    
 
    data = load_data()
    
    sort_order = True if order == 'desc' else False
    
    sorted_data = sorted(data.values(),key = lambda x:x.get(sort_by,0),reverse = sort_order)   