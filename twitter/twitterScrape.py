import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener 
import json
import time
import re

#emoji support
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')

ckey = "ESH4cnWcKgKVHFPcnIjpAUvbe"
csecret = "aTOvrDtmqn2I15RZKEANNNhkPsXryAlECDdmbkAp2L268Dw8N8" 
atoken = "3060784180-REBbkm5XaSZ1XBwpYDL6d6HS12CdXJ7Kz1JEMaR"
asecret = "CDtvPLmbIheR6GXgd5aIKuD0Jl0vJDpRdSIZqHtwpEcWs"

#fileOut = open("/Users/charliebuckets/Desktop/projects/smScraper/output.txt", "a")

class listener(StreamListener):
    def on_data(self, data):
        
        try:
            print "ANOTHER ONE."
            all_data = json.loads(data)
            tweet = all_data["text"]
            username = all_data["user"]["screen_name"]
            timeStamp = all_data["timestamp_ms"]
            hashTags = all_data["entities"]["hashtags"]
            userId = all_data["user"]["id"]
            location = all_data["user"]["location"]
            language = all_data["lang"]
            created_at = all_data["created_at"]
            place = all_data["place"]
            followers_count = all_data["user"]["followers_count"]
            
            #print all_data
            with open('fetched_tweets.txt','a') as tf:
                tf.write(data)
            #tf.close()


            #hiringString = re.search("[Tt][Rr][Uu][Mm][Pp]", tweet)
            #tweetString = tweet.encode("utf-8")
            
            return True
        
        except BaseException, e:
            print "Failed in OnData " + str(e)
            time.sleep(5)
    
    def on_error(self, status):
        print status
        return true
        
#    def on_exception(self, status):
#        print status

#try:
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=['#AZvsSF'])


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