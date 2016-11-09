import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener 
import json
import time
import re
import psycopg2
import datetime

#emoji support
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')
'''
ckey = "ESH4cnWcKgKVHFPcnIjpAUvbe"
csecret = "aTOvrDtmqn2I15RZKEANNNhkPsXryAlECDdmbkAp2L268Dw8N8" 
atoken = "3060784180-REBbkm5XaSZ1XBwpYDL6d6HS12CdXJ7Kz1JEMaR"
asecret = "CDtvPLmbIheR6GXgd5aIKuD0Jl0vJDpRdSIZqHtwpEcWs"
'''
ckey = "ddG8wj7QOLTa2FC2OcfThVv2v"
csecret = "u4ySl4h8CppB43eCYX37OQOUN3uvJ2qfBkh1x8xTOgqQfmUE7I" 
atoken = "3060784180-6bT5hk58xwebXAAhclm8IgnWZSBo2mvCX7I7oGE"
asecret = "62pOOLxYOgCx0Aq8AEJf76yrMUtPJ4oYiTFNA4YCPvmXJ"
try:
    conn = psycopg2.connect("dbname='team7' user='team7' host='/tmp/' password=''")
except:
    print "database connection error"

curr = conn.cursor()

#fileOut = open("/Users/charliebuckets/Desktop/projects/smScraper/output.txt", "a")

class listener(StreamListener):
    def on_data(self, data):
        
        try:
            # not sure how the whole unicode 'u' thing is going to work.  This is a potential fix 
            # if we run into problems with it
            #  ||
            # \  /
            #  \/
            #all_data = json.dumps(json.loads(data))
            
            all_data = json.loads(data)
            
            text = all_data["text"]
            if not type(text) is unicode:
                print "bad tweet   " + str(text)
            if len(text) > 161:
                print "text too long"

            username = all_data["user"]["screen_name"]
            if not type(username) is unicode:
                print "bad username   " + str(username)
            if len(username) > 50:
                print "username too long"

            timeStampInMilliseconds = int(all_data["timestamp_ms"])
            if not type(timeStampInMilliseconds) is int:
                print str(type(timeStamp))
                print "bad timestamp   " + str(timeStampInMilliseconds)
            timeStamp = datetime.datetime.fromtimestamp(timeStampInMilliseconds/1000)

            userId = long(all_data["user"]["id"])
            if not type(userId) is long:
                print "bad userId   " + str(userId)

            location = all_data["user"]["location"]
            if location == None:
                location = "N/A"
            if len(location) > 100:
                print "location too long"
            if not type(location) is unicode and not type(location) is str:
                print "bad location   " + str(location)

            language = all_data["lang"]
            if not type(language) is unicode:
                print "bad language   " + str(language)
            if len(language) > 20: 
                print "language too long"

            created_at = all_data["created_at"]
            if not type(created_at) is unicode:
                print "bad created_at   " + str(created_at)
            if len(created_at) > 60: 
                print "created_at tool long"

            followers_count = int(all_data["user"]["followers_count"])
            if not type(followers_count) is int:
                print "bad followers_count   " + str(followers_count)

            tweet_id = long(all_data["id"])
            if not type(tweet_id) is long:
                print "bad tweet_id   " + str(tweet_id)

            favorite_count = int(all_data["favorite_count"])
            if not type(favorite_count) is int:
                print "bad favortie_count   " + str(favorite_count)

            retweet_count = int(all_data["retweet_count"])
            if not type(retweet_count) is int:
                print "bad retweet_count   " + str(retweet_count)

            favorited = int(all_data["favorited"])
            if not type(favorited) is int:
                print "bad favorited   " + str(favorited)

            verified = all_data["user"]["verified"]
            if not type(verified) is bool:
                print "bad verified   " + str(verified)

            friends_count = int(all_data["user"]["friends_count"])
            if not type(friends_count) is int:
                print "bad friends_count   " + str(friends_count)

            timeZone = all_data["user"]["time_zone"]
            if timeZone == None:
                timeZone = "N/A"
            if not type(timeZone) is str and not type(timeZone) is unicode:
                print str(type(timeZone))
                print "bad timeZone   " + str(timeZone)

            in_reply_to_status_id_str = all_data["in_reply_to_status_id_str"]
            if in_reply_to_status_id_str == None:
                in_reply_to_status_id_str = "N/A"

            if not type(in_reply_to_status_id_str) is unicode and not type(in_reply_to_status_id_str) is str:
                print str(type(in_reply_to_status_id_str))
                print "bad in_reply   " + str(in_reply_to_status_id_str)







            '''
            tweet = all_data["text"]            
            username = all_data["user"]["screen_name"]
            timeStamp = all_data["timestamp_ms"]
            #timeStamp = int(all_data["timestamp_ms"])/1000
            #date = datetime.datetime.fromtimestamp(timeStamp).strftime('%Y-%m-%d %H:%M:%:S')
            #hashTags = all_data["entities"]["hashtags"]
            userId = all_data["user"]["id"]
            location = all_data["user"]["location"]
            language = all_data["lang"]
            created_at = all_data["created_at"]
            #place = all_data["place"]
            followers_count = all_data["user"]["followers_count"]
            tweet_id = all_data["id"]
            favorite_count = all_data["favorite_count"] 
            retweet_count = all_data["retweet_count"] 
            
            favorited = all_data["favorited"]
            verified = all_data["user"]["verified"]
            friends_count = all_data["user"]["friends_count"]
            timeZone = all_data["user"]["time_zone"]
            in_reply_to_status_id_str = all_data["in_reply_to_status_id_str"]
            '''

            ''' 
            print tweet
            print username
            print timeStamp
            print userId
            print location
            print language
            print created_at
            #print place
            print str(followers_count)
            print tweet_id
            print favorite_count
            print str(retweet_count)
            print favorited
            print verified
            print friends_count
            print timeZone
            print in_reply_to_status_id_str
            '''
            #match = re.search(".?([Hh][Ii][Ll][Ll][Aa][Rr][Yy]).?|([Tt][Rr][Uu][Mm][Pp]).?|([Cc][Ll][Ii][Nn][Tt][Oo][Nn]).?|([Rr][Ee][Pp][Uu][Bb][Ll][Ii][Cc][Aa][Nn]).?|([Dd][Ee][Mm][Oo][Cc][Rr][Aa][Tt]).?|([Dd][Ee][Bb][Aa][Tt][Ee]).?", tweet)
            
            
            #if match:
                
                #print all_data
            #with open('debate_two_fetched_tweets.txt','a') as tf:
            #    tf.write(data)
           
            query = "INSERT INTO tweets(text,username,timeStamp,userId,location,language,created_at,followers_count,tweet_id,favorite_count,retweet_count,friends_count,timezone,in_reply_to_status_id_str,favorited,verified) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
            data = (text,username,timeStamp,userId,location,language,created_at,followers_count,tweet_id,favorite_count,retweet_count,friends_count,timeZone,in_reply_to_status_id_str,favorited,verified)   
            
            curr.execute(query,data)
            conn.commit()

            return True
        
        except Exception, e:
            conn.rollback()
            
    
    def on_error(self, status):
        print status
        return true
        
