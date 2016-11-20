#-*- coding: utf-8 -*-
import glob
import psycopg2 as psql
import re
import time

class Load_To_DB(object):
    def __init__(self):
        self.file_list = glob.iglob("data_test/*.csv")
        # self.file_list = './data/cnn_2016_11_08_11_13_56.csv'
        # self.file_list = './data/_test.csv'
        # self.file_list = './data/pbs_2016_10_31_13_12_07.csv'
        self.word_bag = [
            'Vote', 'vote', 'Voting', 'voting', 'Hillary', 'hillary', 'Clinton', 'clinton',
            'Donald', 'donald', 'Trump', 'trump', 'Candidate', 'candidate', 'Elect', 'elect',
            'Election', 'election', 'President', 'president', 'Presidency', 'presidency',
            'Debate', 'debate', 'White House', 'White house', 'white house', 'Campaign', 'campaign',
            'Voter', 'voter', 'Poll', 'poll', 'Email', 'email', 'Wall', 'wall'
            ]
    def print_file_list(self):
        print self.file_list
    def mock_run(self):
        fileCount = 0
        fileCount += 1
        csvfile = './data/pbs_2016_10_31_13_12_07.csv'
        print csvfile
        # conn = psql.connect(database = 'team7')
        # if conn != None:
        #     print "Database Connection Successful"
        # cur = conn.cursor()
        file_read = open(csvfile)
        isRelevant = 0
        try:
            # for line in file_read:
            #     if 'Query url:' in line:
            #         continue
                # elif '----------------Post:----------------' in line:
            lines = file_read.readlines()
            MAX_LINE = len(lines)
            index = 1
            while index < 40: # MAX_LINE:
                if '----------------Post:----------------' in lines[index]:
                    isRelevant = 0
                    topic = ''
                    index += 2
                    while index < 40 and not ('--------------Comments:--------------' in lines[index]):
                        topic = topic + lines[index].strip()
                        index += 1
                    # apply filter here to decide relevant or not
                    for word in self.word_bag:
                        if word in topic:
                            isRelevant = 1
                            break
                elif '--------------Comments:--------------' in lines[index]:
                    index += 1
                elif 'Total Posts:' in lines[index]:
                    index += 1
                else:
                    if isRelevant:
                        line = lines[index].split('|')
                        line = [s.strip() for s in line]
                        print line
                        likes = line[2]
                        identifier = line[3]
                        comment = line[4]
                        if comment:
                            print 'there is a comment'
                            # cur.execute("INSERT INTO temp_master_data (comment, likes, source, identifier)\
                            #         VALUES (%s, %s, %s, %s)",(comment, likes, 'facebook', identifier));
                            # conn.commit()
                    index += 1
        except BaseException, e:
            print '-----in file:' + csvfile + '-----'
            print '-----index-----', index
            print str(e)
        finally:
            # conn.close()
            file_read.close()
        print fileCount
    def run(self):
        conn = psql.connect(database = 'team7')
        if conn != None:
            print "Database Connection Successful"
        else:
            print 'Database Connection Failed. Mission Abort!'
            return
        cur = conn.cursor()
        fileCount = 0
        totalLoadCount = 0
        logTime = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
        logPath = './log/LoadToDB_'+logTime+'.log'
        logWrite = open(logPath, 'w')
        for csvfile in self.file_list:
            fileCount += 1
            eachFileCount = 0
            isRelevant = 0
            file_read = open(csvfile)
            try:
                print 'Loading %s into database...' % (csvfile)
                lines = file_read.readlines()
                MAX_LINE = len(lines)
                index = 1
                while index < MAX_LINE:
                    if '----------------Post:----------------' in lines[index]:
                        isRelevant = 0
                        topic = ''
                        index += 2
                        while index < MAX_LINE and not ('--------------Comments:--------------' in lines[index]):
                            topic = topic + lines[index].strip()
                            index += 1
                        # apply filter here to decide relevant or not
                        for word in self.word_bag:
                            if word in topic:
                                isRelevant = 1
                                break
                    elif '--------------Comments:--------------' in lines[index]:
                        index += 1
                    elif 'Total Posts:' in lines[index]:
                        index += 1
                    else:
                        if isRelevant:
                            line = lines[index].split('|')
                            line = [s.strip() for s in line]
                            # print line
                            likes = line[2]
                            identifier = line[3]
                            comment = line[4]
                            if comment:
                                cur.execute("INSERT INTO normalization_test (comment, likes, source, identifier)\
                                        VALUES (%s, %s, %s, %s)",(comment, likes, 'facebook', identifier));
                                conn.commit()
                                eachFileCount += 1
                                totalLoadCount += 1
                        index += 1
            except BaseException, e:
                print '-----in file: ' + csvfile + '-----'
                print '-----in line: ' + str(index) + '-----'
                print str(e)
            except IOError:
                print 'Failed To Open ' + csvfile
            finally:
                file_read.close()
            print >> logWrite, 'In file %s, %d records were loaded into database' % (csvfile, eachFileCount)
        logWrite.close()
        conn.close()
        print '%d Files Loaded' % (fileCount)
        print '%d Records Loaded' % (totalLoadCount)
if __name__ == '__main__':
    test = Load_To_DB()
    # test.print_file_list()
    test.run()
    # test.mock_run()
