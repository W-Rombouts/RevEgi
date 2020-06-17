import tools

class FileHeader:
    def __init__(self, initialFileIndex, sizeOfFile, sizeOfName, nameOfFile):
        self.initialFileIndex = initialFileIndex
        self.sizeOfFile = sizeOfFile
        self.sizeOfName = sizeOfName
        self.nameOfFile = nameOfFile


filename = 'casus.zufs'
with open(filename, 'rb') as f:
    content = f.read()
    blockSize = content[0:4]

blockList = tools.ConvertToBlocksAndBytes(content, blockSize, byteSize=4)

meta = blockList[0]
blockSize = meta[0]
sizeOfMeta = meta[1]
sizeOfFileDirectory = meta[2]
sizeOfFileTable = meta[3]

fileDirectory = b"".join(blockList[1])
fileList = []
startIndicator = 0
endLine = -1
while endLine != 0:
    initialFileIndex = fileDirectory[0 + startIndicator:4 + startIndicator]
    sizeOfFile = fileDirectory[4 + startIndicator:8 + startIndicator]
    sizeOfName = fileDirectory[8 + startIndicator:12 + startIndicator]
    binaryNameOfFile = fileDirectory[
                 12 + startIndicator:12 + startIndicator + (int.from_bytes(sizeOfName, 'big'))]

    nameOfFile = binaryNameOfFile.decode("utf-8")
    startIndicator = 12 + startIndicator + (int.from_bytes(sizeOfName, 'big'))
    endLine = int.from_bytes(sizeOfFile, 'big')
    if endLine != 0:
        fileList.append(FileHeader(initialFileIndex, sizeOfFile, sizeOfName, nameOfFile))

fileTable = blockList[2:(2 + int.from_bytes(sizeOfFileTable, 'big'))]

fileData = blockList[(3 + int.from_bytes(sizeOfFileTable, 'big')):len(blockList) + 1]

for file in fileList:

    value = -1
    locationList = [int.from_bytes(file.initialFileIndex, 'big')]
    while str(value) != str('0'):
        if value == -1:
            value = int.from_bytes(fileTable[0][int(locationList[0] + 1 / 4)], 'big')
            locationList.append(value)
        else:
            fileTableNumber = int(int(value + 1 / 4) / 1024)
            value = int.from_bytes(fileTable[fileTableNumber][int(value + 1 / 4) - (fileTableNumber * 1024)], 'big')
            locationList.append(value)
    locationList.pop()

    foundBlockList = []
    for x in locationList:
        foundBlockList.append(b''.join(fileData[x - 1]))

    with open(file.nameOfFile, 'bw') as finalFile:
        finalFile.write(b''.join(foundBlockList))
