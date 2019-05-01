#reading a file and inserting data to the databade

import sqlite3

conn = sqlite3.connect('c:/Python/emaildb.sqlite') #open db file , create if not exists
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS counts')  #drop table if table already exists

cur.execute('CREATE TABLE counts (count INTEGER, email TEXT)') # create table with fields counts and email

fname= input('Enter file name: ')

if(len(fname)<1):
    fname='c:/Python/mbox-short.txt'
#reading emails from given file
file_handle = open(fname)
for line in file_handle:
    if(not line.startswith('From:')): continue
    words = line.split()
    temail = words[1]
    cur.execute('SELECT count FROM counts WHERE email=?',(temail,)) #check if email already exixts in the table
    row = cur.fetchone()
    if row is None:
        cur.execute('''
        INSERT INTO counts(count,email) VALUES(1,?)''',(temail,)) #if email not exixts insert email with count 1
    else:
        cur.execute('''UPDATE counts SET count = count + 1 WHERE email = ?''',(temail,)) #if email exixts then increase the count by 1
    conn.commit()   #commit all the changes made to the database

sqlstr = 'SELECT count, email FROM counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(row[0],row[1])

cur.close()
