# Write a program which repeatedly reads numbers until the
# user enters “done”. Once “done” is entered, print out the total, count,
# and average of the numbers. If the user enters anything other than a
# number, detect their mistake using try and except and print an error
# message and skip to the next number.

sigma = 0
count = 0
minimum = None
maximum = None

while True:
    inp = input('Enter a number:\n')
    if inp == 'done':
        if count == 0:
            print('You must input at least one number.')
            continue
        else:
            break
    try:
        inp = float(inp)
    except:
        print('Invalid input.')
        continue

    sigma = sigma + inp
    count = count + 1
    if minimum == None or minimum > inp:
        minimum = inp
    if maximum == None or maximum < inp:
        maximum = inp

print('Sum is ' + str(sigma) + '\nNumber of elements is ' + str(count) + '\nAverage is ' + str(sigma/count))
print('Maximum: ' + str(maximum) + '\nMinimum: ' + str(minimum))