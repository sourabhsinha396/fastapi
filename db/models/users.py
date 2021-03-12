from sqlalchemy import Column,Integer,String,Boolean, DateTime
from datetime import datetime

from db.base_class import Base


class Users(Base):
    id = Column(Integer,primary_key = True)
    username = Column(String,unique = True,nullable = False,index=True) #by default nullable is not false so specify everywhere
    email = Column(String,unique=True,nullable=False,index=True)
    email_verified = Column(Boolean,default=False)
    salt = Column(String) # TODO:sepeartion of concerns, It does not belong to users
    password = Column(String)
    is_active = Column(Boolean,default = False)
    is_superuser= Column(Boolean,default=False)
    created_at = Column("created", DateTime, default=datetime.now())
    updated_at = Column("updated", DateTime, default=datetime.now(), onupdate=datetime.now())