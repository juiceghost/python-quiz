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
# def translate():
#     usr_input=(str(input("Enter some text: ")))
#     usr_input=usr_input.replace("a", "4")
#     usr_input=usr_input.replace("b", "8")
#     usr_input=usr_input.replace("e", "3")
#     usr_input=usr_input.replace("l", "1")
#     usr_input=usr_input.replace("o", "0")
#     usr_input=usr_input.replace("s", "5")
#     usr_input=usr_input.replace("t", "7")
#     print(usr_input)
#     return usr_input
# translate()
#######################################################

#FUNCTIONS
# def multi(x, y):
#    """"Returns the result of x*y"""
#    result=x*y
#    return result    
# product=multi(3, 3)
# print(product)
# help(multi)

#1,
# def cube(x):
#     result=x**3
#     return  result
# powered=cube(3)
# print(powered)

#2,
# def greet(name):
#     print(f'Hello {name}!')
#     return name
# greet("Maurito")

def convert_cel_to_far(C):
    F = C * 9/5 + 32
    print(f'{C} degrees C = {round(F, 2)} degrees F')
    return F
convert_cel_to_far(C=float(input("Enter a temperature in Celsius degrees: ")))

def convert_far_to_cel(F):
    C = (F - 32) * 5/9
    print(f'{F} degrees F = {round(C, 2)} degrees C')
    return C
convert_far_to_cel(F=float(input("Enter a temperature in Fahrenheit degrees: ")))


