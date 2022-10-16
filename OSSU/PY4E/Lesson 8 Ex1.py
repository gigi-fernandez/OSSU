file = open('mbox-short.txt')
for line in file:
    print(line.upper().rstrip())