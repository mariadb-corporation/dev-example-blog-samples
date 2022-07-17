from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey
from sqlalchemy.orm import relationship

from base import Base


class AssetTyp(Base):
    __tablename__ = 'asset_types'

    id = Column(Integer, primary_key=True)
    name = Column(String(length=50))

