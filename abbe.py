import os


class User:
    # Captures the user's information
    def __init__(self, name):
        # stores a user
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    # def __hash__(self):
    #    return hash((self.name,))

    # def __str__(self):
    #    return self.name


class AnonymousSurvey:
    # Collect anonomys answers to survey question
    def __init__(self, question):
        # store a question, and store responses
        self.question = question
        self.responses = []

    def show_question(self):
        # show the survey question
        print(self.question)

    def store_response(self, new_response):
        # store a response to the survey
        self.responses.append(new_response)

    def show_results(self):
        # show all the responses that have been given
        print('Survey results: ')
        for response in self.responses:
            print(f'- {response}')


# load user(s)
users = []  # List of instances of User
user_file = "users.csv"
if os.path.exists(user_file):
    with open(user_file, mode="r") as file:
        # write header
        # write user data
        lines = file.readlines()
        for line in lines[1:]:
            users.append(User(line.strip()))
survey_responses = []  # List of instances of User
survey_responses_file = "survey_responses.csv"
if os.path.exists(survey_responses_file):
    with open(survey_responses_file, mode="r") as file:
        # write header
        # write user data
        lines = file.readlines()
        for line in lines[1:]:
            survey_responses.append(line.strip())

# print(users)
# load previous survey responses

# make a question and make a survey
question = 'What programming languages did you learn in chronological order?'
my_survey = AnonymousSurvey(question)
survey_completed = False

# show the question and store responses to the question and show results.
my_survey.show_question()
print("Enter 'q' or a blank response at any time to quit. ")
while True:
    response = input('Language: ')
    my_survey.store_response(response)
    if response == 'q' or response == '':
        print(' Thank you to everyone who participated in the survey! ')
        my_survey.show_results()
        break

# survey completed, if user gave at least one response, capture his/her name

if len(my_survey.responses) > 1:
    # User has given at least one response, capture name
    my_user = User(input('Please state your name: '))
    survey_completed = True
try:
    if my_user:
        print(f'Thanks for using the Survey tool, {my_user.name}.')
except:
    print('Thanks for using the Survey tool.')

if survey_completed:
    # Write responses to disk along with user
    with open("users.csv", mode="w") as file:
        # write header
        # write user data
        # write all loaded users, and append latest user if and only if:
        # user does NOT already exist in loaded
        file.write(f'name\n')
        #

        # if not any(isinstance(user, User) for user in users):
        if my_user not in users:
            users.append(my_user)
        for user in users:
            file.write(f'{user.name}\n')
    with open("survey_responses.csv", mode="w") as file:
        # write header
        file.write('user,question,')
        # how many responses are there?
        # response1,response2,response3

        trimmed_responses = my_survey.responses[:-1]

        # given all previous entrances, count commas per line
        # check length of latest trimmed_responses
        #
        max_commas = 0
        for row in survey_responses:
            if row.count(',') > max_commas:
                max_commas = row.count(',')
        if len(trimmed_responses) + 2 > max_commas:
            max_commas = len(trimmed_responses) + 2
        # print(max_commas)
        # input()
        for index in range(max_commas - 2):
            if index < max_commas - 3:
                file.write(f'response{index + 1},')
            else:
                file.write(f'response{index + 1}\n')
        """ for index, item in enumerate(trimmed_responses):
            if index < len(trimmed_responses) - 1:
                file.write(f'response{index + 1},')
            else:
                file.write(f'response{index + 1}\n') """
        # write survey data
        for row in survey_responses:
            row_commas = row.count(',')
            added_commas = ''
            for i in range(row_commas, max_commas - 1):
                added_commas += ','
            file.write(f'{row}{added_commas}\n')  # add commas if needed
        file.write(f'{my_user.name},{my_survey.question},')
        for index, item in enumerate(trimmed_responses):
            if index < len(trimmed_responses) - 1:
                file.write(f'{item},')
            else:
                if index + 2 < max_commas:  # add commas
                    row_added_commas = ''
                    for i in range(index + 2, max_commas):
                        row_added_commas += ','
                file.write(f'{item}{row_added_commas}\n')

""" 
# en csv-fil med alla users:
name
yac
abbe
kjebo

# csv-file för surveys
question,response1,response2,response3,response4,response5...
What programming language did you learn first? ,C,Java,ASM,AMOS,Javascript

"""
