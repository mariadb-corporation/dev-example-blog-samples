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

for file in os.listdir(path):
    if os.path.isdir(path + '\\' + file):
        paths.append(path + file)
    else:
        sfile = path + '\\' + file
        print(sfile)
        with ExifToolHelper() as et:
            try:
                for d in et.get_tags(sfile, tags=['SourceFile', 'File:Directory', 'File:FileName']):
                    for k, v in d.items():

                        print(f"Dict: {k} = {v}")
            except:
                print('Fehler')


session.close()
