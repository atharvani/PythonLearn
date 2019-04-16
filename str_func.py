#execise on string functions

#read a string backwords using while loop

word1 = input('Enter a word: ')
word_len = len(word1)
while(word_len > 0):
    letter = word1[word_len - 1]
    print(letter, word_len)
    word_len = word_len -1

#slice function
fruit = word1
print('fruit[:] :',fruit[:] )
print('fruit[:3] :',fruit[:3] )
print('fruit[4:] :',fruit[4:] ) # can give you empty string if index is out of range
print('fruit[2:4] :',fruit[2:4] )


#function to find number of occurances of letter in the given string

def find_letter(word1, letter1):
    count = 0
    for letter in word1:
        if(letter == letter1):
            count = count + 1
    return count


print('Count of l in Shital: ', find_letter('Shital','l'))
print('Count of s in atharv: ', find_letter('atharv','s'))
print('Count of a in ahamdnagar: ', find_letter('ahamdnagar','a'))


#finding letters using string method - Count
str1 = 'Shital'
str2 = 'atharv'
str3 = 'ahamadnagar'
print('Count of l in Shital: ', str1.count('l'))
print('Count of s in atharv: ', str2.count('s'))
print('Count of a in ahamadnagar: ', str3.count('a',4,10))


#using find and slice
str1 =  'X-DSPAM-Confidence:0.8475'
str2_index = str1.find(':')
str2 = str1[str2_index +1 :]
print(str2)
try:
    num = float(str2)
    print('the number is :', num)
except:
    print('not a number')


#using different string functions

str1 = 'shital'
str2 = 'KAPIL'
str3 = 'atharv'
str4 = 'anika'
str5 = 'sanap'
str6 = 'shital.sanap'

print('str capitalize :',str1, str1.capitalize())
print('casefold:',str2, str2.casefold())
print('center', str3.center(12,'-'))
print('rfind a', str4, str4.rfind('a'))
print('replace', str6,str6.replace('sanap','ghuge'))
print('split', str6, str6.split('.', maxsplit=3))
