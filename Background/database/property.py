from .db import Base,session
from sqlalchemy import Column,Integer,String,TIMESTAMP,ForeignKey
from sqlalchemy import String,Integer,TIMESTAMP,DECIMAL

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