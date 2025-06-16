from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime




class DriverDataSchema(BaseModel):
    id: int
    d_name: str
    C_vehicle_number: str
    C_vehicle_type: str
    P_vehicle_number: str
    P_vehicle_type: str
    license_number: str
    D_phone_number: str
    D_email: EmailStr
    last_ride: datetime
    status: bool
    d_created_at: datetime
    d_updated_at: datetime
    rating: float
    class Config():
        from_attributes = True
        
class User_dataSchema(BaseModel):
    id : int
    u_name : str
    u_email : str
    u_phone : str
    u_created_at : datetime
    u_updated_at : datetime
    last_ride : datetime
    last_ride_vechicle_number : str
    class Config():
        from_attributes = True

class RidedataSchema(BaseModel):
    id : str
    driver_id : int 
    passenger_id : int
    start_location : str
    end_location : str
    created_at : datetime
    updated_at : datetime
    class Config():
        from_attributes = True

class FeedbackDataSchema(BaseModel):
    id : int
    ride_id : int
    passenger_id : int
    driver_id : int
    rating : float
    comments : str
    created_at : datetime
    updated_at : datetime
    class Config():
        from_attributes = True

class PaymentDataSchema(BaseModel):
    id : int
    ride_id : int
    amount : float
    payment_method : str
    payment_status : str
    created_at : datetime
    updated_at : datetime
    class Config():
        from_attributes = True
class EmergencyContactDataSchema():
    id : int
    passenger_id : int
    contact_name : str
    contact_phone_number : str
    created_at : datetime
    updated_at : datetime
    class Config():
        from_attributes = True

class DriverAvialabilitySchema(BaseModel):
    id : int
    driver_id : int
    available : bool
    last_updated : datetime
    class Config():
        from_attributes = True


