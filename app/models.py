from database import Base
from sqlalchemy import Column,Integer,TIMESTAMP,String,Float,Text
from sqlalchemy import CheckConstraint ,ForeignKey, DECIMAL, Boolean
from sqlalchemy import func


"""
******** C (uppercase C) ----> Current ***********
eg C_vechicle_number ----> Current Vechicle Number

********* P (Uppercase P) -----> Previous *******

********* d ----------> Driver ********


********* u ..............> user **********


"""
class DriverData(Base):
    __tablename__ = 'driver_data'

    id = Column(Integer, primary_key=True, index=True)
    d_name = Column(String(100), nullable=False)
    C_vechicle_number = Column(String(50), nullable=False, unique=True, index=True)
    C_vechicle_type = Column(String(50), nullable=False)
    P_vechicle_number = Column(String(50), index=True)
    P_vechicle_type = Column(String(50), nullable=False)
    license_number = Column(String(50), nullable=False, unique=True, index=True)
    D_phone_number = Column(String(20), nullable=False, unique=True, index=True)
    D_email = Column(String(100), nullable=False, unique=True, index=True)
    last_ride = Column(TIMESTAMP)
    status = Column(Boolean, nullable=False, server_default="1")
    d_created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    d_updated_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    rating = Column(DECIMAL(2, 1), CheckConstraint('rating >= 0 AND rating <= 5'), nullable=True)

class User_data(Base):
    __tablename__ = 'user_data'
    id = Column(Integer , primary_key=True, index=True)
    u_name = Column(String(101))
    u_email = Column(String(102) , unique=True , index=True , nullable=False)
    u_phone = Column(Integer, unique=True, nullable=False , index=True)
    u_created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    u_updated_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    last_ride = Column(TIMESTAMP, server_default=func.now())
    last_ride_vechicle_number = Column(String(50), index=True)

class RideData(Base):
    __tablename__ = 'ride_data'
    id = Column(Integer, primary_key=True, index=True)
    driver_id = Column(Integer, ForeignKey('driver_data.id'), nullable=False)
    passenger_id = Column(Integer, ForeignKey('user_data.id'), nullable=False)
    start_location = Column(String(255), nullable=False)
    end_location = Column(String(255), nullable=False)
    fare = Column(DECIMAL(10, 2), nullable=False)
    ride_status = Column(String(20), nullable=False, server_default='ongoing')
    start_time = Column(TIMESTAMP, server_default=func.now())
    end_time = Column(TIMESTAMP)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    
class FeedbackData(Base):
    __tablename__ = 'feedback_data'
    id = Column(Integer, primary_key=True, index=True)
    ride_id = Column(Integer, ForeignKey('ride_data.id'), nullable=False)
    passenger_id = Column(Integer, ForeignKey('user_data.id'), nullable=False)
    driver_id = Column(Integer, ForeignKey('driver_data.id'), nullable=False)
    rating = Column(DECIMAL(2, 1), CheckConstraint('rating >= 0 AND rating <= 5'), nullable=True)
    comments = Column(Text)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)

class PaymentData(Base):
    __tablename__ = 'payment_data'
    id = Column(Integer, primary_key=True, index=True)
    ride_id = Column(Integer, ForeignKey('ride_data.id'), nullable=False)
    amount = Column(DECIMAL(10, 2), nullable=False)
    payment_method = Column(String(50), nullable=False)
    payment_status = Column(String(20), nullable=False, server_default='pending')
    payment_time = Column(TIMESTAMP, server_default=func.now())
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)

class EmergencyContactData(Base):
    __tablename__ = 'emergency_contact_data'
    id = Column(Integer, primary_key=True, index=True)
    passenger_id = Column(Integer, ForeignKey('user_data.id'), nullable=False)
    contact_name = Column(String(100), nullable=False)
    contact_phone_number = Column(String(15), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)

class DriverAvailability(Base):
    __tablename__ = 'driver_availability'
    id = Column(Integer, primary_key=True, index=True)
    driver_id = Column(Integer, ForeignKey('driver_data.id'), nullable=False)
    available = Column(Boolean, nullable=False, server_default="1")
    last_updated = Column(TIMESTAMP, server_default=func.now())server_default='CURRENT_TIMESTAMP'
""""Well just want to make this as 100"""
