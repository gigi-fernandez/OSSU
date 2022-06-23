try:
    int(input('Please think of a number between 0 and 100! '))
except:
    print('Wrong type of input.')
    quit()
low = 0
high = 100
guessNumber = 0
while True:
    guess = (high + low)/2
    print('Is your secret number',guess,'?')
    guessCompass = input('Enter \'h\' to indicate the guess is too high. Enter \'l\' to indicate the guess is too low. Enter \'c\' to indicate if the guess is correct: ')
    guessNumber += 1
    if (guessCompass == 'h'):
        high = guess
    elif (guessCompass == 'l'):
        low = guess
    elif (guessCompass == 'c'):
        break
    else:
        print('Incorrect input, try again')
print('Took',guessNumber,'guesses')
print('Game over. Your secret number is', guess)