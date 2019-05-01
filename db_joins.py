import sqlite3
import xml.etree.ElementTree as ET

#create trackdb database
conn = sqlite3.connect('c:/Python/tracksdb.sqlite')
cur = conn.cursor()

#create tables


cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist(
Artist_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT  UNIQUE,
name TEXT UNIQUE
);

CREATE TABLE Album(
Album_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
title TEXT UNIQUE,
Artist_id INTEGER
);

CREATE TABLE Track(
Track_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
title TEXT UNIQUE,
Album_id INTEGER,
len INTEGER,
rating INTEGER,
count INTEGER
);
''')

fname = input('Enter file name: ')
if(len(fname)<1):
    fname = 'c:/Python/Library.xml'

def lookup(d, key):
    found = False

    for child in d:
        if found: return child.text
        if(child.tag == 'key' and child.text == key):
            found = True
    return None

stuff = ET.parse(fname)
alltracks = stuff.findall('dict/dict/dict')

print('Dict count: ', len(alltracks))

for entry in alltracks:
    if(lookup(entry,'Track ID') is None): continue

    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')

    if name is None or artist is None or album is None: continue

    print(name, artist, album, count, rating, length)

    cur.execute('''INSERT OR IGNORE INTO Artist(name) VALUES(?) ''', (artist,))
    cur.execute('''SELECT Artist_id FROM Artist WHERE name = ?''', (artist,))
    Artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album(title,Artist_id) VALUES(?,?)''', (album,Artist_id))
    cur.execute('''SELECT Album_id FROM Album WHERE title = ?''', (album,))
    Album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track(title, Album_id,len, rating, count) VALUES(?,?,?,?,?)''',(name, Album_id, length, rating, count))
    conn.commit()
