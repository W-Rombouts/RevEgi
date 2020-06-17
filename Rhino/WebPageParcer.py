import copy


def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub) # use start += 1 to find overlapping matches

file = open('rhino.txt','r',errors='ignore')
text = file.read();

pages = list(find_all(text,'<html>'))
pages.append(len(text))
PageList = []
prevLoc = 0

print(len(pages))

for x in pages:
    PageList.append(text[prevLoc:x+7])
    prevLoc = x


counter = 1
for y in PageList:
    f = open('Webpage'+str(counter)+'.html','w+')
    f.write(y)
    f.close()
    counter +=1