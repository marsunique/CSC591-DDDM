# MUST DOWNLOAD PUNKT, AVG_perceptron, tagsets(?), maxent_treebank, stopwords, 
# brown Corpus, corpora_worldnet
 
#nltk.download()
import praw
from pathlib import Path
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
import gensim
from gensim import corpora, models
from nltk.collocations import *
from vaderSentiment.vaderSentiment import sentiment as vaderSentiment
from collections import defaultdict


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


#sublist2 = ['politics','PoliticalDiscussion','thedonald','sandersforpresident',
#'political_revolution','hillaryclinton','neutralpolitics','liberal','conservative',
#'democrats','republicans','moderatepolitics','politicalfactchecking','economics',
#'environment','progressive','libertarian']        

sublist = ['politics','PoliticalDiscussion','thedonald','sandersforpresident',
'political_revolution','hillaryclinton','neutralpolitics','liberal','conservative',
'democrats','republicans','moderatepolitics','politicalfactchecking','progressive','libertarian']


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
                        
full_list = []                      
for i in sublist:
    for j in typelist:
        textfile = open(output_path + i + ' ' + j + 'titles.txt','r')
        titlelist = textfile.readlines()
        textfile.close() 
        temp = title_scrape(titlelist)
    full_list = full_list + [temp]




#def combine_comment_files(start):
#    i = start
#    input_path= 'C:/Users/Tim Sawicki/Documents/Python Scripts/output/'
#    comment_path = Path(input_path + str(i) + ' comments.txt')
#    with open(input_path + 'combinedfile.txt', 'w') as outfile:
#        while comment_path.is_file():
#            with open(input_path + str(i) + ' comments.txt') as infile:
#                for line in infile:
#                    outfile.write(line)
#            infile.close()
#            i = i+1
#            comment_path = Path(input_path + str(i) + ' comments.txt')
#    outfile.close()
#    return()
#    
#combine_comment_files(1)
#
#
#input_path= 'C:/Users/Tim Sawicki/Documents/Python Scripts/title grab/'
#textfile = open(input_path + 'COMBINED.txt','r')
#commentlist = textfile.readlines()
#textfile.close()



















stopwordlist = stopwords.words('english')
lemmatizer = WordNetLemmatizer()
p_stemmer = PorterStemmer()
pos_list = ['NN','VB','NNS','VBS']





#---------------------------------TOKENIZING---------------------------------




#To Tokenize to words
def strip_tags(comments):
    return([x.strip() for x in comments])

def sentences(comments):
    return([nltk.sent_tokenize(x) for x in comments])
    
def unnest_sentences(comments_as_sentences):
    sentences_as_list = []
    for x in list(range(len(comments_as_sentences))):
        for y in list(range(len(comments_as_sentences[x]))):
            sentences_as_list = sentences_as_list + [comments_as_sentences[x][y]]
    return(sentences_as_list)

def singlewords(sentence):
    return([nltk.word_tokenize(x) for x in sentence])
    
# Remove sentences of X length
def remove_sentences(sentences):
    return([x for x in sentences if len(x) > 3])    
    
    
    
    




    
#-----------------------------LIST OF FUNCTIONS------------------------------    

#Once list is tokenized into words, you can now do any function on them using this:
def loop_on_tokenized(list_of_words,function,needs_build=True):
    templist = []
    final = []
    if needs_build==True:
        for i in list(range(len(list_of_words))):
            for j in list(range(len(list_of_words[i]))):
                temp = function(list_of_words[i][j])
                if temp!='SKIP':
                    templist = templist + [temp]
            final = final + [templist]
            templist = []
    else:
        for i in list(range(len(list_of_words))):
            for j in list(range(len(list_of_words[i]))):
                list_of_words[i][j] = function(list_of_words[i][j])
                final = list_of_words
    return(final)  

def stopwords(word):
    if word not in stopwordlist:
        return(word)
    else:
        return('SKIP')
    
def fix_contractions(text):
    replacethis = {"n't":"not","'ve":"have","'s":"is","'d":"would","'ll":"will","'re":"are"}
    for i, j in replacethis.items():
        text = text.replace(i, j)
    return(text)

def is_url(word):
    if 'http' not in word:
        return(word)
    else:
        return('SKIP')
    
def is_char(word):
    if word.isalnum():
        return(word)
    else:
        return('SKIP')
    
def lowercase(word):
    return(word.lower())
    
def lemmatize_func(word):
    return(lemmatizer.lemmatize(word))
    
def stemmer(word):
    return(p_stemmer.stem(word))    

def pos_finder(all_sentences):
    temp = []
    for i in all_sentences:
        temp = temp + [nltk.pos_tag(i)]        
    return(temp)
    

def pos_filter(pos_tuple):
    for i in pos_list:
        if pos_tuple[1]==i:
            return(pos_tuple[0])
    return('SKIP')
    
