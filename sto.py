# samantha = "Somebody said something to Samantha."
# result = samantha.replace('s', 'x')
# print(result)

def translate(string):
    translation = {'a': '4', 'b': '8', 'e': '3',
                   'l': '1', 'o': '0', 's': '5', 't': '7'}
    for key in translation:
        print(f'key: {key} - translation[key]: {translation[key]}')
        string = string.replace(key, translation[key])
    return string

# Denna funktion ska göra samma sak som challengen MEN
# utan att använda replace, translate, make_trans
# lösningen SKA använda en lista av tuples samt find
# "leet" -> "1337"


def replace(string, old, new):
    while string.find(old) != -1:
        index = string.find(old)
        string = string[:index]+new+string[index+1:]
    return string


table = [('a', '4'), ('b', '8'), ('e', '3'), ('l', '1'),
         ('o', '0'), ('s', '5'), ('t', '7')]
text = input('Enter some text: ')
for item in table:
    text = replace(text, item[0], item[1])
print(text)


# # questions from https://www.welovequizzes.com/multiple-choice-quiz-questions-and-answers/

# '''
# Function: ask('putquestionhere'):
#     answer=input(putquestionhere)
#     try:
#         answer is x
#             do this
#         elif etc
#             do that
#         return result
#     except:
#         "that answer didn't work"

# for question in questions:
#     ask(question)
# '''
# questions=['\nIn 1768, Captain James Cook set out to explore which ocean?\nA. Pacific Ocean\nB. Atlantic Ocean\nC. Indian Ocean\nD. Arctic Ocean\n', '\nWhat is actually electricity?\nA. A flow of water\nB. A flow of air\nC. A flow of electrons\nD. A flow of atoms\n', 'Which of the following is not an international organisation?\nA. FIFA\nB. NATO\nC. ASEAN\nD. FBI\n', '\nWhat is the most points that a player can score with a single throw in darts?\nA. 20\nB. 40\nC. 60\nD. 80\n', '\nWhich of the following is a song by the German heavy metal band “Scorpions”?\nA. Stairway to Heaven\nB. Wind of Change\nC. Don’t Stop Me Now\nD. Hey Jude\n', '\nWhat is the speed of sound?\nA. 120 km/h\nB. 1,200 km/h\nC. 400 km/h\nC. 700 km/h\n', '\nWhat is the main component of the sun?\nA. Liquid lava\nB. Gas\nC. Molten iron\nD. Rock\n', '\nThe phrase: ”I think, therefore I am” was coined by which philosopher?\nA. Socrates\nB. Plato\nC. Aristotle\nD. Descartes\n', '\nIn total, how many novels were written by the Bronte sisters?\nA. 4\nB. 5\nC. 6\nD. 7\n', '\nWhich did Viking people use as money?\nA. Rune stones\nB. Jewellery\nC. Seal skins\nD. Wool\n']

# answers='ACDCBBBDDB'

# user_answers=''

# score=0

# def ask(question):
#     global user_answers
#     answer=input(question+'--> ')
#     if answer.upper()=='A':
#         user_answers+='A'
#     elif answer.upper()=='B':
#         user_answers+='B'
#     elif answer.upper()=='C':
#         user_answers+='C'
#     elif answer.upper()=='D':
#         user_answers+='D'
#     else:
#         print('Please try again!')
#         ask(question)

# print('\nWelcome to this quiz!\nYou\'ll be asked 10 multiple choice questions, and at the end you get to see your score.\nTo answer a question, input either of the letters A, B, C or D followed by ENTER key.')

# for question in questions:
#     ask(question)

# for n in range(len(answers)):
#     if answers[n]==user_answers[n]:
#         score+=1

# print(f'\nYou scored {score} out of 10 points.\n')
