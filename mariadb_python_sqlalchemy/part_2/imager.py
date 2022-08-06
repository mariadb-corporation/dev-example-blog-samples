import os
from PIL import Image


path = "c:\\TestImage"

for file in os.listdir(path):
    print(os.path.join(path, file))
    im = Image.open(os.path.join(path, file))
    im.show()