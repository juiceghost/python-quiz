import sqlite3

conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('mydatabase.db')
c = conn.cursor()

# create a table
# c.execute("""CREATE TABLE result ( result text ))""")

# Query the database and return all records


def show_all():

    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM result")
    items = c.fetchall()

    for item in items:
        print(item)

    conn.commit()
    conn.close()

# Add a new record to the table


def add_one(result):
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()
    c.execute("INSERT INTO result (RESULT) VALUES (?)", (result))
    conn.commit()
    conn.close()

# Interactive quiz 16/11 2021
# def insert_variable_into_table(result):

#     conn = sqlite3.connect('mydatabase.db')
#     c = conn.cursor()

#     sqlite_insert_with_param = """INSERT INTO result
#                             (result)
#                             VALUES (?);"""
#     data_tuple = (result)
#     c.execute(sqlite_insert_with_param, data_tuple)
#     conn.commit()
#     conn.close()


# Which Avenger are you? Build a personality or recommendation quiz which asks users some questions, stores their answers, and then perform some kind of calculation to give the user a personalized end result that's based on their answers
print("Welcome to this ineractive quiz\nWho among the Avengers are you?\n Iron Man\nCaptain America\nHulken\nThor\nBlack Widow\nHawkeye.")

# Ask the user some questions
questions = ["How much do you like really tight tights?"]
# , "How patriotic are you?", "How much anger managment do you need?", "How do you go to work?", "How rich are you?",
#             "How humble are you?", "How smart are you?"]
answers = []
scale = "From 1 - 7 how much do recognize yourself? 1 = not at all, 7 = totally\n-->"
for q in questions:
    print(q)
    answers.append(int(input(scale)))
    print(answers)
#  - Use string input
# Store their answers

#   - Store in list or some sort of array, for example numpy-array
# Perform some kind of calculation
# result = []
question1 = "How smart are you? answer from 1 - 3"
question2 = "How much do you like working with gear? answer from 1 - 3"
for i in answers:
    if 1 <= i <= 3:
        print("You can be some of these Angengers, Iron man, Hulk, Hawkeye. Here is next question")
        ans = (int(input(question1)))
        if ans == 1:
            result = 'HULK, Smash and Bash is your thing'
            # Hard coded way to add one:

            # c.execute(
            #     "INSERT INTO result VALUES('data_tuple')")

            # Another way of adding to database table:

            # insert_variable_into_table((result,))
            # conn.commit()
        elif ans == 2:
            result = 'HAWKEYE, You have super vision, but you are average in brains...'
        else:
            result = 'IRONMAN, Smart, rich playboy, congrats or whatever...'
    elif 4 <= i <= 7:
        print("You can be some of these Anvengers, Black Widow, Thor, Captain America. Here is next question")
        ans = int(input(question2))
        if 2 <= ans <= 3:
            finish = input("Do you like bad weather? y/n\n-->")
            if finish == "y":
                result = 'THOR, you are the god of thunder!'
            else:
                result = 'CAPTAIN-AMERICA, yay you are an patriotic person'
        else:
            result = 'BLACK-WIDOW, You really like black tight suits, but you really kick a guys buts'

add_one((result,))
show_all()
#   - I would use a if-statement to kind of climb down a tree.
#   - Or evaluate all answers as numbers, and
# to if ""if this andadddd this equals x you are thix avenger# Give the user a personalized end result (based on their answers)
#   - Print the answer

# Inputs
# Användaren lämnar svar på frågor

# Outputs
# Programmet ställer frågor till användaren
# Efter beräkning ges användaren sitt resultate thix avenger# Give the user a personalized end result (based on their answers)
#   - Print the answer

# Inputs
# Användaren lämnar svar på frågor

# Outputs
# Programmet ställer frågor till användaren
# Efter beräkning ges användaren sitt resultat
