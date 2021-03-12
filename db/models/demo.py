from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from db.base_class import Base


class Item(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)