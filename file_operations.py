#to execute the file operations

try:
    ffile = open('c:/Python/mbox-short.txt')
except:
    print('Error,file not found.')
    quit()

for line in ffile:
    line = line.rstrip()
#    print(line.upper())

#extract data from find_letter
count = 0
sum = 0
fname = input('Enter the file name : ')
try:
    ffile = open(fname)
except:
    print('Error, File not found')
    quit()

for line in ffile:
    fpos = line.find('X-DSPAM-Confidence:')
    if fpos != -1:
        fpos2 = line.find(':')
        try:
            fnum = float(line[fpos2+1:])
            count = count + 1
            sum = sum + fnum
        except:
            continue

print('the average SPAM confidence is : ', sum/count)


#easter egg hunt
count = 0
fname = input('Enter the file name: ')
if fname.find('na na boo boo') != -1:
    print('NA NA BOO BOO TO YOU - You have been punked!')
    quit()
try:
    ffile = open(fname)
except:
    print('File can not be opened:', fname)
    quit()

for line in ffile:
    if line.startswith('Subject:'):
        count = count + 1

print('there were', count, 'subject lines in', fname)
