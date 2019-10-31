from .db import Base,session
from sqlalchemy import String,Integer,TIMESTAMP,DECIMAL,Column
from sqlalchemy import Column,Integer,String,TIMESTAMP,ForeignKey
from sqlalchemy import String,Integer,TIMESTAMP,DECIMAL
class Users(Base):
    __tablename__='user'

    uid = Column(Integer,primary_key=True)
    num = Column(String)
    name = Column(String)
    cid = Column(Integer)
    did = Column(Integer)
    email = Column(String)
    tel = Column(Integer)