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

session.commit()

def addMetaData(filename):
    with ExifToolHelper(encoding='utf-8') as et:
        for t in et.get_tags(filename, ['EXIF:*', 'XMP:*']):
            counters = len(t.items())
            for k, v in t.items():
                test: list = k.split(':')
                if len(test) == 2:
                    tdata = ExifData(key=test[1], keydata=str(v), file=fdata, typ=test[0])
                    session.add(tdata)
                    session.commit()
        print("Metadaten: " + str(counters) + " Gespeichert")



print('Anzahl Dateien:' + str(len(os.listdir(path))))
counter = len(os.listdir(path))

for file in os.listdir(path):
    fdata = FileData(filename=file, path=path, fullname=path + '\\' + file)
    session.add(fdata)
    session.commit()
    addMetaData(path + '\\' + file)
    counter -= 1
    print('Noch abzuarbeiten: ' + str(counter) + ' Dateien' )

session.close()
