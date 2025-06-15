from database import Base , engine , SessionLocal
from fastapi import FastAPI , Depends, HTTPException
import models
from sqlalchemy.orm import Session
from contextlib import asynccontextmanager
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from decimal import Decimal

async def lifespan(app : FastAPI):
   Base.metadata.create_all(bind=engine)
   
   yield
app = FastAPI(lifespan=lifespan)


#-------------------------------------------------
# pydantic base model for DriverData
class DriverDataSchema(BaseModel):
    id : Optional[int]
    d_name : str
    C_vehicle_number : str
    C_vehicle_type : str
    P_vehicle_number : str
    P_vehicle_type : str
    license_number : str
    D_phone_number : str
    D_email : str
    last_ride : datetime
    status : bool
    d_created_at : datetime
    d_updated_at : datetime
    rating : Decimal

    class Config:
       from_attributes = True
#-------------------------------------------------

# db session intialize
def get_db():
    db = SessionLocal()
    try : 
      yield db
    finally:
        db.close()

"""  uvicorn app.main:app --reload use this to load this  
now when you go to http://127.0.0.1:8000/(the app.get() values you can access the api) 

example: http://127.0.0.1:8000/test_case/1


also when you push this to main branch do like this:

 1243  git add .
 1244  git commit -m 'FASTAPI_INTIALIZATION'
 1245  git pull origin main
 1246  git push -u origin main

 first add -> commit -> pull -> push


 that commit will save your work locally 

 and pull will keep you upto date 

 and push will push it to the main branch
"""
@app.get("/")
def rooted():
   return {'Message':'Hello'}

@app.post('/api/vehicle_number')
def add_vehicle_number(request : DriverDataSchema ,db : Session = Depends(get_db)):
   exist_already = db.query(models.DriverData).filter_by(C_vehicle_number =request.C_vehicle_number).first()
   if exist_already:
      raise HTTPException(status_code=400 , detail='Vehicle already exist in Database.')
   driver_v_number = models.DriverData(C_vehicle_number=request.C_vehicle_number)
   db.add(driver_v_number)
   db.commit()
   db.refresh(driver_v_number)
   return{'id':driver_v_number.id,'Vehicle_number:':driver_v_number.C_vechicle_number}
