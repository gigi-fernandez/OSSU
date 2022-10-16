# Write a function called chop that takes a list and modifies it, 
# removing the first and last elements, and returns None. Then write
# a function called middle that takes a list and returns a new list that
# contains all but the first and last elements.

def chop(t):
    try:
        type(t) == list
    except:
        print('Error, not a table.')
        exit()
    del t[0]
    del t[len(t)-1]

random_list = ['one', 'two', 'three', 'four', 5]
chop(random_list)
print(random_list)
print(chop(random_list))

# Working fine