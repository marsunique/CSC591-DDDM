import psycopg2 as psql
import math

class Score_Normalization(object):
    def __init__(self):
        self.maxScore = 1
    def findMax(self, cur):
        query = "SELECT MAX(likes::int) FROM normalization_test"
        cur.execute(query);
        res = cur.fetchone()
        print res
        self.maxScore = res[0] + 2
        print self.maxScore
    
    def normalize(self, cur, conn):
        print "IN NORMALIZE()"
        query = "SELECT * FROM normalization_test"
        cur.execute(query)
        cur2 = conn.cursor()
        for row in cur:
            comment = row[0]
            likes = str(math.log(int(row[1])+2, self.maxScore) * 10)
            # likes = str((int(row[1])+1)/float(self.maxScore)*10)
            location = row[2]
            source = row[3]
            identifier = row[4]
            # print 'original score: ', row[1]
            # print 'after normalized: ', str(math.log(int(row[2]+2), self.maxScore) * 10)
            insert_query = "INSERT INTO normalization_after_test (comment, likes, source, identifier) VALUES (%s, %s, %s, %s)"
            cur2.execute(insert_query, (comment, likes, source, identifier));
            conn.commit()

    def run(self):
        conn = psql.connect(database = 'team7')
        if conn != None:
            print "Database Connection Successful"
        else:
            print "Database Connection Failed!"
        cur = conn.cursor()
        try:
            self.findMax(cur)
            self.normalize(cur, conn)
        finally:
            conn.close()
            print 'Normalization Done!'

if __name__ == '__main__':
    test = Score_Normalization()
    test.run()
