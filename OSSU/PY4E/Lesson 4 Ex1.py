import random

avg = 0

for i in range(1000):
    x = random.randint(0,1000)
    print(x)
    avg = avg + x
print('random average is '+ str(avg/10))