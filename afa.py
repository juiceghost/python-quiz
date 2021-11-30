# Interactive quiz 16/11 2021 

# Which Avenger are you? Build a personality or recommendation quiz which asks users some questions, stores their answers, and then perform some kind of calculation to give the user a personalized end result that's based on their answers

# Ask the user some questions
#  input()
# Store their answers
#  memory, file write or sqlite
# Perform some kind of calculation
#  math
# Give the user a personalized end result (based on their answers)
#  print()

# Inputs
# Användaren lämnar svar på frågor
# Outputs
# Programmet ställer frågor till användaren
# Efter beräkning ges användaren sitt resultat

# "How well does this apply for you?"

# "I always take the lead in group assignments"
# "1 - Not true at all .. 7 - Extremely true"

# "I always finish my assignments on time"
# "1 - Not true at all .. 7 - Extremely true"

# "Helping others succeed is more important than my own success"
# "1 - Not true at all .. 7 - Extremely true"

# Start with an extremely small and simple version of your project 
# Add more functionality later


class Person:
    questions = [
        "I always take the lead in group assignments: ",
        "I always finish my assignments on time: ",
        "Helping others succeed is more important than my own success: ",
        "I work a lot on the side with other things than studies: ",
        "I like to tinker with hardware: "
    ]

    @staticmethod
    def check_result(user_input, message):
        if user_input == 1:
            return message[0]
        elif user_input == 7:
            return message[1]
        else:
            return message[2]

    def check_question_1(self):
        doc_answer = [
            "You never take the lead in group assignments",
            "You always take the lead in group assignments",
            "You sometimes take the lead in group assignments"
        ]
        return Person.check_result(person.answers['1'], message=doc_answer)

    def check_question_2(self):
        doc_answer = [
            "You never finish your assignments on time",
            "You always finish your assignments on time",
            "You sometimes finish your assignments on time"
        ]
        return Person.check_result(person.answers['2'], message=doc_answer)

    def check_question_3(self):
        doc_answer = [
            "Helping others succeed is never more important than your own success",
            "Helping others succeed is always more important than your own success",
            "Helping others succeed is sometimes more important than your own success"
        ]
        return Person.check_result(person.answers['3'], message=doc_answer)

    def check_question_4_and_5(self):
        other_time = person.answers['4'] * 2.5 + person.answers['5'] * 0.75
        if (3.25 <= other_time <= 8.24):
            return "You probably have enough time for your studies"
        elif (8.25 <= other_time <= 13.24): \
            return "You might want to increase time spent on studies"
        else:
            return "You definitely want to increase time spent on studies"

person = Person()
person.answers = {}

print("1 = Not true at all, 7 = Extremely true\n ")
for index, item in enumerate(person.questions, 1):
    user_input = int(input(item))
    person.answers.update({f'{index}': user_input})

print(person.answers)
print(person.check_question_1())
print(person.check_question_2())
print(person.check_question_3())
print(person.check_question_4_and_5())

# Give the user a result whether he/she takes the lead in group assignments (always, sometimes, never)

# köra ett if-träd som man klättrar ner beroende på vad anvädnaren svarar

# "I always take the lead in group assignments"