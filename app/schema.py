from pydantic import BaseModel, EmailStr
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
        