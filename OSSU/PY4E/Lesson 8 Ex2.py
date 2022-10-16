# Write a program to prompt for a file name, and then read
# through the file and look for lines of the form 'X-DSPAM-Confidence: 0.847'

spam_confidence = 0
spam_count = 0

inp = input('Enter the name of the file:\n')

try:
    file = open(inp)
except:
    if inp == 'na na boo boo':
        print('NA NA BOO BOO TO YOU!')
    else:
        print('File could not be opened.')
    exit()

for line in file:
    line_pos = line.find('X-DSPAM-Confidence: ')
    if line_pos == -1:
        continue
    new_line = line[line_pos:]
    pos = new_line.strip().find(':') + 1
    spam_score = line[pos:]
    print(float(spam_score))
    spam_confidence = spam_confidence + float(spam_score)
    spam_count = spam_count + 1
print(spam_confidence/spam_count)
