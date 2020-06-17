UpsideDownCharacterList = [' ', 'z', 'ʎ', 'x', 'ʍ', 'ʌ', 'n', 'ʇ', 's', 'ɹ', 'b', 'd', 'o', 'u', 'ɯ', 'l', 'ʞ', 'ɾ',
                           'ᴉ', 'ɥ', 'ƃ', 'ɟ', 'ǝ', 'p', 'ɔ', 'q', 'ɐ', 'Z', '⅄', 'X', 'M', 'Λ', 'Ո', 'Ʇ', 'S', 'ᴚ',
                           'ტ', 'Ԁ', 'O', 'N', 'W', '⅂', 'ꓘ', 'ᒋ', 'I', 'H', '⅁', 'Ⅎ', 'Ǝ', 'ᗡ', 'Ɔ', 'ᗺ', 'Ɐ']
CharList = [' ', 'z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g',
            'f', 'e', 'd', 'c', 'b', 'a', 'Z', 'Y', 'X', 'W', 'V', 'U', 'T', 'S', 'R', 'Q', 'P', 'O', 'N', 'M', 'L',
            'K', 'J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A']
englishWordList = open('englishWordList.txt', 'r').read().strip().split('\n')

def SearchUpsideDown(text: str):
    index = 0
    indexList = []
    hitList = []
    for x in text:
        if x in UpsideDownCharacterList:
            hitList.append(x)
            indexList.append(index)
            print(str(int((index / len(text)) * 100)) + "%")
        index += 1

    return ''.join(hitList), indexList


def RotateUpsideDownText(text: str):
    reverseText = []
    counter = 0
    for x in text:
        index = 0
        for char in UpsideDownCharacterList:
            if char == x:
                reverseText.append(CharList[index])
            index += 1
        counter += 1
        print(str(int((counter / len(text)) * 100)) + "%")
    reverseText.reverse()
    return ''.join(reverseText)


def FindEnglishWords(text: str):
    text = text.strip().split(' ')
    foundWords = []
    wordLocation = []
    wordCounter = 0
    for w in text:
        for word in englishWordList:
            if w == word:
                foundWords.append(word)
                wordLocation.append(wordCounter)
                print(str(int((wordCounter / len(text)) * 100)) + "%")
        wordCounter += 1
    return ' '.join(foundWords),wordLocation

def getUpsideDownWords(text:str):
    UpsideDownString, LocationList = SearchUpsideDown(text)
    rightSideUpString = RotateUpsideDownText(UpsideDownString)
    foundWords, wordLocation = FindEnglishWords(rightSideUpString)
    return foundWords