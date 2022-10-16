# Write a program that categorizes each mail message by
# which day of the week the commit was done. To do this look for lines
# that start with “From”, then look for the third word and keep a running
# count of each of the days of the week. At the end of the program print
# out the contents of your dictionary (order does not matter).

d = dict()
mbox = open('mbox.txt')

for line in mbox:
    line = line.split()
    if len(line) < 3 or line[0] != 'From': continue
    date = line[2]
    if date not in d:
        d[date] = 1
    else:
        d[date] = d.get(date, 0) + 1


print(d)