#    def on_exception(self, status):
#        print status

#try:
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)
while True:
    try:
        twitterStream = Stream(auth, listener())
        twitterStream.filter(locations=[-172.863636, 4.671721,  -28.019894, 71.943955], track=['Trump', 'Clinton', 'Donald', 'Hillary', 'Debate', 'Republican', 'Democrat', 'Vote'] )
    except Exception:
        pass

''' SAMPLE TWITTER JSON OBJECT FROM STREAM
{u'contributors': None, 
 u'truncated': False, 
 u'text': u'#AZvsSF THESE ARE THE CARDINALS I KNOW', 
 u'is_quote_status': False, 
 u'in_reply_to_status_id': None, 
 u'id': 784217049652264960, 
 u'favorite_count': 0, 
 u'source': u'<a href="http://twitter.com/download/iphone" rel="nofollow">Twitter for iPhone</a>',
 u'retweeted': False, 
 u'coordinates': None,
 u'timestamp_ms': u'1475806889342',
 u'entities': {u'user_mentions': [], u'symbols': [], u'hashtags': [{u'indices': [0, 7], u'text': u'AZvsSF'}], u'urls': []}, u'in_reply_to_screen_name': None, 
 u'id_str': u'784217049652264960',
 u'retweet_count': 0,
 u'in_reply_to_user_id': None, 
 u'favorited': False, 
 
 u'user': {
     u'follow_request_sent': None, 
     u'profile_use_background_image': False, 
     u'default_profile_image': False,
     u'id': 1623724580, 
     u'verified': False, 
     u'profile_image_url_https': u'https://pbs.twimg.com/profile_images/754456973270056960/umtsrMcw_normal.jpg', u'profile_sidebar_fill_color': u'000000', 
     u'profile_text_color': u'000000', 
     u'followers_count': 332, 
     u'profile_sidebar_border_color': u'000000', 
     u'id_str': u'1623724580', 
     u'profile_background_color': u'000000', 
     u'listed_count': 2, 
     u'profile_background_image_url_https': u'https://abs.twimg.com/images/themes/theme1/bg.png', 
     u'utc_offset': -18000, 
     u'statuses_count': 6961, 
     u'description': u'sc:caleb_conerly Cardinals 1-3',
     u'friends_count': 188, 
     u'location': u'Houston, TX', 
     u'profile_link_color': u'000000', 
     u'profile_image_url': u'http://pbs.twimg.com/profile_images/754456973270056960/umtsrMcw_normal.jpg', 
     u'following': None,
     u'geo_enabled': True, 
     u'profile_banner_url': u'https://pbs.twimg.com/profile_banners/1623724580/1471659383', 
     u'profile_background_image_url': u'http://abs.twimg.com/images/themes/theme1/bg.png', 
     u'name': u'CXI', 
     u'lang': u'en', 
     u'profile_background_tile': False, 
     u'favourites_count': 5591, 
     u'screen_name': u'Cconerly_', 
     u'notifications': None, u'url': u'https://curiouscat.me/Cconerly_6', 
     u'created_at': u'Fri Jul 26 19:44:46 +0000 2013', 
     u'contributors_enabled': False, 
     u'time_zone': u'Central Time (US & Canada)', 
     u'protected': False, 
     u'default_profile': False, 
     u'is_translator': False}, 
 u'geo': None, 
 u'in_reply_to_user_id_str': None,
 u'lang': u'en', 
 u'created_at': u'Fri Oct 07 02:21:29 +0000 2016',
 u'filter_level': u'low', 
 u'in_reply_to_status_id_str': None, 
 u'place': None
}
'''
'''

for tweet in tweepy.Cursor(api.search, q="hate trump", lang = "en").items(300):
#    print tweet.text.encode("utf-8")
    count = count + 1
    #might be an issue with the file path
    fileOut = open("output.csv", "a")
    fileOut.write(tweet.user.screen_name + "  ||  " + tweet.text + "  ||  " + str(tweet.created_at))
    fileOut.write("\n")
    fileOut.close()
    print str(count) + "\t" + tweet.user.screen_name + "  ||  " + tweet.text 
                

print "done"





#twitterStream.filter(locations=[-119.45,33.46,-116.94,34.44]) #NC
#twitterStream.filter(locations=[-84.309940, 34.98, -74.96, 36.53])
#except baseExcpetion, e:
#    print "Failed on read", str(e)
#    time.sleep(5)
'''


