from __future__ import print_function
import tweepy   
import json    
from pymongo import MongoClient 
import datetime 
MONGO_HOST = "mongodb://192.168.43.89:27017"  
CONSUMER_KEY = "p8HS37I0Lnt715jlH0XPk5bq1"          
CONSUMER_SECRET = "gGNzJzBWYXlM4iu7X8WVlMrZIphYrCkIs9ElP01a7xsZPTKsW8"  
ACCESS_TOKEN = "1270862959527378944-BZc1fFOrsE2gN1ObzmfLXwFs7r2jGV"  
ACCESS_TOKEN_SECRET = "MsHGGI24p50K8KfhHUxOKRNr8UThTNWWQlgDuTt6gzsp4" 
class StreamListener(tweepy.StreamListener):    
        def on_connect(self):           
                print("You are now connected to the streaming API.")
        def on_error(self, status_code):  
                print("An Error has occured: " + repr(status_code))
                return False
        def on_data(self, data):   
                try:
                        client = MongoClient(MONGO_HOST)   
                        db = client.twitterdb    
                        datajson = json.loads(data)  
                        tweet_id = datajson["id_str"]
                        username = datajson["user"]["screen_name"]
                        text = datajson["text"]
                        hashtags = datajson["entities"]["hashtags"]
                        lokasi = datajson["place"]["name"]
                        dt = datajson["created_at"]
                        created_at = datetime.datetime.strptime(dt, "%a %b %d %H:%M:%S +0000 %Y")
                        tweet = {"id" : tweet_id, "username" : username, "cuitan" : text, "hashtags" : hashtags, "lokasi" : lokasi, "waktu" : created_at}
                        print("Tweet collected...") 
                        db.twitter.insert_one(tweet)  
                except Exception as e:
                        print(e)
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)   #autentikasi ke api twitter deengan konsumer key dan consumer secret
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)        #set acces token
listener = StreamListener(api=tweepy.API(wait_on_rate_limit=True))  #gunakan listener tweet
streamer = tweepy.Stream(auth=auth, listener=listener)  #gunakan streamer
streamer.filter(locations=[ 94.77, -11.21, 141.02, 6.27 ])
