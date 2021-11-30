import sys

print("W31c0m3 70 L33t Ch47")
LetterDict = {"a": "4", "b": "8", "e": "3",
              "l": "1", "o": "0", "s": "5", "t": "7"}


def ReplaceLetter(SelString, SelLetter):
    Result = ""
    for char in SelString:
        if char == SelLetter:
            char = LetterDict[char]
        Result += char
    return Result


for line in sys.stdin:
    PlaceHolder = line
    for letter in LetterDict:
        PlaceHolder = ReplaceLetter(PlaceHolder, letter)
    sys.stdout.write(PlaceHolder)
