from sqlalchemy import Enum
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from datetime import datetime

from db.base_class import Base


class Cleanings(Base):
    id = Column(Integer,primary_key = True)
    name = Column(String)
    description = Column(String,nullable=True)
    cleaning_type = Column(String)
    price = Column(Integer)
    created_at = Column("created", DateTime, default=datetime.now())
    updated_at = Column("updated", DateTime, default=datetime.now(), onupdate=datetime.now())