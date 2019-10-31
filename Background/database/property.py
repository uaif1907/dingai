from .db import Base,session


class User(Base):
    pass


from sqlalchemy import String,Integer,TIMESTAMP,DECIMAL,Column,DateTime
from sqlalchemy import Column,Integer,String,TIMESTAMP,ForeignKey
from sqlalchemy import String,Integer,TIMESTAMP,DECIMAL
from sqlalchemy.orm import relationship
from .Admin import Admins

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
    aid = Column(Integer,ForeignKey("admin.id"))
    cid = Column(Integer)
    uid = Column(Integer)
    did = Column(Integer)
    admin = relationship("Admins",foreign_keys=aid)
    # foreign_keys 创建多个反向映射时使用



