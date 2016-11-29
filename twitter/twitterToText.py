import psycopg2


try:
    conn = psycopg2.connect("dbname='team7' user='team7' host='/tmp/' password=''")
except:
    print "database connection error"

curr = conn.cursor()

query = "SELECT tweet_id FROM tweets;"
        
curr.execute(query)#,data)
conn.commit()

rows = curr.fetchall()
        
with open('tweetsToUpdate.txt', 'w+') as outFile:
    count = 0
    for row in rows:
        if count % 1000000 == 0:
            print count
        newItem = str(row)[1:]
        newItem = newItem[:-3]
        
        outFile.write(newItem +',')
        count = count + 1
