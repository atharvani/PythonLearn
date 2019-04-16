#learning dictionaries
def file_open(fileName):
    try:
        file_handle = open(fileName)
        return file_handle
    except:
        print('file not found!')
        quit()

file_handle = file_open('c:/Python/words.txt')
dict1 = dict()
for line in file_handle:
    words = line.split();
    for word in words:
        if word in dict1:
            continue
        dict1[word] = 1

#print(dict1)

def find_word(word):
    x = dict1.get(word,0)
    if x !=0:
        print('the word is present',word)
    else:
        print('word is not present', word)

find_word('with')
find_word('shital')
find_word('are')
find_word('after')


#writing program for number of times the word appears in the find_letter

file_handle = file_open('C:/Python/mbox-short.txt')

dict1 = dict()
for line in file_handle:
    line = line.strip()
    words = line.split()
    if len(words) > 0 and words[0] == 'From':

        if len(words) <= 2:
            continue
        else:
            word = words[2]
            if word in dict1:
                dict1[word]  += 1
            else:
                dict1[word] = 1

print(dict1)

# count number of unique emails

file_handle = file_open('C:/Python/mbox-short.txt')

dict2 = dict()
for line in file_handle:
    line = line.strip()
    words = line.split()
    if len(words) > 0 and words[0] == 'From':
        if len(words) <= 1:
            continue
        else:
            word = words[1]

            if word in dict2:   # can use dict2.get(word,0) gives value of word, and 0 if word is not in dict2
                dict2[word]  += 1
            else:
                dict2[word] = 1

print(dict2)
# find maximum number of emails by the sender

maxnum = None
mSender = None

for email, num in dict2.items():
    if maxnum is None or num > maxnum:
        maxnum = num
        mSender = email

print('maximum number of emails sent by:', mSender,'is',maxnum)


#find the unique domains n cout of emails from each

maxnum = None
mDomain = None
dict3 = dict()

for email, num in dict2.items():
    domain_pos = email.find('@')
    if domain_pos > 0:
        domain = email[domain_pos +1 :]
        if domain in dict3:
            dict3[domain] = dict3[domain] + num
        else:
            dict3[domain] = num

print(dict3)
