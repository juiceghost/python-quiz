class AnonymousSurvey:
    #Collect anonomys answers to survey question

    def __init__(self, question):
            #store a question, and store responses
        self.question = question
        self.responses = []
    
    def show_question(self):
        #show the survey question
        print(self.question)

    def store_response(self, new_response):
        #store a response to the survey
        self.responses.append(new_response)

    def show_results(self):
        #show all the responses that have been given
        print('Survey results: ')
        for response in self.responses:
            print(f'- {response}')

#make a question and make a survey
question = 'What programming language did you learn first? '
my_survey = AnonymousSurvey(question)

#show the question and store responses to the question and show results.
my_survey.show_question()
print("Enter 'q' at any time to quit. " )
while True:
    response = input('Language: ')
    my_survey.store_response(response)
    if response == 'q':
        print(' Thank you to everyone who participated in the survey! ')
        my_survey.show_results()
        break
    