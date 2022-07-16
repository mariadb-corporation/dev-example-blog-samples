from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from base import Base


class Asset(Base):
    __tablename__ = 'Assets'

    id_asset = Column(Integer, primary_key=True)
    model_id = Column(Integer)
    name = Column(String(length=100))

    def __int__(self, name):
        self.name = name
