from utilitybelt import change_charset


def translate(my_string):

    # denna lösning kan översätta ett ord i taget....
    originalph = "abcdefghijklmnopqrstuvwxyz"
    leetalph = "48cd3fghijk1mn0pqr57uvwxyz"

    # Min andra lösning som funkade galant.
    # replacements = (('a', '4'), ('b', '8'), ('e', '3'),
    #                 ('l', '1'), ('o', '0'), ('s', '5'), ('t', '7'))

    # new_string = my_string
    # for old, new in replacements:
    #     new_string = new_string.replace(old, new)
    new_string = change_charset(my_string, originalph, leetalph)

    return new_string


translateMe = input("Write a word you want to translate: ")

print(translate(translateMe))
