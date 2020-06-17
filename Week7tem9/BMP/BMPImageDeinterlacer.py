with open('banana_1Converted.bmp', 'rb') as bmp:
    header = bmp.read()

headerID = header[0:2]
fileSizeHeader = int.from_bytes(header[2:6], 'little')
reservedSpace = header[6:10]
startPixelArray = header[10:14]
something = header[14:18]
imageWidth = int.from_bytes(header[18:20], 'little')
imageHeight = int.from_bytes(header[20:22], 'little')
something2 = header[22:int.from_bytes(startPixelArray,'little')]
pixelArray = header[int.from_bytes(startPixelArray,'little'):-1]
counter = 0
picture1 = []
picture2 = []
while counter < len(pixelArray):
    if int(counter) % 2 == 0:
        picture1.append(pixelArray[counter:counter + 3])
    else:
        picture2.append(pixelArray[counter:counter + 3])
    counter += 3

open("Image1.bmp", 'bw').write(b''.join(
    [headerID, int(fileSizeHeader / 2).to_bytes(4, 'little'), reservedSpace, startPixelArray, something,
     int(imageWidth / 2).to_bytes(2, 'little'), int(imageHeight / 2).to_bytes(2, 'little'), something2,
     b''.join(picture1)]))

open("Image2.bmp", 'bw').write(b''.join(
    [headerID, int(fileSizeHeader / 2).to_bytes(4, 'little'), reservedSpace, startPixelArray, something,
     int(imageWidth / 2).to_bytes(2, 'little'), int(imageHeight / 2).to_bytes(2, 'little'), something2,
     b''.join(picture2)]))
