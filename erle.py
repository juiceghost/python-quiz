
def leetspeak():
    leet = input("Skriv något: ")

    new = leet.replace("a", "4") .replace(
        "b", "8") .replace("t", "7") .replace("e", "3") .replace("b", "8") .replace("l", "1") .replace("s", "5")
    print(new)


def quiz():
    questions = ["Är du rädd för mörker?", "Har du stora fötter? ",
                 "Kan du åka skidor ", "Varför? "]

    scale = "1 = Stämmer inte alls <---> 5 = Stämmer mycket bra\n"
    print("\n\nVilket husdjur passar dig? By - erle\n============================\n\n")
    answers = []
    print("Hur väl stämmer följande påståenden?")

    for question in questions:
        print(question)

        answers.append(int(input(scale)))

    # print(sum(answers))
    print("Ditt husdjur blir....")
    input()
    if sum(answers) <= 6:
        print("Triceratops")
    elif sum(answers) <= 10:
        print("Elefant")
    elif sum(answers) < 15:
        print("Alligator")
    else:
        print("Cocker Spaniel")


def tempcalc():

    def convert_cel_to_far():
        celsius = float(input("Enter a temperature in degrees C: "))
        far = float(celsius * 9/5 + 32)
        far = round(far, 2)
        print(str(celsius) + " Degrees C is " + str(far) + " degrees F")

    def convert_far_to_cel():
        farenheit = float(input("Enter a temperature in degrees F: "))
        cel = float((farenheit - 32) * 5/9)
        cel = round(cel, 2)
        print(str(farenheit) + " Degrees C is " + str(cel) + " degrees F")

    convert_cel_to_far()
    convert_far_to_cel()


while True:
    coice = input(
        "Vad vill du göra? 1 = Leet Speak 2 = Quiz 3 = Celsius och Farenheitkalkylator ")

    if coice == "1":
        leetspeak()
    if coice == "2":
        quiz()
    if coice == "3":
        tempcalc()
