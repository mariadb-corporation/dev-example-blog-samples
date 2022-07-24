from exiftool import ExifToolHelper
import os
from datetime import date

from base import Session, engine, Base
from MetaData import FileData
from MetaData import ExifData

# Generate database schema
Base.metadata.create_all(engine)

# Create a new session
session = Session()

path = "c:\\TestImage"

paths = []

session.commit()

# fdata = FileData()

for file in os.listdir(path):
    fdata = FileData()
    if os.path.isdir(path + '\\' + file):
        paths.append(path + file)
    else:
        sfile = path + '\\' + file
        print(sfile)
        with ExifToolHelper() as et:
            try:
                for d in et.get_tags(sfile, tags=['SourceFile', 'File:Directory', 'File:FileName']):
                    for k, v in d.items():
                        if k == 'File:FileName':
                            fdata.filename = v
                        elif k == 'File:Directory':
                            fdata.path = v
                        elif k == 'SourceFile':
                            fdata.fullname = v
            except:
                print('Fehler')

            try:
                for t in et.get_tags(sfile, tags=['EXIF:*', 'XMP:*']):
                    for k, v in t.items():
                        test: list = k.split(':')
                        if len(test) == 2:
                            tdata = ExifData(key=test[1], keydata=str(v), file=fdata, typ=test[0])
                            session.add(tdata)
                            session.commit()
            except:
                print('Fehler')

    session.add(fdata)
    session.commit()

session.close()
