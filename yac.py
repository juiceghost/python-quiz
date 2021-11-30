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


questions = ["I always take the lead in group assignments", "I always finish my assignments on time", "Helping others succeed is more important than my own success", "I work a lot on the side with other things than studies", "I like to tinker with hardware"]
scale = "1 = Not true at all, 7 = Extremely true\nλ "
answers = []
feedback = []

print("Welcome to the Interactive Quiz v0.2\n====================================\n\n")
print("How well does the following statements apply to you?\n")
# iterera genom questions och printa varje sträng
for question in questions:
    print(question)
    #print(scale)
    #answers = [5,int(input(scale)),9]
    #print(answers)
    answers.append(int(input(scale)))

# Give the user a result whether he/she takes the lead in group assignments (always, sometimes, never)

# köra ett if-träd som man klättrar ner beroende på vad anvädnaren svarar

# "I always take the lead in group assignments"

if(answers[0] == 1):
    feedback.append("You never take the lead in group assignments")
elif(answers[0] == 7):
    feedback.append("You always take the lead in group assignments")
else:
    feedback.append("You sometimes take the lead in group assignments")

if(answers[1] == 1):
    feedback.append("You never finish your assignments on time")
elif(answers[1] == 7):
    feedback.append("You always finish your assignments on time")
else:
    feedback.append("You sometimes finish your assignments on time")

if(answers[2] == 1):
    feedback.append("Helping others succeed is never more important than your own success")
elif(answers[2] == 7):
    feedback.append("Helping others succeed is always more important than your own success")
else:
    feedback.append("Helping others succeed is sometimes more important than your own success")

# "I work a lot on the side" 3, "I like to tinker with hardware" 4

other_time = answers[-2] * 2.5 + answers[-1] * 0.75

if(3.25 <= other_time <= 8.24):
    feedback.append("You probably have enough time for your studies")
elif(8.25 <= other_time <= 13.24):
    feedback.append("You might want to increase time spent on studies")
else:
    feedback.append("You definitely want to increase time spent on studies")

print(feedback)