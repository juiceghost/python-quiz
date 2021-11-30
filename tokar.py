# Interactive quiz 16/11 2021 

# Which Avenger are you? Build a personality or recommendation quiz which asks users some questions, stores their answers, and then perform some kind of calculation to give the user a personalized end result that's based on their answers

# Ask the user some questions
#  
# Store their answers
# Perform some kind of calculation
# Give the user a personalized end result (based on their answers)

# Inputs
# Användaren lämnar svar på frågor

# Outputs
# Programmet ställer frågor till användaren
# Efter beräkning ges användaren sitt resultat


# "What is your favourite color? ": ["Green", "Food", "Yellow", "Yeah..."],

def main():
    #print(questions)
    #print(questions.items())
    for key, value in questions.items():
        print(f'{key}\n')
        for idx, i in enumerate(value):
            print(f'{idx + 1}: {i}')
        scoring()


def scoring():
    while True:
        answer = input(">>> ")
        if answer.isnumeric() and int(answer) < 5:
            score.append(int(answer))
            break
        else:
            call_error()


def call_error():
    print("Error! Try again.")


questions = {
    "What is your favourite color? ": ["Green", "Food", "Yellow", "Yeah..."],
    "What is your favourite food?  ": ["Baked beans", "Food", "Banan", "Aspirins"],
    "How do you react on stress? ": ["I'll kill you", "Food", "Stress?", "That's gonna wake the neighbors"],
    "Would you say the glass is half full or half empty? ": ["Empty", "Food", "Half full", "All right, that's enough of this kung-fu shit!"],
    "How do you spend your vacation? ": ["Alone in the dark", "Food", "Being happy!", "Hey Carmine, let me ask you something: what sets off a metal detector first? The lead in your ass or the shit in your brains?"]
    }

result = ["Hulken", "Bulken", "Clownen Manne", "John McClane"]

score = []

main()

mid = sum(score) / len(questions)
#print(mid)
print(f'You are {result[round(mid) - 1]}')