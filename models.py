import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy import Table
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class testTable(Base):
    __tablename__ = 'test'
    id = Column(Integer(), primary_key=True)
    field = Column(String())