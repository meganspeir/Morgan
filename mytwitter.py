from twython import Twython
import json

APP_KEY = 'HIDDEN'
APP_SECRET = 'HIDDEN'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)

# print twitter.search(q='python')
search = twitter.search(q='#oakmtg :(', result_type='mixed')
for entry in search['statuses']:
    print entry

