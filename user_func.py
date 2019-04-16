# in built functions functions

import random

for i in range(10):
    x = random.random()
    print(x)

print(random.randint(12, 15))
print(random.randint(2, 8))

t = [23, 45, 56]
print(random.choice(t))

#user defined functions
# repeat_lyrics()              NameError: name 'repeat_lyrics' is not defined

def repeat_lyrics():           # sequence of definition of function doesnt matter
    print_lyrics()
    print_lyrics()

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')

repeat_lyrics()


# function to compute pay

def computePay(hours, rate):

    if(hours > 40):
        ohours = hours - 40
        regPay = 40 * rate
        overtime = ohours * rate * 1.5
    else:
        overtime = 0
        regPay = hours * rate
    pay = regPay + overtime
    return pay


print(computePay(20, 10))
print(computePay(45, 10))

# function to calculate grades
def computegrades(score):
    if(score >1.0):
        print('Bad score')
    elif(score>= 0.9):
        print('A')
    elif(score >= 0.8):
        print('B')
    elif(score >= 0.7):
        print('C')
    elif(score >= 0.6):
        print('D')
    elif(score < 0.6):
        print('F')
    else:
        print('Bad score')

computegrades(1.0)
computegrades(10.0)
computegrades(0.56)
computegrades(0.7)
computegrades(0.8)
