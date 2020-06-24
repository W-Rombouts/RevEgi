import tools
import copy


class FileHeader:
    def __init__(self, initialFileIndex, sizeOfFile, sizeOfName, nameOfFile):
        self.initialFileIndex = initialFileIndex
        self.sizeOfFile = sizeOfFile
        self.sizeOfName = sizeOfName
        self.nameOfFile = nameOfFile


bruteForceMode = True

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
headerBlocks = []
locationListList = []
for value in range(0, int.from_bytes(sizeOfFileTable, 'big') + 1):
    headerBlocks.append(value)
locationListList.append(headerBlocks)

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
zifFile = []
counter = 0
skip = False
headerFound = False
for blockData in fileData:
    if not headerFound and b''.join(blockData[0:2]).decode('utf-8', errors='ignore').__contains__("ZIF1"):
        zifFile.append(b''.join(blockData))
        headerFound = True

    if len(set(blockData)) >= 4:
        for byte in blockData:
            if int.from_bytes(byte, 'little') < 4278190080:  # all colortable data is bigger than 000000ff
                if int.from_bytes(byte, 'little') != 1096040772:  # Data Tag
                    skip = True
                break
        if not skip:
            zifFile.append(b''.join(blockData))
    skip = False

skip = False
for blockData in fileData:
    if len(set(blockData)) >= 4:
        for byte in blockData:
            if int.from_bytes(byte, 'little') > 266756:  # All blockdata is smaller than the colortable size
                if int.from_bytes(byte, 'little') != 638264843:  # SlackSpace
                    skip = True
                break
        if not skip:
            counter += 1
            zifFile.append(b''.join(blockData))
        skip = False
print(counter)
with open('Diagonal Image Conversion/image.zif', 'bw') as zifContainer:
    zifContainer.write(b''.join(zifFile))

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
    locationListList.append(locationList)
    foundBlockList = []
    if not bruteForceMode:
        for x in locationList:
            foundBlockList.append(b''.join(fileData[x - 1]))

        with open(file.nameOfFile, 'bw') as finalFile:
            finalFile.write(b''.join(foundBlockList))

newListSomeReason = []

if bruteForceMode:
    copyBlockList = copy.deepcopy(blockList)

    for List in copyBlockList:
        if len(set(List)) == 1:
            copyBlockList.remove(List)
        else:
            newListSomeReason.append(b''.join(List))
    with open('test.data', 'bw') as finalfinalFile:
        finalfinalFile.write(b''.join(newListSomeReason))

    copyBlockList = newListSomeReason
    counterHeader = 0
    counterBody = 0
    foundParts = [newListSomeReason[11]]
