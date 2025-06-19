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

#Driver ENDPOINTS

@app.post('/api/driverdetails')
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
      'Driver' : driver.d_name,
      'id' : driver.id,
      'Current Vehichle' : driver.C_vehicle_number
   }



# User ENDPOINTS
@app.post('/api/userinfo')
def useradd(request : schema.User_dataSchema,db : Session = Depends(get_db)):
   exist_already = db.query(models.User_data).filter_by(u_phone = request.u_phone).first()
   if exist_already:
      raise HTTPException(status_code=400 , detail='User already Exist')
   user = models.User_data(**request.model_dump())
   db.add(user)
   db.commit()
   db.refresh(user)
   return {
      'message':'User added Succesfully',
      'user' : user.u_name,
      'phone':user.u_phone
   }

