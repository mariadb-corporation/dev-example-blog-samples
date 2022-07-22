from exiftool import ExifToolHelper
import os

path = "c:\\TestImage"

paths = []

for file in os.listdir(path):
    if os.path.isdir(path + '\\' + file):
        paths.append(path + file)
    else:
        sfile = path + '\\' + file
        print(sfile)
        with ExifToolHelper() as et:
            try:
                for d in et.get_tags(sfile, tags=['EXIF:*']):
                    for k, v in d.items():
                        print(f"Dict: {k} = {v}")
            except:
                print('Fehler')
