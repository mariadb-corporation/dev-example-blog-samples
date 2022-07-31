from exiftool import ExifToolHelper
import os
from datetime import date

from base import Session, engine, Base
from sqlalchemy import select
from MetaData import FileData
from MetaData import ExifData
from MetaData import ExifTags

# Generate database schema
Base.metadata.create_all(engine)

# Create a new session
session = Session()

path = "c:\\TestImage"

session.commit()


def addMetaData(filename):
    with ExifToolHelper(encoding='utf-8') as et:
        for t in et.get_tags(filename, ['EXIF:*', 'XMP:*', 'IPTC:*']):
            counters = len(t.items())
            for k, v in t.items():
                test: list = k.split(':')
                if len(test) == 2:
                    tdata = ExifData(tag_id=gettagid(test[1]), keydata=str(v), file=fdata, typ=test[0])
                    session.add(tdata)
                    session.commit()
        print("Metadaten: " + str(counters) + " Gespeichert")


def addMetaTags(filename):
    with ExifToolHelper(encoding='utf-8') as et:
        for t in et.get_tags(filename, ['EXIF:*', 'XMP:*', 'IPTC:*']):
            counters = len(t.items())
            for k, v in t.items():
                test: list = k.split(':')
                if len(test) == 2:
                    if tagexist(test[1]):
                        continue
                    else:
                        tdata = ExifTags(key=test[1], tagtyp=test[0])
                        session.add(tdata)
                        session.commit()
                        print("MetaTags: " + str(counters) + " Gespeichert")


def tagexist(strtag):
    stm = select(ExifTags).where(ExifTags.key == strtag)
    result = session.execute(stm)
    if result.raw.rowcount == 1:
        return True
    else:
        return False


def gettagid(strtag):
    stmt = select(ExifTags).where(ExifTags.key == strtag)
    result = session.execute(stmt)
    return result

print('Anzahl Dateien:' + str(len(os.listdir(path))))
counter = len(os.listdir(path))

for file in os.listdir(path):
    fdata = FileData(filename=file, path=path, fullname=path + '\\' + file)
    session.add(fdata)
    session.commit()
    addMetaTags(path + '\\' + file)
    addMetaData(path + '\\' + file)
    counter -= 1
    print('Noch abzuarbeiten: ' + str(counter) + ' Dateien')

session.close()
