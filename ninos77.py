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

#============Cats With Hats===================#

cats = range(1,101)
cat_list=[]

#first round, stop at every cat, placing a hat on each one.

for c in cats:
    cat_list.append("cat#"+str(c))
print(cat_list)

#The second round, stop only at every second cat (#2, #4, #6,
#8, and so on).
for c in cats:
    if c % 2 == 0:
        cat_list.append("cat#"+str(c))
print(cat_list)

# The third round, stop only at every third cat (#3, #6, #9, #12,and so on).
for c in cats[1:]:
    if c % 3 != 0 :
        cat_list.append("cat#"+str(c))
print(cat_list)

# for c in cats:
#     if c % 2 == 0 :
#         c *= 2
#         cat_list.append("cat#"+str(c))
# print(cat_list)
# start = 3
# step = 4
# for i in range(start,len(cats)+1,step):
#     cat_list.append("cat#"+ str(cats[i]))
# print(cat_list)

#######=============Turn Your User Into a L33t H4x0r=========================################

my_string =input("Enter your text: ")
new_string = ""
for l in my_string.strip():
    if l == "a":
        #my_string = my_string.replace(l ,"4")
        postion =  my_string.index(l)
        new_letter = my_string[postion]
        new_letter = "4"
        new_string += new_letter
    elif l =="b":
        #my_string = my_string.replace(l ,"8")
        postion =  my_string.index(l)
        new_letter = my_string[postion]
        new_letter = "8"
        new_string += new_letter
    elif l =="e":
        #my_string = my_string.replace(l ,"3")
        postion =  my_string.index(l)
        new_letter = my_string[postion]
        new_letter = "3"
        new_string += new_letter  
    elif l =="l":
        #my_string = my_string.replace(l ,"1")
        postion =  my_string.index(l)
        new_letter = my_string[postion]
        new_letter = "1"
        new_string += new_letter 
    elif l =="o":
        #my_string = my_string.replace(l ,"0")
        postion =  my_string.index(l)
        new_letter = my_string[postion]
        new_letter = "0"
        new_string += new_letter  
    elif l =="s":
        #my_string = my_string.replace(l ,"5")
        postion =  my_string.index(l)
        new_letter = my_string[postion]
        new_letter = "5"
        new_string += new_letter
    elif l =="t":
        #my_string = my_string.replace(l ,"7")
        postion =  my_string.index(l)
        new_letter = my_string[postion]
        new_letter = "7"
        new_string += new_letter     
print(new_string)      
          
#=======================Find the Factors of a Number=====================================#

number = 200

for n in range(1,number+1):
    if number % n == 0:
        print(f"factor number {n}")
        