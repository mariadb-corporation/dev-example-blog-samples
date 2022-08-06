from exiftool import ExifToolHelper
import os
from datetime import date

from base import Session, engine, Base
from MetaData import FileData
from MetaData import ExifData
import xml.etree.ElementTree as xstring


# Create a new session
session = Session()

file1 = session.query(ExifData).filter(ExifData.key == 'Categories')


for d in file1:
    root = xstring.fromstring(d.keydata)
    test = root[0].text
    test1 = root[0][0].text
    test2 = d.file_id
    fullfile = session.query(FileData).filter(FileData.id == d.file_id)
    for f in fullfile:
        f.fullname

    print(test, test1, f.fullname)



