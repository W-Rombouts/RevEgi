from collections import defaultdict

filename = 'StenographedImage.png'
with open(filename, 'rb') as f:
    content = f.read()

counter = 0
start = 0

filesList = defaultdict(list)

while counter < len(content):
    fileID = content[start:start + 4]
    startSize = start + 4
    size = content[startSize:startSize + 4]
    startData = startSize + 4
    data = content[startData:startData + int.from_bytes(size, 'big')]
    filesList[int.from_bytes(fileID, 'big')].append(data)
    start = startData + int.from_bytes(size, 'big')

    counter = start

for x in filesList:
    open('FilestreamBanana' + str(x), 'bw').write(b''.join(filesList[x]))
