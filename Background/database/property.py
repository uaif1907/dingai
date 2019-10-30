from .db import Base,session
from sqlalchemy import String,Integer,TIMESTAMP,DECIMAL,Column
from sqlalchemy import Column,Integer,String,TIMESTAMP,ForeignKey
from sqlalchemy import String,Integer,TIMESTAMP,DECIMAL

class User(Base):
    pass

# 退库
class Cancellings(Base):
    __tablename__ = "cancelling"
    id = Column(Integer,primary_key=True)
    aid = Column(Integer)
    time = Column(TIMESTAMP)
    area = Column(Integer)
    explain = Column(String)
    rid = Column(Integer)


class Admins(Base):

   pass

class Companys(Base):
    pass

class Departments(Base):
    pass

class Users(Base):
    # _tablename__='user'
    # id = Column(Integer)
    # username = Column(String)
    # password = Column(String)
    pass
class Propertys(Base):
    pass
