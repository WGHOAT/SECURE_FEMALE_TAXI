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

#Driver Availability Endpoint
@app.post('/api/driveravailability')
def driver_availability_add(request : schema.DriverAvialabilitySchema, db : Session = Depends(get_db)):
   availability = db.query(models.DriverAvailability).filter_by(driver_id=request.driver_id).first()
   if availability:
      raise HTTPException(status_code=400, detail='Availability already exists for this driver')
   availability = models.DriverAvailability(**request.model_dump())
   db.add(availability)
   db.commit()
   db.refresh(availability)
   return {
      'message': 'Driver availability added successfully',
      'availability_id': availability.id
   }


#Ride Data ENDPOINT
@app.post('/api/ridedata')
def ride_add(request : schema.RidedataSchema, db : Session = Depends(get_db)):
   ride = models.RideData(**request.model_dump())
   db.add(ride)
   db.commit()
   db.refresh(ride)
   return {
      'message': 'Ride data added successfully',
      'ride_id': ride.id
   }


#Payment Data ENDPOINT
@app.post('/api/payment')
def payment_add(request : schema.PaymentDataSchema, db : Session = Depends(get_db)):
   payment = db.query(models.PaymentData).filter_by(ride_id=request.ride_id).first()
   if payment:
      raise HTTPException(status_code=400, detail='Payment already exists for this ride')
   payment = models.PaymentData(**request.model_dump())
   db.add(payment)
   db.commit()
   db.refresh(payment)
   return {
      'message': 'Payment added successfully',
      'payment_id': payment.id
   }

#Feedback Data Endpoint
@app.post('/api/feedback')
def feedback_add(request : schema.FeedbackDataSchema, db : Session = Depends(get_db)):
   feedback = models.FeedbackData(**request.model_dump())
   db.add(feedback)
   db.commit()
   db.refresh(feedback)
   return {
      'message': 'Feedback added successfully',
      'feedback_id': feedback.id
   }
