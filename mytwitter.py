from twython import Twython

APP_KEY = 'FILL IN'
APP_SECRET = 'FILL IN'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print twitter.search(q='python')
