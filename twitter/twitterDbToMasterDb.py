

import psycopg2


try:
    conn = psycopg2.connect("dbname='team7' user='team7' host='/tmp/' password=''")
except:
    print "database connection error"

curr = conn.cursor()

try:
    query = "DELETE FROM temp_master_data WHERE source = 'twitter';"
    curr.execute(query)#,data)
    conn.commit()
    
    query = "INSERT INTO temp_master_data (identifier, source, comment, likes) SELECT tweet_id::text, 'twitter', text, favorite_count+retweet_count  FROM tweets LIMIT 10;"
    #query = "UPDATE master_data SET comment = (SELECT text::text FROM tweets WHERE tweets.tweet_id::text = master_data.identifier);"
    #query = "SELECT * FROM master_data WHERE source = 'twitter';" 

            #data = (text,username,timeStamp,userId,location,language,created_at,followers_count,tweet_id,favorite_count,retweet_count,friends_count,timeZone,in_reply_to_status_id_str,favorited,verified)

    curr.execute(query)#,data)
    conn.commit()

    
    query = "SELECT * FROM temp_master_data WHERE source = 'twitter';"
    
    curr.execute(query)#,data)
    conn.commit()

    rows = curr.fetchall()
    
    for row in rows:
        print row

except Exception, e:
    print str(e)
    conn.rollback()
