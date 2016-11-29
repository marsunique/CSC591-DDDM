import json
import datetime
import psycopg2

import sys
reload(sys)
sys.setdefaultencoding('utf8')
 
try:
    conn = psycopg2.connect(database='team7', user='team7', host='/tmp/', password='')
    #conn = psycopg2.connect(
    curr = conn.cursor()
 
except psycopg2.DatabaseError, e:
    print 'Error %s' %e
    sys.exit(1)

#with open("allThreeCombinedTwitterFeed.txt", "r+") as inFile:
with open("/home/team7/debate_three_fetched_tweets_Zlati.txt", "r+") as inFile:
    for jsonItem in inFile:
      
        all_data = json.loads(jsonItem)
            
        try:
            
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
            if len(location) > 60:
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
            print "tweet " + str(type(tweet)
            print "username " + str(type(username)
            print "timeStamp " + str(type(timeStamp)
            print "location " + str(type(location)
            print "language " +type(language)
            print "created_at " + type(created_at)
            #print place
            print type(followers_count)
            print type(tweet_id)
            print type(favorite_count)
            print type(retweet_count)
            print type(favorited)
            print type(verified)
            print type(friends_count)
            print type(timeZone)
            print type(in_reply_to_status_id_str)
            '''


            
            query = "INSERT INTO tweets(text,username,timeStamp,userId,location,language,created_at,followers_count,tweet_id,favorite_count,retweet_count,friends_count,timezone,in_reply_to_status_id_str,favorited,verified) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
            data = (text,username,timeStamp,userId,location,language,created_at,followers_count,tweet_id,favorite_count,retweet_count,friends_count,timeZone,in_reply_to_status_id_str,favorited,verified)
              
            curr.execute(query,data)
            conn.commit()
                    
        except Exception, e:
            conn.rollback()
            #print  "ERROR " + str(e)
            #if "text" in str(e):
            #    print text
print "done"
            
