import tools


filename = 'dump.zufs'
with open(filename, 'rb') as f:
    content = f.read()
    blockSize = content[0:4]

blockList = tools.ConvertToBlocksAndBytes(content, blockSize, byteSize=4)

meta = blockList[0]
blockSize = meta[0]
sizeOfMeta = meta[1]
sizeOfFileDirectory = meta[2]
sizeOfFileTable = meta[3]

fileDirectory = blockList[1]
initialFileIndex = fileDirectory[0]
sizeOfFile = fileDirectory[1]
sizeOfName = fileDirectory[2]
binaryNameOfFile = fileDirectory[3:3 + (int(int.from_bytes(sizeOfName, 'big') / 4)) + 1]
byteWideNameOfFile = b''.join(binaryNameOfFile).decode('utf-8')
nameOfFile = byteWideNameOfFile[0:(int.from_bytes(sizeOfName, 'big'))]

fileTable = blockList[2:(2 + int.from_bytes(sizeOfFileTable, 'big'))]

fileData = blockList[(3 + int.from_bytes(sizeOfFileTable, 'big')):len(blockList) + 1]

value = -1
locationList = [int.from_bytes(initialFileIndex, 'big')]
while str(value) != str('0'):
    if value == -1:
        value = int.from_bytes(fileTable[0][int(locationList[0] + 1 / 4)], 'big')
        locationList.append(value)
    else:
        value = int.from_bytes(fileTable[0][int(value + 1 / 4)], 'big')
        locationList.append(value)
locationList.pop()

foundBlockList = []
for x in locationList:
    foundBlockList.append(b''.join(fileData[x - 1]))


with open(nameOfFile, 'bw') as file:
    file.write(b''.join(foundBlockList))
