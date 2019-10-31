from .db import Base,session
from sqlalchemy import String,Integer,TIMESTAMP,DECIMAL,Column
from sqlalchemy import Column,Integer,String,TIMESTAMP,ForeignKey
from sqlalchemy import String,Integer,TIMESTAMP,DECIMAL


class Departments(Base):
    __tablename__ = 'department'
    id = Column(Integer, primary_key=True)
    cid = Column(Integer)
    name = Column(String)
