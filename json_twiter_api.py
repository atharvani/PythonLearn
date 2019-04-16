import urllib.request, urllib.error,urllib.parse
import ssl
import twurl

TWITTER_URL = 'https://api.twitter.com/1.1/statuses/user_timeline.json'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    print('')
    acct = input('enter user account: ')
    if(len(acct))<1:
        break
    url = twurl.augment(TWITTER_URL,{'screen_name':acct, 'count':'2'})
    print('retrieving' ,url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    print(data[:250])
    js = json.loads(data)
    print(json.dumps(js, indent=2))
    headers = dict(connection.getheaders())
    print('Remaining',headers['x-rate-limit-remaining'])

    for u in js['users']:
        print(u['screen_name'])
        if 'status' not in u:
            print('no status found')
            continue
        s = u['status']['text']
        print(' ', s[:50])
