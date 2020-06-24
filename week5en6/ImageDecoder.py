with open("image.zif", 'rb') as f:
    content = f.read()

with open('header.bmp', 'rb') as bmp:
    header = bmp.read()

headerID = header[0:2]
fileSizeHeader = header[2:6]
reservedSpace = header[6:10]
startPixelArray = header[10:14]
something = header[14:18]
imageWidth = header[18:20]
imageHeight = header[20:22]
something2 = header[22:26]

fileType = content[0:4]
fileWidth = content[4:8]
fileHeight = content[8:12]
fileSize = content[12:16]
colorIndicator = content[16:20]
paletteSize = content[20:24]
paletteData = content[24:24 + int.from_bytes(paletteSize, 'little')]
dataIndicator = content[24 + int.from_bytes(paletteSize, 'little'):24 + int.from_bytes(paletteSize, 'little') + 4]
dataSize = content[24 + int.from_bytes(paletteSize, 'little') + 4:24 + int.from_bytes(paletteSize, 'little') + 8]
pixelData = content[24 + int.from_bytes(paletteSize, 'little') + 8:24 + int.from_bytes(paletteSize,
                                                                                       'little') + 8 + int.from_bytes(
                                                                                        dataSize, 'little')]

print(int.from_bytes(fileWidth, 'little'),int.from_bytes(fileHeight, 'little'),int.from_bytes(fileSize, 'little'))


paletteCounter = 0
paletteList = []
while paletteCounter < int.from_bytes(paletteSize, 'little'):
    paletteList.append(paletteData[paletteCounter:paletteCounter + 4])
    paletteCounter += 4

print(len(paletteList))

pixelCounter = 0
pixelList = []
print(int.from_bytes(dataSize, 'little'))
while pixelCounter < int.from_bytes(dataSize, 'little'):
    pixelList.append(pixelData[pixelCounter:pixelCounter + 4])
    pixelCounter += 4

pixelColorList = []
for x in pixelList:
    pixelColorList.append(paletteList[int.from_bytes(x, 'little')][0:3])

pixelColorList.reverse()

open("zifImage4.bmp", 'bw').write(b''.join(
    [headerID, fileSize, reservedSpace, startPixelArray, something, fileWidth[0:2], fileHeight[0:2], something2,
     b''.join(pixelColorList)]))
