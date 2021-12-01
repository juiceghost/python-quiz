#Review Exercises

#2,
#the_string = "Somebody said something to Samantha."
#the_new_string = the_string.replace("s", "x")
#print(the_new_string)

#3,
#usr_inp = str(input("Hello User! What's your name? "))
#letter_found = usr_inp.find("a")
#print("The index of the letter is: ", letter_found)

#Leet Haxor
def translate():
    usr_input=(str(input("Enter some text: ")))
    usr_input=usr_input.replace("a", "4")
    usr_input=usr_input.replace("b", "8")
    usr_input=usr_input.replace("e", "3")
    usr_input=usr_input.replace("l", "1")
    usr_input=usr_input.replace("o", "0")
    usr_input=usr_input.replace("s", "5")
    usr_input=usr_input.replace("t", "7")
    print(usr_input)
    return usr_input
translate()
