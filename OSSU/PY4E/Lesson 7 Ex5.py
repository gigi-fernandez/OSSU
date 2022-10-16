# Use find and string slicing to extract the portion of the string after 
# the colon character and then use the float function to convert the 
# extracted string into a floating point number.

full_string = 'X-DSPAM-Confidence:0.8475'

pos = full_string.find(':')
score = full_string[pos+1:]
new_score = score.replace('0.', 'Score is ')
print(new_score)
