#Write a program to prompt for a score between 0.0 and 1.0. 
#If the score is out of range, print an error message. If the score is
#between 0.0 and 1.0, print a grade using the following table:
#Score      Grade
# >= 0.9    A
# >= 0.8    B
# >= 0.7    C
# >= 0.6    D
# < 0.6     F

def computescore(score):
    if score <= 1 and score >= 0:    
        if score >= 0.9:
            print('Grade is A')
        elif score >= 0.8:
            print('Grade is B')
        elif score >= 0.7:
            print('Grade is C')
        elif score >= 0.6:
            print('Grade is D')
        elif score < 0.6:
            print('Grade is F')
    else:
        print('Invalid input. Please enter a number between 0 and 1.')

score_input = input('Input your grade (between 0 and 1):\n')
try:
    score_f = float(score_input)
    computescore(score_f)
except:
    print('Invalid input. Please enter a number.')