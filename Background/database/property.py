from .db import Base,session
from sqlalchemy import String,Integer,TIMESTAMP,DECIMAL,Column,DateTime
from sqlalchemy import Column,Integer,String,TIMESTAMP,ForeignKey
from sqlalchemy import String,Integer,TIMESTAMP,DECIMAL


class Propertys(Base):
    __tablename__ = 'property'
    id = Column(Integer, primary_key=True)
    status = Column(Integer)
    bar_codes = Column(String)
    name = Column(String)
    type = Column(Integer)
    model=Column(String)
    sn = Column(Integer)
    unit = Column(String)
    price = Column(DECIMAL)
    time = Column(Integer)
    area = Column(Integer)
    deadline = Column(Integer)
    source = Column(Integer)
    remark = Column(String)
    img = Column(String)
    supplier = Column(String)
    linkman = Column(String)
    tel = Column(String)
    expir = Column(DateTime)
    info = Column(String)
    aid = Column(Integer)
    cid = Column(Integer)
    uid = Column(Integer)
    did = Column(Integer)

