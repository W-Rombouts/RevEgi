from PIL import Image


img = Image.open("banana_1.png")
file_out = "banana_1Converted.bmp"
img.save(file_out)