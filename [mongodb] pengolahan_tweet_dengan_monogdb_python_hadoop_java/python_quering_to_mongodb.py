#untuk mencari user tweet terbanyak
import pymongo
client = pymongo.MongoClient("mongodb://192.168.43.89:27017")
database = client.twitterdb
colle = database.twitter
jum = [{"$group":{"_id":"$username", "Jumlah Cuitan":{"$sum":1}}}, {"$sort" : {"Jumlah Cuitan":-1}}]
jum_tweet = list(colle.aggregate(jum))
jtb = jum_tweet[1]
print("User dengan tweet terbanyak adalah", jtb["_id"], "dengan jumlah tweet", jtb["Jumlah Cuitan"])


#untuk mendapatkan user dan cuitan
import pymongo
client = pymongo.MongoClient("mongodb://192.168.43.89:27017")
database = client.twitterdb
colle = database.twitter
data = [{"$group":{"_id":"$username", "Cuitan":{"$addToSet":"$cuitan"}}}, {"$sort" : {"_id":1}}]
data_tweet = list(colle.aggregate(data))
print(data_tweet)


#mendapatkan word.txt dari cuitan
import pymongo
import pprint
client = pymongo.MongoClient("mongodb://192.168.43.89:27017")
database = client.twitterdb
colle = database.twitter
f = open("word.txt", "w")
word_tweet = list(colle.find())
for word in word_tweet:
        x = word["cuitan"]+" "
        f.write(x)
