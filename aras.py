class Question:
    def __init__(self, prompt, answer):
        self.prompt= prompt
        self.answer= answer


question_prompts= [
    "What is the color of the name 'Coca Cola light' on the 50cl can?\n(a) Black\n(b) Red\n(c) Gray\n\n",
    "What is the background color of the label 'Cola light' on the 50cl can? \n(a) Black \n(b) Red \n(c) Gray \n\n",
    "Which sweetener is added in Coca Cola Light, manufactured for Sweden?\n(a) Saccharin\n(b) Aspertame\n(c) Cyclamates\n\n",
    "Which one taste the best, Coca Cola Light OR Coca Cola Zero?\n(a) Zero\n(b) Light\n(c) Tastes the same\n\n",
    "How much Coca Cola Light is Sara drinking every day?\n(a) 50cl\n(b) 1,5L\n(c) 2L\n\n"
]

questions= [
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
    Question(question_prompts[3], "b"),
    Question(question_prompts[4], "c"),
]
print("\n**************************************************************")
print("Welcome to my favorite Quiz! Answer the 5 questions below by \nchoosing your answer (a), (b), or (c).\n")
print("**************************************************************")
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer==question.answer:
            score+=1
    print("=========================================================")
    print ("You got " + str(score) + "/" + str(len(questions)) + " correct! Good Work! Why not selebrate with a \n             Coca Cola Light ;-)")

run_test(questions)
print("=========================================================")


#L33tH4xor
string = input ("Copy and paste the down below text string: \n Diet coke for breakfirst \n Paste here: ")
new_string= string.replace("a", "4").replace("b", "8").replace("e", "3")
print("This is your new string text: \n\n "+ new_string)
