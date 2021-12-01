# L33t H4x0r translator

L33t_H4x0r_dictionary = ("a", "4", "b", "8", "e", "3",
                         "l", "1", "o", "0", "s", "5", "t", "7")
L33t_H4x0r_dictionary_capitalize = (
    "A", "4", "B", "8", "E", "3", "L", "1", "O", "0", "S", "5", "T", "7")


def list_translator(text, input_list):
    """
    text: is string that will be translate based on input_list
    input_list: need to be a list with strings where even index will be translated to the odd index directly after even index, most be an even number long.
    """
    i = 0
    for x in input_list:  # x is a string in input_list
        # if inder of L33t_H4x0r_dictionary is odd then skip to next loop as its a L33t_H4x0r number.
        if (i % 2) != 0:
            i += 1
            continue

        # support value to keep track last index in string that was found
        last_found_in_string = 0
        while True:
            last_found_in_string = text.find(x, last_found_in_string)

            # if not find more of this letter, then break this while loop.
            if last_found_in_string == -1:
                break
            else:
                # change letter to correponding L33t_H4x0r number
                text = text[:last_found_in_string] + \
                    input_list[int(i+1)] + text[last_found_in_string + 1:]
                # start from next index in next loop.
                last_found_in_string += 1
        i += 1

    return text


def leet_converter():
    user_input_str = str(
        input("Want to talk like a L33t_H4x0r, give me you text and i will help you: "))

    user_input_str = list_translator(user_input_str, L33t_H4x0r_dictionary)
    user_input_str = list_translator(
        user_input_str, L33t_H4x0r_dictionary_capitalize)

    print("here is you L33t_H4x0r text")
    print(user_input_str)


def main():
    leet_converter()


if __name__ == '__main__':
    main()
