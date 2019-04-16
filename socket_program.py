#connecting to the file at remote computer

import socket
import urllib.request


def open_sock(user_url):
    try:
        mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #mysocket.connect(('data.pr4e.org', 80))
        urls = user_url.split('/')
        #print(urls[0],urls[2],urls[3])
        mysocket.connect((urls[2],80))
        #cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
        cmd1 = 'GET '+ user_url + ' HTTP/1.0\r\n\r\n'
        cmd = cmd1.encode()
        mysocket.send(cmd)
        while True:
            data = mysocket.recv(5120)
            if (len(data) < 1):
                break
            else:
                #print(data.decode())
                return data.decode()
        mysocket.close()
    except:
        print('page not found.')
        quit()

# opening a socket gives you all the data in the file including header
user_url = input('enter the URL: ')
if(user_url == ''):
    user_url = 'http://data.pr4e.org/romeo.txt'
data = open_sock(user_url)
print(data)

#count the number of characters
user_url = input('enter the URL: ')
if(user_url == ''):
    user_url = 'http://data.pr4e.org/romeo.txt'
data = open_sock(user_url)
print(len(data))
print(data[:3000])


# urllib gives you only data in the file
user_url1 = input('Enter url: ')
if(user_url1 == ''):
    user_url1 = 'http://data.pr4e.org/romeo.txt'

fhand = urllib.request.urlopen(user_url1)
char_len = 0
print_flag = 0
for line in fhand:
    line = line.decode()
    char_len = char_len + len(line)
    if (char_len < 3000):
        if(print_flag == 0):
            print(line)
        continue
    else:
        if(print_flag == 0):
            new_len = len(line) - (char_len-3000)
            line = line[:new_len]
            print(line)
            print_flag = 1

print('Total characters in the page:',char_len)


# finding html tag p

import urllib.request, urllib.parse, urllib.error
import re
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

user_url2 = input('Enter url :')
if(user_url2 == ''):
    user_url2 = 'http://data.pr4e.org/romeo.txt'
count = 0
fhand = urllib.request.urlopen(user_url2).read()
paras = re.findall(b'<p',fhand)
for para in paras:
    count= count + 1

print('number of paras in file: ',count)


# print except headers using socket
user_url3 = input('Enter url :')
if(user_url3 == ''):
    user_url3 = 'http://data.pr4e.org/romeo.txt'
data = open_sock(user_url3)
pos = data.find('\r\n\r\n')
print(data[pos+4:])


#write a program using BeautifulSoup3 to find links in the given url

import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup
import ssl

#to ignore ssl errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url4 = input('Enter url: ')
if(url4 == ''):
    url4 = 'http://data.pr4e.org/romeo.txt'

fhand = urllib.request.urlopen(url4,context=ctx).read()

bsoup = BeautifulSoup(fhand,'html.parser')

tags = bsoup('a')

for tag in tags:
    print(tag.get('href',None))
