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


class listener(StreamListener):
    final_dict = {}
    def on_data(self, data):
        try:
            user_info = {}
            #print(data) #prints the json format 
            tweet = data.split(',"text":"')
            tweet_for_link = tweet[0]
             
            tweet_link = tweet_for_link.split(',')[1][5:]
            tweet_for_text = tweet[1].split('","source":' )
             
            tweet_for_screen_name = tweet_for_text[1].split('"screen_name":"')[1]
            
            screen_name = tweet_for_screen_name.split('","location":')[0]
            user_info['Text'] = tweet_for_text[0]
            user_info['Screen name'] = screen_name 
            self.final_dict[tweet_link] = user_info 
            
            print(self.final_dict)
            #function()
            #savefile = open('twitDB.txt','a')
            #savefile.write(user_info) #or data and remove the three liness
            #savefile.write('\n')
            #savefile.close() 
            return True
        except BaseException:
            print('failed on data')
            time.sleep(5) 
    def on_error(self, status):
        print(status)
        
    def function(self):
        print("CALLED")
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["pilit"])


    


