from .db import Base,session
from sqlalchemy import String,Integer,TIMESTAMP,DECIMAL,Column
from sqlalchemy import Column,Integer,String,TIMESTAMP,ForeignKey
from sqlalchemy import String,Integer,TIMESTAMP,DECIMAL

class Admins(Base):
    __tablename__='admin'
    id = Column(Integer,primary_key=True)
    username=Column(String)
    password=Column(String)
    type=Column(Integer)
