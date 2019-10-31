from .db import Base,session
from sqlalchemy import String,Integer,TIMESTAMP,DECIMAL,Column
from sqlalchemy import Column,Integer,String,TIMESTAMP,ForeignKey
from sqlalchemy import String,Integer,TIMESTAMP,DECIMAL
from .property import Propertys

from sqlalchemy.orm import relationship


class Main(Base):
    __tablename__='maintain'
    id = Column(Integer,primary_key=True)
    time1 = Column(TIMESTAMP)
    uid = Column(Integer,ForeignKey('user.uid'))
    explain=Column(String)
    pid=Column(Integer)
    explain2 = Column(String)
    price = Column(DECIMAL)
    people = Column(String)
    time2 = Column(TIMESTAMP)

