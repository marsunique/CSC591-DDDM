import praw
import re
#from pathlib import Path
#import time

#Input Variables:
    
username = 'comment_scraper' #your username
password = 'scraping' #your password
output_path = '/home/team7/Reddit_Files/Output/'
reg_exp = ".?([Hh][Ii][Ll][Ll][Aa][Rr][Yy]).?|([Tt][Rr][Uu][Mm][Pp]).?|([Cc][Ll][Ii][Nn][Tt][Oo][Nn]).?|([Rr][Ee][Pp][Uu][Bb][Ll][Ii][Cc][Aa][Nn]).?|([Dd][Ee][Mm][Oo][Cc][Rr][Aa][Tt]).?|([Dd][Ee][Bb][Aa][Tt][Ee]).?"
#subreddit = 'politics'
#category = 'hot' #pick from (hot, new, rising, controversial, top, gilded)
#subreddit_limit = 5 #max 1000


r = praw.Reddit(user_agent='Political Comments Scraper v1.0 by' + username)
r.login(username, password)
print("\nReady to search, m'lord!")

def get_category(cat,subreddit,subreddit_limit):
    catstr = 'get_' + cat
    return(getattr(r.get_subreddit(subreddit),catstr))(limit=subreddit_limit)
    
#regular expressions (regex)
def keywords(search_this): 
    return(re.search(reg_exp, search_this))   

    
    

#specific thread
#sub = r.get_submission(submission_id='58eh18')

#for a specific subreddit, put the ID in the myfilter section (ex: '58eh18')
def runsearch(subreddit,category,subreddit_limit,myfilter=True):
    #masterpath = Path(output_path + 'masterfile.txt')
    #if masterpath.is_file():
    if False:
        #get last line in master file
        master = open(output_path + 'masterfile.txt','rb')
        with master as f:
            f.seek(-2, 2)             # Jump to the second last byte.
            while f.read(1) != b"\n": # Until EOL is found...
                f.seek(-2, 1)         # ...jump back the read byte plus one more.
            last = f.readline()       # Read last line.
        master.close()
        lastline = last.decode()
        item = int(lastline[0:lastline.index(',')]) + 1
    else:
        master = open(output_path + 'masterfile.txt','w+')
        master.write('ITEM NUMBER, THREAD TITLE,THREAD ID, CREATED\n0, DEFAULT ENTRY, NONE, 0\n')
        master.close()
        item = 1
    if myfilter==True or myfilter==False:
        submissions = get_category(category,subreddit,subreddit_limit)    
        for sub in submissions:
            title = sub.title
            title = (title.encode('ascii',errors='ignore')).decode()
    #        url = sub.url
            thread = sub.id
            created = sub.created
            if myfilter==True:
                if keywords(title):
                    master = open(output_path + 'masterfile.txt','r') 
                    if thread not in master.read():
                        master.close()
                        master = open(output_path + 'masterfile.txt','a')
                        master.write(str(item) + ', [' + title + '], ' + thread + ', ' + str(created) + '\n')
                        master.close()
                        sub.replace_more_comments(limit=None, threshold=0)
                        comments = praw.helpers.flatten_tree(sub.comments)
                        commentfile = open(output_path + str(item) + ' comments.txt','w')
                        commentdetails = open(output_path + str(item) + ' details.txt','w')
                        for x in list(range(len(comments))):
                            comment = " ".join(((comments[x].body).strip()).split())
                            if comments[x].author_flair_text is None:
                                flair = 'None'
                            else: flair = comments[x].author_flair_text
                            commentdetails.write(str(comments[x].score) + ', ' + flair + ', ' + str(comments[x].created) + '\n')
                            try:
                                commentfile.write(comment + '\n')
                            except UnicodeEncodeError:
                                commentfile.write((comment.encode('ascii',errors='ignore')).decode() + '\n')              
                        commentfile.close()
                        commentdetails.close()
                        item = item + 1
                    else:
                        master.close()
            if myfilter==False:
                master = open(output_path + 'masterfile.txt','r') 
                if thread not in master.read():
                    master.close()
                    master = open(output_path + 'masterfile.txt','a')
                    master.write(str(item) + ', [' + title + '], ' + thread + ', ' + str(created) + '\n')
                    master.close()
                    sub.replace_more_comments(limit=None, threshold=0)
                    comments = praw.helpers.flatten_tree(sub.comments)
                    commentfile = open(output_path + str(item) + ' comments.txt','w')
                    commentdetails = open(output_path + str(item) + ' details.txt','w')
                    for x in list(range(len(comments))):
                        comment = " ".join(((comments[x].body).strip()).split())
                        if comments[x].author_flair_text is None:
                            flair = 'None'
                        else: flair = comments[x].author_flair_text
                        commentdetails.write(str(comments[x].score) + ', ' + flair + ', ' + str(comments[x].created) + '\n')
                        try:
                            commentfile.write(comment + '\n')
                        except UnicodeEncodeError:
                            commentfile.write((comment.encode('ascii',errors='ignore')).decode() + '\n')              
                    commentfile.close()
                    commentdetails.close()
                    item = item + 1
                else:
                    master.close()  
    else:
        sub = r.get_submission(submission_id=myfilter)
        title = sub.title
        thread = sub.id
        created = sub.created
        master = open(output_path + 'masterfile.txt','r')
        if thread not in master.read():
            master.close()
            master = open(output_path + 'masterfile.txt','a')
            master.write(str(item) + ', [' + title + '], ' + thread + ', ' + str(created) + '\n')
            master.close()
            sub.replace_more_comments(limit=None, threshold=0)
            comments = praw.helpers.flatten_tree(sub.comments)
            commentfile = open(output_path + str(item) + ' comments.txt','w')
            commentdetails = open(output_path + str(item) + ' details.txt','w')
            for x in list(range(len(comments))):
                comment = " ".join(((comments[x].body).strip()).split())
                if comments[x].author_flair_text is None:
                    flair = 'None'
                else: flair = comments[x].author_flair_text
                commentdetails.write(str(comments[x].score) + ', ' + flair + ', ' + str(comments[x].created) + '\n')
                try:
                    commentfile.write(comment + '\n')
                except UnicodeEncodeError:
                    commentfile.write((comment.encode('ascii',errors='ignore')).decode() + '\n')              
            commentfile.close()
            commentdetails.close
        else:
            master.close()             
                
runsearch('politics','top_from_week',200,False)
            
            
            
#vars(comments[10]) 
#print dir(sub)
         


         
#commentlist = []
#comment_list = []
#for x in list(range(len(comments))):
#    for y in list(range(len(comments[x]))):
#        commentlist = commentlist + [[comments[x][y].body]]
#    comment_list = comment_list + [[commentlist]]

#def get_date(submission):
#    time = submission.created
#    return datetime.datetime.fromtimestamp(time)