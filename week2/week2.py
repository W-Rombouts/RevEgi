import codecs
import string

filename = 'casus6output'
englishWordList = open('englishWordList.txt','r').read().strip().split('\n')

matchedOutputFile = open(filename+'Matchedoutput.txt','w')
#print(englishWordList)
with open(filename+'.txt', 'r') as f:
    data = f.read().strip().split('\n')

outputFile = open(filename+'output.txt','w')
counter =0
for r in data:
        counter+=1
        test = r
        r = codecs.decode(r, 'rot_13')
        raw = r
        f = 1
        for char in raw:
            if char not in string.ascii_letters:
                f = 0
        if f and len(raw.strip()):
            outputFile.writelines(raw+'\n')
            print(test + ' | ' + raw)
        for word in englishWordList:
            if r == word:
                matchedOutputFile.writelines(word+'\n')
                print(word + ' @ ' + str(int((counter/len(data))*100))+'%')
