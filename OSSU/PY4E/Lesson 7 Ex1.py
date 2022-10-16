
def Count(word, letter):
    count = 0
    for l in word:
        if l == letter:
            count = count + 1
    print(count)

inpW = input('Enter a string:\n')
inpL = input('Enter the character you want to count in that string:\n')
Count(inpW, inpL)

