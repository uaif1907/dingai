# 贾争
from .db import Base,session
from sqlalchemy import String,Integer,TIMESTAMP,DECIMAL,Column,ForeignKey
from sqlalchemy.orm import relationship

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
    did = Column(Integer,ForeignKey("department.id"))
    pid = Column(Integer,ForeignKey("property.id"))
    img = Column(String)
    remark = Column(String)
    admin = relationship("Admins", foreign_keys=aid)
    company = relationship('Companys', foreign_keys=cid)
    department = relationship("Departments", foreign_keys=did)
    property = relationship("Propertys",foreign_keys=pid)