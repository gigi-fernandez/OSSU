# Find all unique words in a file

romeo = open('romeo.txt')

def IsWordInTable(word, table):
    result = True
    for v in table:
        if v != word: 
            continue
        else: result = False
    return result

dictionary = []
for line in romeo:
    line = line.split()
    for word in line:
        print('Debug: ', word)
        if IsWordInTable(word, dictionary) == False: continue
        else: dictionary.append(word)
    
dictionary.sort()
print(dictionary)