def clear_empty(all_sentences):
    temp = []
    for i in all_sentences:
        if i != []:
            temp = temp + [i]
    return(temp)
            
def make_single_list(all_sentences):
    temp = []
    for i in list(range(len(all_sentences))):
        for j in list(range(len(all_sentences[i]))):
            temp = temp + [all_sentences[i][j]]
    return(temp)

        
#-------------------------------START CLEANING-------------------------------- 
    
    
    
    
    
# Get comments as tokenized list  
wordlist = strip_tags(commentlist)                          
wordlist = sentences(wordlist)
wordlist = unnest_sentences(wordlist)
wordlist = singlewords(wordlist)
wordlist = remove_sentences(wordlist)



# WORD FUNCTIONS
wordlist = loop_on_tokenized(wordlist,is_char)
wordlist = loop_on_tokenized(wordlist,lemmatize_func)
wordlist = loop_on_tokenized(wordlist,lowercase)
wordlist = loop_on_tokenized(wordlist,stopwords)
#wordlist = loop_on_tokenized(wordlist,fix_contractions,False)
wordlist = loop_on_tokenized(wordlist,is_url)
                          

wordlist = pos_finder(wordlist)                        
wordlist = loop_on_tokenized(wordlist,pos_filter) 
wordlist = clear_empty(wordlist)                



# CREATING FREQ TOPICS
wordlist2 = make_single_list(wordlist)
freq = nltk.FreqDist(wordlist2)
freqlist = freq.most_common(250)

topics = []
for i in freqlist:
    topics = topics + [i[0]]

output_path= 'C:/Users/Tim Sawicki/Documents/Python Scripts/'
master = open(output_path + 'topics2.txt','a+')
for i in topics:
    master.write(i + '\n')
master.close()




#--------------------FINAL BIGRAM TOPICS (FROM FREQ TOPICS)-------------------
#IF FIRST TIME
#topic_path= 'C:/Users/Tim Sawicki/Documents/Python Scripts/'
#textfile = open(topic_path + 'topics2.txt','r')
#topics = textfile.readlines()
#textfile.close()
#topics = strip_tags(topics) 
#bigram_measures = nltk.collocations.BigramAssocMeasures() 
#bigram_list = [] 
#for i in topics:
#    finder = BigramCollocationFinder.from_words(wordlist2)
#    finder.apply_ngram_filter(lambda w1, w2: i not in (w1, w2))
#    for j in finder.score_ngrams(bigram_measures.likelihood_ratio)[0:3]:
#        if j[1] > 40:
#            bigram_list = bigram_list + [j[0]]




#IF LOADING FROM TXT
sentence_path= 'C:/Users/Tim Sawicki/Documents/Python Scripts/'
textfile = open(sentence_path + 'final_topics2.txt','r')
topics_list = textfile.readlines()
textfile.close()
temp = []
for i in list(range(len(topics_list))):
    x = topics_list[i].strip()
    divide = x.index(',')
    word1 = x[:divide]
    word2 = x[divide+2:]
    temp = temp + [(word1,word2)]    
bigram_list = temp


bigrams_update = []
cutlist = []
for i in bigram_list:
    checklist = [(i[1], i[0]), (i[1] + 's', i[0]), (i[1], i[0] + 's'), (i[1] + 's', i[0] + 's'), (i[1][:-1], i[0]), 
             (i[1], i[0][:-1]), (i[1][:-1], i[0][:-1]), (i[0] + 's', i[1]), (i[0], i[1] + 's'),(i[0] + 's', i[1] + 's'),
             (i[0][:-1], i[1]), (i[0], i[1][:-1]), (i[0][:-1], i[1][:-1])]
    if i not in cutlist:
        for j in checklist:
            if j in bigram_list:
                cutlist = cutlist + [j]
        bigrams_update = bigrams_update + [i]


final_topic_path= 'C:/Users/Tim Sawicki/Documents/Python Scripts/'
for i in bigrams_update:
    master = open(final_topic_path + 'final_topics_cleaned.txt','a')
    master.write(i[0] + ', ' + i[1] + '\n')
    master.close()


            

#sentence_topics = []
#for i in bigram_list:
#    for j in wordlist:
#        if i[0] in j and i[1] in j:
#            sentence_topics = sentence_topics + [[j,i]]
#    
#d = defaultdict(int)
#for i in sentence_topics:
#        d[i[1]] += 1        




# COLLOCATIONS - requires wordlist2
#bigram_measures = nltk.collocations.BigramAssocMeasures()
#trigram_measures = nltk.collocations.TrigramAssocMeasures()
#finder = BigramCollocationFinder.from_words(wordlist2)
#finder2 = TrigramCollocationFinder.from_words(wordlist2)
#finder.nbest(bigram_measures.likelihood_ratio,50)
#finder2.nbest(trigram_measures.likelihood_ratio,50)




