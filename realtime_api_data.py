import time 
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey ='C3X4xTxjF4ELlu9DIY533n6Sh' 
csecret ='A3L2ljSILNN9xa4r2ibTlp4Y1dEKOb446mJDKbAWNB830v0GgI'
atoken ='798020067652988929-iHbp6HOloI8dhF2m03FjC0O7J2UomRX'
asecret ='VFXqXCc5XkQyD1VTgxABCEyVZfw5poEDYKEUFbK4Xxn2U'

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

user_info = {}

class listener(StreamListener):
    
    def on_data(self, data):
        try:
            #print(data) #prints the json format 
            tweet = data.split(',"text":"')
            tweet_for_link = tweet[0]
            print(tweet_for_link) 
            print("/n")
            
            tweet_link = tweet_for_link.split(',')[1][5:]
            print("Tweet Link: " + tweet_link)
            
            tweet_for_text = tweet[1].split('","source":' )
            print("Text: "+ tweet_for_text[0]) 
            
            user_info['Tweet Link'] = tweet_link
            user_info['Text'] = tweet_for_text[0]
            
            #print(user_info)
            '''
            savefile = opesn('twitDB.csv','a')
            savefile.write(data) #or data and remove the three lines
            savefile.write('/n')
            savefile.close() '''
            return True
        except BaseException:
            print('failed on data')
            time.sleep(5) 
    def on_error(self, status):
        print(status)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["pilit"])

