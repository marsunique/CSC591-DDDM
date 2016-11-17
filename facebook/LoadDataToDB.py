#-*- coding: utf-8 -*-
import glob

class Load_To_DB(object):
    def __init__(self):
        # self.file_list = glob.iglob("data\\*.csv")
        # self.file_list = './data/cnn_2016_11_08_11_13_56.csv'
        self.file_list = './data/_test.csv'
    def print_file_list(self):
        print self.file_list
    def mock_run(self):
        file_read = open(self.file_list)
        isRelevant = 0
        try:
            # for line in file_read:
            #     if 'Query url:' in line:
            #         continue
                # elif '----------------Post:----------------' in line:
            lines = file_read.readlines()
            MAX_LINE = len(lines)
            index = 1
            while index < MAX_LINE:
                if '----------------Post:----------------' in lines[index]:
                    topic = lines[index+2].strip()
                    ## need regular expression here to decide relevant or not
                    isRelevant = 1
                    index += 3
                elif '--------------Comments:--------------' in lines[index]:
                    index += 1
                elif 'Total Posts:' in lines[index]:
                    index += 1
                else:
                    if isRelevant:
                        line = lines[index].strip().split('|')
                        line = [s.strip() for s in line if s]
                        print line
                    index += 1
                    



                





        finally:
            file_read.close()
    def run(self):
        for csvfile in self.file_list:
            print csvfile
            # file_read = open()
if __name__ == '__main__':
    test = Load_To_DB()
    test.print_file_list()
    # test.run()
    test.mock_run()
