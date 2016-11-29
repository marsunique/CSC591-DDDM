import praw


    
username = 'comment_scraper' #your username
password = 'scraping' #your password
output_path = 'C:/Users/Tim Sawicki/Documents/Python Scripts/title grab/'
#subreddit = 'politics'
#category = 'top_from_year' #pick from (hot, new, rising, controversial, top, gilded)
#subreddit_limit = 1000 #max 1000


r = praw.Reddit(user_agent='Topic Scraper v1.0 by' + username)
r.login(username, password)
print("\nReady to search, m'lord!")

def get_category(cat,subreddit,subreddit_limit):
    catstr = 'get_' + cat
    return(getattr(r.get_subreddit(subreddit),catstr))(limit=subreddit_limit)
    
def title_grabs(subreddit,category,subreddit_limit):
    master = open(output_path + subreddit + ' ' + category + ' titles.txt','w')
    master.write('ITEM, TITLE, THREAD_ID, CREATED, UPVOTES\n')
    master.close()
    item = 1
    submissions = get_category(category,subreddit,subreddit_limit)    
    for sub in submissions:
        title = sub.title
        title = (title.encode('ascii',errors='ignore')).decode()
        thread = sub.id
        created = sub.created
        upvotes = sub.score
        master = open(output_path + subreddit + ' ' + category + ' titles.txt','a')
        master.write(str(item) + ', [' + title + '], ' + thread + ', ' + str(created) + ', ' + str(upvotes) + '\n')
        master.close() 
        item = item + 1


sublist = ['politics','PoliticalDiscussion','thedonald','sandersforpresident',
'political_revolution','hillaryclinton','neutralpolitics','liberal','conservative',
'democrats','republicans','moderatepolitics','politicalfactchecking','economics',
'environment','progressive','libertarian']        

typelist = ['top_from_year','controversial_from_year','top_from_month','controversial_from_month']


for i in sublist:
    for j in typelist:        
        title_grabs(i, j, 1000)






        
def title_scrape(titlelist):
    title_list = []
    for i in titlelist[2:]:
        start = i.index('[')
        end = i.index(']')
        title_list = title_list + [i[start+1:end]]
    return(title_list)        
                


sublist2 = ['politics','PoliticalDiscussion','thedonald','sandersforpresident',
'political_revolution','hillaryclinton','neutralpolitics','liberal','conservative',
'democrats','republicans','moderatepolitics','politicalfactchecking','progressive','libertarian']  
        
full_list = []                      
for i in sublist2:
    for j in typelist:
        textfile = open(output_path + i + ' ' + j + 'titles.txt','r')
        titlelist = textfile.readlines()
        textfile.close() 
        temp = title_scrape(titlelist)
    full_list = full_list + [temp]











           
#dir(sub)