'''
Status(contributors=None, truncated=False, text=u'@mignaci0 why you gotta write thanks Dev', is_quote_status=False, in_reply_to_status_id=782958916221140994, id=782962166030667776, favorite_count=0, _api=<tweepy.api.API object at 0x10650fc10>, author=User(follow_request_sent=False, has_extended_profile=False, profile_use_background_image=True, _json={u'follow_request_sent': False, u'has_extended_profile': False, u'profile_use_background_image': True, u'default_profile_image': False, u'id': 202745499, u'profile_background_image_url_https': u'https://abs.twimg.com/images/themes/theme1/bg.png', u'verified': False, u'profile_text_color': u'333333', u'profile_image_url_https': u'https://pbs.twimg.com/profile_images/3275822229/b3cc7a8612c9e37b530a29470ec1a488_normal.jpeg', u'profile_sidebar_fill_color': u'DDEEF6', u'entities': {u'description': {u'urls': []}}, u'followers_count': 145, u'profile_sidebar_border_color': u'C0DEED', u'id_str': u'202745499', u'profile_background_color': u'C0DEED', u'listed_count': 2, u'is_translation_enabled': False, u'utc_offset': -18000, u'statuses_count': 12165, u'description': u'', u'friends_count': 170, u'location': u'Central New Jersey', u'profile_link_color': u'0084B4', u'profile_image_url': u'http://pbs.twimg.com/profile_images/3275822229/b3cc7a8612c9e37b530a29470ec1a488_normal.jpeg', u'following': False, u'geo_enabled': False, u'profile_banner_url': u'https://pbs.twimg.com/profile_banners/202745499/1361243371', u'profile_background_image_url': u'http://abs.twimg.com/images/themes/theme1/bg.png', u'screen_name': u'devykins', u'lang': u'en', u'profile_background_tile': False, u'favourites_count': 74, u'name': u'devykins\u2122\xa9\uf8ff', u'notifications': False, u'url': None, u'created_at': u'Thu Oct 14 18:45:18 +0000 2010', u'contributors_enabled': False, u'time_zone': u'Quito', u'protected': False, u'default_profile': True, u'is_translator': False}, time_zone=u'Quito', id=202745499, _api=<tweepy.api.API object at 0x10650fc10>, verified=False, profile_text_color=u'333333', profile_image_url_https=u'https://pbs.twimg.com/profile_images/3275822229/b3cc7a8612c9e37b530a29470ec1a488_normal.jpeg', profile_sidebar_fill_color=u'DDEEF6', is_translator=False, geo_enabled=False, entities={u'description': {u'urls': []}}, followers_count=145, protected=False, id_str=u'202745499', default_profile_image=False, listed_count=2, lang=u'en', utc_offset=-18000, statuses_count=12165, description=u'', friends_count=170, profile_link_color=u'0084B4', profile_image_url=u'http://pbs.twimg.com/profile_images/3275822229/b3cc7a8612c9e37b530a29470ec1a488_normal.jpeg', notifications=False, profile_background_image_url_https=u'https://abs.twimg.com/images/themes/theme1/bg.png', profile_background_color=u'C0DEED', profile_banner_url=u'https://pbs.twimg.com/profile_banners/202745499/1361243371', profile_background_image_url=u'http://abs.twimg.com/images/themes/theme1/bg.png', name=u'devykins\u2122\xa9\uf8ff', is_translation_enabled=False, profile_background_tile=False, favourites_count=74, screen_name=u'devykins', url=None, created_at=datetime.datetime(2010, 10, 14, 18, 45, 18), contributors_enabled=False, location=u'Central New Jersey', profile_sidebar_border_color=u'C0DEED', default_profile=True, following=False), _json={u'contributors': None, u'truncated': False, u'text': u'@mignaci0 why you gotta write thanks Dev', u'is_quote_status': False, u'in_reply_to_status_id': 782958916221140994, u'id': 782962166030667776, u'favorite_count': 0, u'entities': {u'symbols': [], u'user_mentions': [{u'id': 85904684, u'indices': [0, 9], u'id_str': u'85904684', u'screen_name': u'mignaci0', u'name': u'Leeneaux'}], u'hashtags': [], u'urls': []}, u'retweeted': False, u'coordinates': None, u'source': u'<a href="http://twitter.com/download/iphone" rel="nofollow">Twitter for iPhone</a>', u'in_reply_to_screen_name': u'mignaci0', u'in_reply_to_user_id': 85904684, u'retweet_count': 0, u'id_str': u'782962166030667776', u'favorited': False, u'user': {u'follow_request_sent': False, u'has_extended_profile': False, u'profile_use_background_image': True, u'default_profile_image': False, u'id': 202745499, u'profile_background_image_url_https': u'https://abs.twimg.com/images/themes/theme1/bg.png', u'verified': False, u'profile_text_color': u'333333', u'profile_image_url_https': u'https://pbs.twimg.com/profile_images/3275822229/b3cc7a8612c9e37b530a29470ec1a488_normal.jpeg', u'profile_sidebar_fill_color': u'DDEEF6', u'entities': {u'description': {u'urls': []}}, u'followers_count': 145, u'profile_sidebar_border_color': u'C0DEED', u'id_str': u'202745499', u'profile_background_color': u'C0DEED', u'listed_count': 2, u'is_translation_enabled': False, u'utc_offset': -18000, u'statuses_count': 12165, u'description': u'', u'friends_count': 170, u'location': u'Central New Jersey', u'profile_link_color': u'0084B4', u'profile_image_url': u'http://pbs.twimg.com/profile_images/3275822229/b3cc7a8612c9e37b530a29470ec1a488_normal.jpeg', u'following': False, u'geo_enabled': False, u'profile_banner_url': u'https://pbs.twimg.com/profile_banners/202745499/1361243371', u'profile_background_image_url': u'http://abs.twimg.com/images/themes/theme1/bg.png', u'screen_name': u'devykins', u'lang': u'en', u'profile_background_tile': False, u'favourites_count': 74, u'name': u'devykins\u2122\xa9\uf8ff', u'notifications': False, u'url': None, u'created_at': u'Thu Oct 14 18:45:18 +0000 2010', u'contributors_enabled': False, u'time_zone': u'Quito', u'protected': False, u'default_profile': True, u'is_translator': False}, u'geo': None, u'in_reply_to_user_id_str': u'85904684', u'lang': u'en', u'created_at': u'Mon Oct 03 15:15:01 +0000 2016', u'in_reply_to_status_id_str': u'782958916221140994', u'place': None, u'metadata': {u'iso_language_code': u'en', u'result_type': u'recent'}}, coordinates=None, entities={u'symbols': [], u'user_mentions': [{u'id': 85904684, u'indices': [0, 9], u'id_str': u'85904684', u'screen_name': u'mignaci0', u'name': u'Leeneaux'}], u'hashtags': [], u'urls': []}, in_reply_to_screen_name=u'mignaci0', id_str=u'782962166030667776', retweet_count=0, in_reply_to_user_id=85904684, favorited=False, source_url=u'http://twitter.com/download/iphone', user=User(follow_request_sent=False, has_extended_profile=False, profile_use_background_image=True, _json={u'follow_request_sent': False, u'has_extended_profile': False, u'profile_use_background_image': True, u'default_profile_image': False, u'id': 202745499, u'profile_background_image_url_https': u'https://abs.twimg.com/images/themes/theme1/bg.png', u'verified': False, u'profile_text_color': u'333333', u'profile_image_url_https': u'https://pbs.twimg.com/profile_images/3275822229/b3cc7a8612c9e37b530a29470ec1a488_normal.jpeg', u'profile_sidebar_fill_color': u'DDEEF6', u'entities': {u'description': {u'urls': []}}, u'followers_count': 145, u'profile_sidebar_border_color': u'C0DEED', u'id_str': u'202745499', u'profile_background_color': u'C0DEED', u'listed_count': 2, u'is_translation_enabled': False, u'utc_offset': -18000, u'statuses_count': 12165, u'description': u'', u'friends_count': 170, u'location': u'Central New Jersey', u'profile_link_color': u'0084B4', u'profile_image_url': u'http://pbs.twimg.com/profile_images/3275822229/b3cc7a8612c9e37b530a29470ec1a488_normal.jpeg', u'following': False, u'geo_enabled': False, u'profile_banner_url': u'https://pbs.twimg.com/profile_banners/202745499/1361243371', u'profile_background_image_url': u'http://abs.twimg.com/images/themes/theme1/bg.png', u'screen_name': u'devykins', u'lang': u'en', u'profile_background_tile': False, u'favourites_count': 74, u'name': u'devykins\u2122\xa9\uf8ff', u'notifications': False, u'url': None, u'created_at': u'Thu Oct 14 18:45:18 +0000 2010', u'contributors_enabled': False, u'time_zone': u'Quito', u'protected': False, u'default_profile': True, u'is_translator': False}, time_zone=u'Quito', id=202745499, _api=<tweepy.api.API object at 0x10650fc10>, verified=False, profile_text_color=u'333333', profile_image_url_https=u'https://pbs.twimg.com/profile_images/3275822229/b3cc7a8612c9e37b530a29470ec1a488_normal.jpeg', profile_sidebar_fill_color=u'DDEEF6', is_translator=False, geo_enabled=False, entities={u'description': {u'urls': []}}, followers_count=145, protected=False, id_str=u'202745499', default_profile_image=False, listed_count=2, lang=u'en', utc_offset=-18000, statuses_count=12165, description=u'', friends_count=170, profile_link_color=u'0084B4', profile_image_url=u'http://pbs.twimg.com/profile_images/3275822229/b3cc7a8612c9e37b530a29470ec1a488_normal.jpeg', notifications=False, profile_background_image_url_https=u'https://abs.twimg.com/images/themes/theme1/bg.png', profile_background_color=u'C0DEED', profile_banner_url=u'https://pbs.twimg.com/profile_banners/202745499/1361243371', profile_background_image_url=u'http://abs.twimg.com/images/themes/theme1/bg.png', name=u'devykins\u2122\xa9\uf8ff', is_translation_enabled=False, profile_background_tile=False, favourites_count=74, screen_name=u'devykins', url=None, created_at=datetime.datetime(2010, 10, 14, 18, 45, 18), contributors_enabled=False, location=u'Central New Jersey', profile_sidebar_border_color=u'C0DEED', default_profile=True, following=False), geo=None, in_reply_to_user_id_str=u'85904684', lang=u'en', created_at=datetime.datetime(2016, 10, 3, 15, 15, 1), in_reply_to_status_id_str=u'782958916221140994', place=None, source=u'Twitter for iPhone', retweeted=False, metadata={u'iso_language_code': u'en', u'result_type': u'recent'})
'''
