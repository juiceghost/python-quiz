from alphabet import Alphabet
#Create a "Code" Generator that takes text as input and replaces each letter with another letter, and outputs the "encoded" message
START_SHIFT = 1
END_SHIFT = 30
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
while True:
        try:
            shift = int(input(f"Type the shift number between ({START_SHIFT}- {END_SHIFT}):\n"))
            if shift >= START_SHIFT and shift <=  END_SHIFT:
                break
            else:
                print("Your choice number is wrong!!!")
        except ValueError:
            print("You have to chose a integer\n")
            pass

def encode(text,shift):
    new_word = ""
    for letter in text.strip():
        if letter == " " or letter == "?" or letter == "," or letter == ".":
            new_word += letter
        else:    
            position = Alphabet.index(letter)
            new_position = position + shift
            new_letter = Alphabet[new_position]
            new_word += new_letter
    print (f"Your Message or Word is:{new_word}")


def decode(text,shift):
    new_word = ""
    for letter in text.strip():
        if letter == " " or letter == "?" or letter == "," or letter == ".":
            new_word += letter
        else:    
            position = Alphabet.index(letter)
            new_position = position - shift
            new_letter = Alphabet[new_position] 
            new_word += new_letter
    print (f"Your Message or Word is: {new_word}")



def start_encode_decode(direction):
    if direction == "encode":
        encode(text,shift)
    else:
        decode(text,shift)    


start_encode_decode(direction)