#!/usr/bin/python3
"""class definition of a State and an instance 
   Base = declarative_base()"""

import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class State(Base):
    """Class State"""

    __tablename__ = "states"
 
    id = Column(Integer, primary_key=True, autoincrement=True,
                 nullable=False, unique=True)
    name = Column(String(128), nullable=False)

