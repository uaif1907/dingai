from .db import Base,session
from sqlalchemy import String,Integer,TIMESTAMP,DECIMAL,Column

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