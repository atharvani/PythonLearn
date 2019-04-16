#program to find most common word in the file
fname = input('Enter file: ')
if(len(fname) < 1):
    fname = 'c:/Python/clown.txt'
fhand = open(fname)

di = dict()

for lines in fhand:
    lines = lines.rstrip()
    words = lines.split()
    for word1 in words:
        di[word1] = di.get(word1,0) + 1

    print(di)

x = sorted(di.items())
print(x[:5])

lst1 = list()

for k,v in di.items():
    newt = (v,k)
    lst1.append(newt)

print('list: ', sorted(lst1, reverse=True))

for v,k in lst1[:5]:
    print(k,v)
