def isPalyndrome(sentence):
    if len(sentence) <= 1:
        return True
    else:
        if sentence[0] == sentence[-1]:
            return isPalyndrome(sentence[1:-1])
        else:
            return False

print(isPalyndrome('amijima'))