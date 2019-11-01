from .db import Base

from sqlalchemy import Column,ForeignKey
from sqlalchemy import String,Integer,TIMESTAMP,DECIMAL





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


