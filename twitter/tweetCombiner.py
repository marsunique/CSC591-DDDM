import psycopg2
import re
import json

import sys
reload(sys)
sys.setdefaultencoding('utf8')


try:
    conn = psycopg2.connect(database='team7', user='team7', host='/tmp/', password='')  
    debateTweets = []
    with open("backups/debate_fetched_tweets.txt", "r+") as openFile:
        for item in openFile:
            try:
                all_data = json.loads(item)
                tweet = all_data["text"]
                userName = all_data["user"]["screen_name"]
                match = re.search(".?([Hh][Ii][Ll][Ll][Aa][Rr][Yy]).?|([Tt][Rr][Uu][Mm][Pp]).?|([Cc][Ll][Ii][Nn][Tt][Oo][Nn]).?|([Rr][Ee][Pp][Uu][Bb][Ll][Ii][Cc][Aa][Nn]).?|([D    d][Ee][Mm][Oo][Cc][Rr][Aa][Tt]).?|([Dd][Ee][Bb][Aa][Tt][Ee]).?", tweet) 
                if match:
                    newItem = [userName, tweet]
                    debateTweets.append(newItem)
    
                    cur = conn.cursor()
                    cur.execute("INSERT INTO tweets VALUES(" + userName +", " + tweet + " 1, 1)")
                    conn.commit() 

            except (ValueError):
                print "ERROR----------------------------------------------------------------" 


    with open("backups/debate_fetched_tweets_dustin.txt", "r+") as openFile:
        i = 0
        for item in openFile:
            try:
                all_data = json.loads(item)
                tweet = all_data["text"]
                userName = all_data["user"]["screen_name"]
                match = re.search(".?([Hh][Ii][Ll][Ll][Aa][Rr][Yy]).?|([Tt][Rr][Uu][Mm][Pp]).?|([Cc][Ll][Ii][Nn][Tt][Oo][Nn]).?|([Rr][Ee][Pp][Uu][Bb][Ll][Ii][Cc][Aa][Nn]).?|([D    d][Ee][Mm][Oo][Cc][Rr][Aa][Tt]).?|([Dd][Ee][Bb][Aa][Tt][Ee]).?", item) 
                if match:
                    if item not in debateTweets:
                        i = i + 1
                        newItem = [userName, tweet]
                        debateTweets.append(newItem)
                        cur = conn.cursor()
                        cur.execute("INSERT INTO tweets VALUES(" + userName +", " + tweet + " 1, 1)")
                        conn.commit() 
                        if i % 1000 == 0:
                            print str(i) + " second one"
            except (ValueError):
                print "ERROR"
    print len(debateTweets)

    with open("backups/rama_debate_fetched_tweets.txt", "r+") as openFile:
        i = 0
        for item in openFile:
            try:
                all_data = json.loads(item)
                tweet = all_data["text"]
                userName = all_data["user"]["screen_name"]
                match = re.search(".?([Hh][Ii][Ll][Ll][Aa][Rr][Yy]).?|([Tt][Rr][Uu][Mm][Pp]).?|([Cc][Ll][Ii][Nn][Tt][Oo][Nn]).?|([Rr][Ee][Pp][Uu][Bb][Ll][Ii][Cc][Aa][Nn]).?|([D    d][Ee][Mm][Oo][Cc][Rr][Aa][Tt]).?|([Dd][Ee][Bb][Aa][Tt][Ee]).?", item) 
                if match:
                    if item not in debateTweets:
                        i = i + 1
                        newItem = [userName, tweet]
                        debateTweets.append(newItem)
                        cur = conn.cursor()
                        cur.execute("INSERT INTO tweets VALUES(" + userName +", " + tweet + " 1, 1)")
                        conn.commit() 
                        if i % 1000 == 0:
                            print str(i) + " third one"
            except (ValueError):
                print "ERROR"
    print len(debateTweets)

except psycopg2.DatabaseError, e:
    if conn:
        conn.rollback()

    print str(e)
    sys.exit(1)
'''
with open("allThreeCombinedTwitterFeed.txt", "w+") as newFile:
    i = 0
    for item in debateTweets:
        newFile.write(item)

'''



'''
with open("combinedTwitterFeed.txt", "r+") as outFile:
    for item in outFile:
        #outFile.write(item)
        all_data = json.loads(item)
        tweet = all_data["text"]
        #print tweet
        with open("tweetText.txt", "a") as outieFile:
            outieFile.write(tweet)
'''
  
