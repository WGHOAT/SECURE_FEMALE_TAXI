from database import Base , engine , SessionLocal
from fastapi import FastAPI , Depends, HTTPException
import schema
from sqlalchemy.orm import Session
from contextlib import asynccontextmanager
import models


async def lifespan(app : FastAPI):
   Base.metadata.create_all(bind=engine)
   
   yield
app = FastAPI(lifespan=lifespan)


#-------------------------------------------------
# pydantic base model for DriverData
'''
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
'''
# db session intialize
def get_db():
    db = SessionLocal()
    try : 
      yield db
    finally:
        db.close()

'''use fastapi dev to run bro 

but install fastapi[standard] first

'''

@app.get("/")
def rooted():
   return {'Message':'Hello'}

@app.post('/api/driveradd')
def driveradd(request : schema.DriverDataSchema , db : Session  = Depends(get_db) ):
   exist_already = db.query(models.DriverData).filter_by(C_vehicle_number = request.C_vehicle_number).first()
   if exist_already :
      raise HTTPException(status_code=400,detail='Driver already exist in Database')
   driver = models.DriverData(**request.model_dump())
   db.add(driver)
   db.commit()
   db.refresh(driver)
   return {
      'message':'Driver and vehicle Added Successfully',
      'id' : driver.id,
      'Current Vehichle' : driver.C_vehicle_number
   }
