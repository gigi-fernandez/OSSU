# Write a while loop that starts at the last character in the
# string and works its way backwards to the first character in the string,
# printing each letter on a separate line, except backwards.

word = input('Type something that will be spelled backwards:\n')
index = len(word) - 1

while index >= 0:
    print(str(word[index]))
    index = index - 1
