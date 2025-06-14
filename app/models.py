from database import Base
from sqlalchemy import Column,Integer,TIMESTAMP,String,Float
class User_data(Base):
    __tablename__ = 'user_data'

    id = Column(Integer , primary_key=True, index=True)
    name = Column(String(101))
    email = Column(String(102) , unique=True , index=True)



