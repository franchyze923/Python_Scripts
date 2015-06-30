from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time

ckey = 'tqNuXU78PvduTFFk6cvEWUe4B'
csecret = 'HUwxRoiZt7aYf3EKlQz0WQ6mHDEypXccIpOJ31v8V9rBUJQCNd'
atoken = '337431098-81Cnaondhm016I6NZtkWCP22yCNWKejIWJkOFORT'
asecret = '0RD7daEhbxIy0GM6UZpfDItOpVGjkIqrAZnpwQPu9u7nN'

class listener(StreamListener):

    def on_data(self, raw_data):
        try:

            #print (raw_data)

            tweet = raw_data.split(',"text":"')[1] .split('","source')[0]
            #print(tweet)

            username = raw_data.split(',"screen_name":"')[1] .split('","location')[0]
            #print(username)

            location = raw_data.split(',"location":"')[1] .split('","url')[0]
            #print(location)

            saveThis = 'Time - '+ str(time.time()) + '\n'+ 'Username - ' + username + '\n'+ 'Tweet - '+ "'" +tweet +"'" + '\n' + 'Location - ' + location + '\n'

            print(saveThis)

            savetweet = open('twitDB89.csv', 'a')
            savetweet.write(saveThis)
            savetweet.write('\n')
            savetweet.close()
            return True

        except BaseException as e:
            print('failed ondata',str(e))
            time.sleep(5)

    def on_error(self, status_code):
        print (status_code)

auth = OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)

twitterStream = Stream(auth,listener())
twitterStream.filter(track=["beer"])

