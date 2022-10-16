# Rewrite the program that prompts the user for a list of 
# numbers and prints out the maximum and minimum of the numbers at
# the end when the user enters “done”. Write the program to store the
# numbers the user enters in a list and use the max() and min() functions to
# compute the maximum and minimum numbers after the loop completes

listarray = []

while True:
    inp = input('Enter a number:\n')
    if inp == 'done':
        break
    try:
        float(inp)
    except:
        print('That is not a number. Try again.')
        continue
    listarray.append(inp)

print(listarray)
print('Min is: ', min(listarray))
print('Max is: ', max(listarray))
