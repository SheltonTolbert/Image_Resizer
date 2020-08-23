import PIL 
import os
from PIL import Image
import pathlib


path = str(pathlib.Path(__file__).parent.absolute()).replace('\\','/') + '/images'


print(path)


os.listdir(path)

for file in os.listdir(path):
	f_img = path+"/"+file
	img = Image.open(f_img)
	img = img.resize((2000,2000))
	img.save(f_img)

