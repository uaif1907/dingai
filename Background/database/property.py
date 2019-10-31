from .db import Base,session
from sqlalchemy import String,Integer,TIMESTAMP,DECIMAL,Column,DateTime
from sqlalchemy import Column,Integer,String,TIMESTAMP,ForeignKey
from sqlalchemy import String,Integer,TIMESTAMP,DECIMAL
from .Admin import Admins
from .User import Users
from .Company import Companys
from .Department import Departments
from sqlalchemy.orm import relationship

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
    cid = Column(Integer,ForeignKey("company.id"))
    uid = Column(Integer,ForeignKey("user.uid"))
    did = Column(Integer,ForeignKey("department.id"))
    admin = relationship("Admins",foreign_keys=aid)
    user = relationship("Users",foreign_keys=uid)
    company = relationship('Companys',foreign_keys=cid)
    department = relationship("Departments",foreign_keys=did)
    # foreign_keys 创建多个反向映射时使用



