from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey
from sqlalchemy.orm import relationship

from base import Base
class FileData(Base):
    __tablename__ = 'filedata'

    id = Column(Integer, primary_key=True)
    filename = Column(String(length=60))
    path = Column(String(length=254))


class ExifData(Base):
    __tablename__ = 'exifdata'

    id = Column(Integer, primary_key=True)
    file_id = Column(Integer, ForeignKey('filedata.id'))
    file = relationship("FileData")
    key = Column(String(length=60))
    keydata = Column(String(length=500))


