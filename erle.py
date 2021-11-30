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
