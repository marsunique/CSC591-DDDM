import psycopg2

#def combine_comment_files(start, filetype):
#    i = start
#    input_path= 'C:/Users/Tim Sawicki/Documents/Python Scripts/output/'
#    endloop = False
#    with open(input_path + 'combined '+filetype+' file.txt', 'w') as outfile:
#        while endloop == False:
#            with open(input_path + str(i) + ' ' + filetype + '.txt') as infile:
#                for line in infile:
#                    outfile.write(line)
#            infile.close()
#            i = i+1
#            try:
#                comment_path = open(input_path + str(i) + ' ' + filetype + '.txt')
#                comment_path.close()
#            except (OSError,IOError,FileNotFoundError):
#                endloop = True
#    outfile.close()
#    return()
#    
#combine_comment_files(1, 'comments')
#combine_comment_files(1, 'details')     

state_list = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado',
'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 
'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan',
'Minnesota','Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 
'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 
'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 
'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 
'Wisconsin', 'Wyoming']


def write_comment_files(start,end='No'):
    psql_creds = {'dbname': 'team7'}
    conn = psycopg2.connect(**psql_creds)
    cur = conn.cursor()
    i = start
    input_path= '/home/team7/Reddit_Files/Previous Output/Output/'
    endloop = False
    master = open(input_path + 'masterfile.txt')
    for j in list(range(i+1)):
        master.readline()
    while endloop == False:
        commentlines = open(input_path + str(i) + ' comments.txt')
        detaillines = open(input_path + str(i) + ' details.txt')
        masterline = master.readline()
        find_id = masterline.index(']')
        find_stop = masterline.index(',', find_id+2)
        thread_id = masterline[find_id+3:find_stop]
        for line1,line2 in zip(commentlines,detaillines):
            comment = line1
            detail = line2
            detail = detail.split(',')
            if len(detail) > 3:
                detail[3] = detail[3].strip()
            else:
                detail = detail + ['Missing']
            if detail[1] in state_list:
                pass
            else:
                detail[1] = 'None'
            row_insert = (comment, detail[0], detail[1], 'Reddit', str(thread_id) + '_' + str(detail[3]))
            cur.execute("""INSERT INTO reddit_data2 (comment, likes, location, source, identifier) VALUES (%s, %s, %s, %s, %s);""", row_insert)    
            conn.commit()
        i = i+1
        commentlines.close()
        detaillines.close()
        if i == end:
            break
        try:
            comment_path = open(input_path + str(i) + ' comments.txt')
            comment_path.close()
        except (OSError,IOError):
            if i < 2852:
                print(str(i) + ' skipped')
                master.readline()
                i = i+1
            else:
                endloop = True
    master.close()
    conn.close()
    print('\n File writing has completed without errors, ending at ' + str(i))
    return()

write_comment_files(1)

#except (OSError,IOError,FileNotFoundError,NameError):