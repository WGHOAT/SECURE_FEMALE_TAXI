from database import Base , engine , SessionLocal
from fastapi import FastAPI , Depends, HTTPException
import schema
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
import models


async def lifespan(app : FastAPI):
   async with engine.begin() as conn:
      await conn.run_sync(Base.metadata.create_all)   
   yield
app = FastAPI(lifespan=lifespan)



# db session intialize
async def get_db():
    db = SessionLocal()
    try : 
      yield db
    finally:
      await db.close()

'''use fastapi dev to run bro 

but install fastapi[standard] first

'''

@app.get("/")
def rooted():
   return {'Message':'Hello'}

#Driver ENDPOINTS

@app.post('/api/driverdetails')
async def driveradd(request : schema.DriverDataSchema , db : AsyncSession  = Depends(get_db) ):
   result = await db.execute(select(models.DriverData).where(models.DriverData.C_vehicle_number == request.C_vehicle_number))
   exist_already = result.scalars().first()
   if exist_already :
      raise HTTPException(status_code=400,detail='Driver already exist in Database')
   driver = models.DriverData(**request.model_dump())
   db.add(driver)
   await db.commit()
   await db.refresh(driver)
   return {
      'message':'Driver and vehicle Added Successfully',
      'Driver' : driver.d_name,
      'id' : driver.id,
      'Current Vehichle' : driver.C_vehicle_number
   }



# User ENDPOINTS
@app.post('/api/userinfo')
async def useradd(request : schema.User_dataSchema,db : AsyncSession = Depends(get_db)):
   result = await db.execute(select(models.User_data).where(models.User_data.u_phone == request.u_phone))
   exist_already = result.scalars().first()
   if exist_already:
      raise HTTPException(status_code=400 , detail='User already Exist')
   user = models.User_data(**request.model_dump())
   db.add(user)
   await db.commit()
   await db.refresh(user)
   return {
      'message':'User added Succesfully',
      'user' : user.u_name,
      'phone':user.u_phone
   }

#Driver Availability Endpoint
@app.post('/api/driveravailability')
async def driver_availability_add(request : schema.DriverAvialabilitySchema, db : AsyncSession = Depends(get_db)):
   result = await db.execute(select(models.DriverAvailability).where(models.DriverAvailability.driver_id == request.driver_id))
   availability = result.scalars().first()
   if availability:
      raise HTTPException(status_code=400, detail='Availability already exists for this driver')
   availability = models.DriverAvailability(**request.model_dump())
   db.add(availability)
   await db.commit()
   await db.refresh(availability)
   return {
      'message': 'Driver availability added successfully',
      'availability_id': availability.id
   }


#Ride Data ENDPOINT
@app.post('/api/ridedata')
async def ride_add(request : schema.RidedataSchema, db : AsyncSession = Depends(get_db)):
   ride = models.RideData(**request.model_dump())
   db.add(ride)
   await db.commit()
   await db.refresh(ride)
   return {
      'message': 'Ride data added successfully',
      'ride_id': ride.id
   }


#Payment Data ENDPOINT
@app.post('/api/payment')
async def payment_add(request : schema.PaymentDataSchema, db : AsyncSession = Depends(get_db)):
   result = await db.execute(select(models.PaymentData).where(models.PaymentData.ride_id == request.ride_id))
   payment = result.scalars().first()
   if payment:
      raise HTTPException(status_code=400, detail='Payment already exists for this ride')
   payment = models.PaymentData(**request.model_dump())
   db.add(payment)
   await db.commit()
   await db.refresh(payment)
   return {
      'message': 'Payment added successfully',
      'payment_id': payment.id
   }

#Feedback Data Endpoint
@app.post('/api/feedback')
async def feedback_add(request : schema.FeedbackDataSchema, db : AsyncSession = Depends(get_db)):
   feedback = models.FeedbackData(**request.model_dump())
   db.add(feedback)
   await db.commit()
   await db.refresh(feedback)
   return {
      'message': 'Feedback added successfully',
      'feedback_id': feedback.id
   }
