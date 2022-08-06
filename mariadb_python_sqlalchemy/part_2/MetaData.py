from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey
from sqlalchemy.orm import relationship

from base import Base
class FileData(Base):
    __tablename__ = 'filedata'

    id = Column(Integer, primary_key=True)
    filename = Column(String(length=60))
    path = Column(String(length=254))
    fullname = Column(String(length=254))

    def __int__(self, filename, path, fullname):
        self.filename = filename
        self.path = path
        self.fullname = fullname


class ExifData(Base):
    __tablename__ = 'exifdata'

    id = Column(Integer, primary_key=True)
    file_id = Column(Integer, ForeignKey('filedata.id'))
    file = relationship("FileData")
    tag_id = Column(Integer, ForeignKey('exiftags.id'))
    tag = relationship("ExifTags")
    keydata = Column(String(length=2000))


class ExifTags(Base):
    __tablename__ = 'exiftags'

    id = Column(Integer, primary_key=True)
    tagtyp = Column(String(length=10))
    key = Column(String(length=40))
