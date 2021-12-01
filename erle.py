
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


while True:
    coice = input("Vad vill du göra? 1 = Leet Speak 2 = Quiz")

    if coice == "1":
        leetspeak()
    if coice == "2":
        quiz()
