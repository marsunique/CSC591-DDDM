import psycopg2
import sys
import codecs

reload(sys)
sys.setdefaultencoding('utf8')

try:
    conn = psycopg2.connect(database='team7', user='team7', host='/tmp/', password='')
    #conn = psycopg2.connect(
    curr = conn.cursor()
 
except psycopg2.DatabaseError, e:
    print 'Error %s' %e
    sys.exit(1)

curr.execute("SELECT text FROM tweets;")

with open("allTweets.txt", "w+") as outFile:   
    for record in curr:
        record = str(record).encode('utf-8')
        record = record[2:]
        outFile.write(record[:-3])
