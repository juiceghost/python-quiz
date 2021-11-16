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