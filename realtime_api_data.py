import time 
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey ='C3X4xTxjF4ELlu9DIY533n6Sh' 
csecret ='A3L2ljSILNN9xa4r2ibTlp4Y1dEKOb446mJDKbAWNB830v0GgI'
atoken ='798020067652988929-iHbp6HOloI8dhF2m03FjC0O7J2UomRX'
asecret ='VFXqXCc5XkQyD1VTgxABCEyVZfw5poEDYKEUFbK4Xxn2U'

class listener(StreamListener):
    def on_data(self, data):
        try:
            #print(data) #prints the json format 
            tweet = data.split(',"text":"')[1].split('","source')[0]
            print(tweet)
            savethis = str(time.time())+'::'+ tweet
            
            savefile = open('twitDB.csv','a')
            savefile.write(data) #or data and remove the three lines
            savefile.write('\n')
            savefile.close() 
            return True
        except BaseException:
            print('failed on data')
            time.sleep(5) 
    def on_error(self, status):
        print(status)
        
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["USA"])
