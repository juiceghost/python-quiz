"""python quiz v.0.1.0"""
n = 1
answers = []

logo = """
┌─┐┬ ┬┌┬┐┬ ┬┌─┐┌┐┌  ┌─┐ ┬ ┬┬┌─┐
├─┘└┬┘ │ ├─┤│ ││││  │─┼┐│ ││┌─┘
┴   ┴  ┴ ┴ ┴└─┘┘└┘  └─┘└└─┘┴└─┘
"""

questions = {
    "What is your favourite color? ": ["Green", "Food", "Yellow", "Yeah..."],
    "What is your favourite food?  ": ["Baked beans", "Food", "Banan", "Aspirins"],
    "How do you react on stress? ": ["I'll kill you", "Food", "Stress?", "That's gonna wake the neighbors"],
    "Would you say the glass is half full or half empty? ": ["Empty", "Food", "Half full",
                                                             "All right, that's enough of this kung-fu shit!"],
    "How do you spend your vacation? ": ["Alone in the dark", "Food", "Being happy!",
                                         "Hey Carmine, let me ask you something: what sets off a metal detector "
                                         "first? The lead in your ass or the shit in your brains?"]
}

nr_questions = len(questions)
result = ["Hulken", "Bulken", "Clownen Manne", "John McClane"]


def calc_res(score: list) -> str:
    """Calculates score
    Parameters:
        score: list
        A list containing integers representing the answers from the quizee
    Returns:
        : str
    """
    mid = sum(score) / len(questions)
    print("\033[H\033[J", end="")  # explained on https://stackoverflow.com/a/50560686
    return f'{logo}\nYou are {result[round(mid) - 1]}\n'


for key, value in questions.items():
    print("\033[H\033[J", end="")  # explained on https://stackoverflow.com/a/50560686
    print(logo)
    print(f'Question number {n} of {nr_questions}\n')
    print(f'{key}\n')
    n += 1
    for idx, i in enumerate(value):
        print(f'{idx + 1}: {i}')

    while True:
        answer = input(">>> ")
        if answer.isnumeric() and int(answer) < 5:
            answers.append(int(answer))
            break
        else:
            print("Error! Try again.")
print(calc_res(answers))
