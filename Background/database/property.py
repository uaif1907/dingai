from .db import Base,session
from sqlalchemy import Column,Integer,String,TIMESTAMP,ForeignKey
from sqlalchemy import String,Integer,TIMESTAMP,DECIMAL

class Admins(Base):
    __tablename__='admin'
    id = Column(Integer,primary_key=True)
    username=Column(String)
    password=Column(String)
    type=Column(Integer)


class Companys(Base):
    __tablename__ = 'company'
    id = Column(Integer, primary_key=True)

class Departments(Base):
    __tablename__ = 'department'
    id = Column(Integer, primary_key=True)
    cid = Column(Integer)

class Users(Base):
    _tablename__='user'
    uid = Column(Integer,primary_key=True)
    num = Column(String)
    name = Column(String)
    cid = Column(Integer)
    did = Column(Integer)
    email = Column(String)
    tel = Column(Integer)

class Propertys(Base):
    _tablename__ = 'property'
    id = Column(Integer, primary_key=True)
    status = Column(Integer)
    bar_codes = Column(String)
    name = Column(String)


    num = Column(String)

    cid = Column(Integer)
    did = Column(Integer)
    email = Column(String)
    tel = Column(Integer)