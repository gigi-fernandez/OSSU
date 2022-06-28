# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "C:/Users/Portatil/Desktop/Guille/OSSU/python scripts/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:
      if letter not in lettersGuessed:
        return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    tempList = []
    for letter in secretWord:   # Sets up the initial word '_ _ _ _...'
      tempList.append('_ ')
    
    secretList = enumerate(secretWord, 0)
    for pair in secretList:
      index = pair[0]
      letter = pair[1]
      if letter in lettersGuessed:
        tempList[index] = letter
    return ''.join(tempList)


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    allLetters = 'abcdefghijklmnopqrstuvwxyz'
    abcList = []
    for l in allLetters:
      abcList.append(l)
    for letter in lettersGuessed:
      if letter in abcList:
        abcList.pop(abcList.index(letter))
    return ''.join(abcList)

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to the game Hangman!\nI am thinking of a word that is",len(secretWord),"letters long")
    num_guesses = 8
    lettersGuessed = []
    lettersEntered = []
    while True:
      availableLetters = getAvailableLetters(lettersEntered)
      print("-----------")
      print("You have",num_guesses,"guesses left")
      print("Available Letters:",availableLetters)

      while True:
        try:
          guess = input('Please guess a letter: ').lower()[0] # takes only the first letter
        except:
          print('Please enter a valid letter')
          continue
        break

      if guess in lettersEntered:
        print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
        continue

      lettersEntered.append(guess)
      if guess in getGuessedWord(secretWord, [guess]):
        lettersGuessed.append(guess)
        guessSF = getGuessedWord(secretWord, lettersGuessed)    # Guess So Far
        availableLetters = getAvailableLetters(lettersEntered)
        print("Good guess:", guessSF)
        if isWordGuessed(secretWord, lettersGuessed):
          print("-----------")
          print("Congratulations, you won!")
          break

      else:
        num_guesses -= 1
        print("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed))
        if num_guesses <= 0:
          print("-----------")
          print("Sorry, you ran out of guesses. The word was " + secretWord)
          break

print(hangman(chooseWord(loadWords())))


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
