from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey
from sqlalchemy.orm import relationship

from base import Base


class Asset(Base):
    __tablename__ = 'assets'

    id = Column(Integer, primary_key=True)
    model_id = Column(Integer, ForeignKey('models.id'))
    model = relationship("Model")



class Model(Base):
    __tablename__ = 'models'

    id = Column(Integer, primary_key=True)
    bezeichnung = Column(String(length=100))
    typ_id = Column(Integer, ForeignKey('assettypes.id'))
    typ = relationship("AssetTyp", back_populates='models')


class AssetTyp(Base):
    __tablename__ = 'assettypes'

    id = Column(Integer, primary_key=True)
    name = Column(String(length=100))
    models = relationship("Model")


class Computer(Base):
    __tablename__ = 'computer'

    id = Column(Integer, primary_key=True)
    id_asset = Column(Integer, ForeignKey('assets.id'))
    pcname = Column(String(length=50))
    assets = relationship("Asset")
