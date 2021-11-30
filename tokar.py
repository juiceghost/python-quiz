
def speak_to_leet(trans_str: str) -> str:
    char = "abelost"
    leet = "4831057"
    char_to_leet = trans_str.maketrans(char, leet)
    return trans_str.translate(char_to_leet)


def leet_to_speak(trans_str: str) -> str:
    char = "abelost"
    leet = "4831057"
    leet_to_char = trans_str.maketrans(leet, char)
    return trans_str.translate(leet_to_char)


def translate():
    input_str = input("Enter some text: ")
    print(speak_to_leet(input_str))
    input_str = input("3n73r 50m3 73x7: ")
    print(leet_to_speak(input_str))
