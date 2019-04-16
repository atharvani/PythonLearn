#conditional statements

#calculate pay
hours = input('Enter hours of work: ')
try :
    fhrs = float(hours)
except :
    print('Error, Please enter numeric hours')
    quit()
rate = input('Enter the rate per hour: ')
try :
    frate = float(rate)
except:
    print('Error, Please enter numeric rate')
    quit()
#for 40 hours, pay is as per the rate, for next hours pay is 1.5 times the rate
if( fhrs > 40):
    pay = (40 * frate) + ((fhrs - 40) * frate * 1.5)
else:
    pay = fhrs * frate

print('Your pay is:', '$', pay)


#program to promt a score

score = input('Please enter score between 0.0 and 1.0 : ')
try:
    fscore = float(score)
except:
    print('Error, Please enter numeric score')
    quit()

if(fscore< 0.0 or fscore > 1.0):
    print('Bad score')
elif(fscore >= 0.9):
    print('A')
elif(fscore >= 0.8):
    print('B')
elif(fscore >= 0.7):
    print('C')
elif(fscore >= 0.6):
    print('D')
else:
    print('F')
