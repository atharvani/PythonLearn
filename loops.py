# using indefinite loop

total = 0.0
count = 0
avg = 0.0
line = -1
# program to find sum and average
while(True):
    line = input('Enter the number or done : ')
    if(line != 'done'):
        try:
            fline = float(line)
        except:
            print('Error, Please enter the number.')

            continue
    else:
        break
    count = count + 1
    total = total + fline

if(count == 0):
    print("no numbers are entered.")
else:
    print("count:", count, "the sum:", total,"average:",total/count )


#program to find minimum and maximum of the numbers
maxnum = None
minnum = None
while(True):
    line = input('Enter number or done: ')
    if(line == 'done'):
        break
    try:
        iline = int(line)
    except:
        print('Error, Please enter number.')
        continue
    print(maxnum,minnum)
    if(maxnum is None):
        maxnum = iline
    elif(maxnum < iline):
        maxnum = iline
    if(minnum is None):
        minnum = iline
    elif(minnum > iline):
        minnum = iline

print('Maximum: ' , maxnum, "Minimum: ", minnum)
