from exiftool import ExifToolHelper
with ExifToolHelper() as et:
    for d in et.get_metadata('c:\\TestImage\\2019-04-30 21.01.29 2033657518206836718_9998858143.jpg'):
        for k, v in d.items():
            print(f"Dict: {k} = {v}")