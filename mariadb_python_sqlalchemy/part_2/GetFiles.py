from exiftool import ExifToolHelper
import os
from datetime import date

from base import Session, engine, Base
from MetaData import FileData
from MetaData import ExifData
import xml.etree.ElementTree as xstring


# Create a new session
session = Session()

dirpath = 'C:\TestImage'

result = os.walk(dirpath, topdown=False)

for root, dirs, files in result:
    for name in files:
        print(os.path.join(root, name))






