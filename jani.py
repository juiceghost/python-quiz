# Interactive quiz 16/11 2021 

# Which Avenger are you? Build a personality or recommendation quiz which asks users some questions, stores their answers, and then perform some kind of calculation to give the user a personalized end result that's based on their answers

# Ask the user some questions
#  input()
# Store their answers
#  file write or sqlite
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


question = ["I always take the lead in group assignments", "I always finish my assignments on time", "Helping others succeed is more important than my own success"]
scale = "1 - Not true at all, 7 - Extremely true"
answers = []
print("Welcome to the Interactive Quiz v0.1\n")

# iterera genom listan och printa varje sträng

for index in question:
    print(index)
    print(scale)
    answer.append(int(input(">>>")))
