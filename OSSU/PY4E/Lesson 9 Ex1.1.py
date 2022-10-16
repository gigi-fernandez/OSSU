# Write a program that reads the words in words.txt and stores them as
# keys in a dictionary. It doesn’t matter what the values are. Then you
# can use the in operator as a fast way to check whether a string is in the dictionary.

words = open('words.txt')

def IsWordInDic(word, table):
    result = True
    for v in table:
        if v != word: 
            continue
        else: result = False
    return result

dictionary = {}
for line in words:
    line = line.split()
    for word in line:
        print('Debug: ', word)
        if IsWordInDic(word, dictionary) == False: continue
        else: dictionary[word] = 'something'

while True:
    inp = input('Enter a word to check if it\'s in the dictionary:\n')
    if inp in dictionary: print('It\'s in the dictionary!')
    else: print('It\'s not in the dictionary')
    
