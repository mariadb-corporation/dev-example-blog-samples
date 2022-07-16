from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey
from sqlalchemy.orm import relationship

from base import Base


class Model(Base):
    __tablename__ = 'models'

    id_model = Column(Integer, primary_key=True)
    bezeichnung = Column(String(length=50))
    typ_id = Column(Integer)
