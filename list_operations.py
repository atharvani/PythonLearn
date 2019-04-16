#using list functions

#write a function to remove first and last elemnet of list\

def chop(t):

    del t[0]            #deletes the 1st element from list n length gets shorter
    list_len = len(t)
    del t[list_len-1]

def middle(t):
    list_len = len(t)
    list_new = t[1:list_len-1]
    return list_new


list1 = [3,6,9,12,15,18,21]
list2 = [2,4,6,8,10,12,14]

print('list1 before chop function:', list1)
chop(list1)
print('list1 after chop function : ', list1)
list_new1 = middle(list2)
print('after function middle: ', list_new1)
print('list2 after middle function : ', list2)

#debugging the file reading

file_handle = open('c:/Python/mbox-short.txt')

for line in file_handle:
    words = line.split()
    if len(words) != 0 and words[0] == 'From' :
        if len(words) > 2:
            print('day is: ',words[2])

#finding unique words in given find
file_handle = open('c:/Python/romeo.txt')
unique_list = []
for line in file_handle:
    words = line.split()
    if len(words) > 0:
        for word_ele in words:
            if word_ele in unique_list:
                continue
            unique_list.append(word_ele)
unique_list.sort()
print('the list of unique words: ', unique_list)

#Number of emails senders address

file_handle = open('c:/Python/mbox-short.txt')
count_senders = 0

for lines in file_handle:
    words = lines.split()
    if(len(words) > 0 and words[0] == 'From'):
        count_senders = count_senders + 1
        if len(words) > 1 :
            print('sender: ', words[1])

print('number of senders: ', count_senders)

#find max n min from the user input numbers
list1 = []
while(True):
    number1 = input('Enter the number or done to finish: ')
    if number1 == 'done':
        break
    try:
        number1 = float(number1)
        list1.append(number1)
    except Exception as e:
        print('Please enter number')
        continue

print('the list of numbers are: ', list1)
print('maximun number in the list is: ', max(list1))
print('minimum of the list is: ', min(list1))
