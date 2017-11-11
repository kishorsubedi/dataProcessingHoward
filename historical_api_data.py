import tweepy 

ckey ='C3X4xTxjF4ELlu9DIY533n6Sh' 
csecret ='A3L2ljSILNN9xa4r2ibTlp4Y1dEKOb446mJDKbAWNB830v0GgI'
atoken ='798020067652988929-iHbp6HOloI8dhF2m03FjC0O7J2UomRX'
asecret ='VFXqXCc5XkQyD1VTgxABCEyVZfw5poEDYKEUFbK4Xxn2U'

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret) #Token made

api = tweepy.API(auth)
public_tweets = api.search('Kishor')
for tweet in public_tweets:
    print(tweet.text)
