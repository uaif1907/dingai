from .db import Base,session
from sqlalchemy import String,Integer,TIMESTAMP,DECIMAL,Column
from sqlalchemy import Column,Integer,String,TIMESTAMP,ForeignKey
from sqlalchemy import String,Integer,TIMESTAMP,DECIMAL

class Companys(Base):
    __tablename__ = 'company'
    id = Column(Integer, primary_key=True)
    name = Column(String)