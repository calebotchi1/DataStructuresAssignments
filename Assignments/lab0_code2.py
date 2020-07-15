# A Python program that counts the number of strings where the string length
# is 2 or more and the first and last character are same from a given list of strings
# and prints out the number

# by Caleb Otchi


def match_counter(strings):

    # a variable to store how many strings have 2 or more characters and have
    # same first and last character
    num = 0

    for i in strings:
        if len(i) > 1 and i[0] == i[-1]:
            num = num + 1
    return num


# A list of strings
list_of_strings = ['abc', 'xyz', 'aba', '1221', 'lool']

print("There are", match_counter(list_of_strings), "strings that have more than two characters\n and have the same first and last character.")

