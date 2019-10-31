# 贾争
from .db import Base,session
from sqlalchemy import String,Integer,TIMESTAMP,DECIMAL,Column,ForeignKey

class Change(Base):
    __tablename__ = "change"
    id = Column(Integer,primary_key=True)
    oid = Column(Integer)
    ctime = Column(TIMESTAMP)
    aid = Column(Integer,ForeignKey("admin.id"))
    bar_codes = Column(String)
    name = Column(String)
    type = Column(Integer)
    model = Column(String)
    sn = Column(Integer)
    unit = Column(String)
    price = Column(DECIMAL)
    area = Column(Integer)
    deadline = Column(Integer)
    supplier = Column(String)
    linkman = Column(String)
    tel = Column(String)
    expir = Column(TIMESTAMP)
    info = Column(String)
    cid = Column(Integer,ForeignKey("company.id"))
    did = Column(Integer,ForeignKey("Department"))