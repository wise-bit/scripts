from PIL import Image
import os

x = 290
y = 30
width = 1060
height = 1950

for filename in os.listdir("."):
  if filename.endswith(".png") or filename.endswith(".jpg"):
    img = Image.open(filename)
    cropped_img = img.crop((x, y, x + width, y + height))
    cropped_img.save(filename)

