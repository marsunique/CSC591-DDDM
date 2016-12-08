import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.collocations import *
from nltk.sentiment.vader import SentimentIntensityAnalyzer
#from vaderSentiment.vaderSentiment import sentiment as vaderSentiment
#from vaderSentiment import sentiment as vaderSentiment 
import psycopg2

#install = ['averaged_perceptron_tagger','brown','maxent_treebank_pos_tagger',
#           'punkt','stopwords','tagsets','vader_lexicon','wordnet']

#for i in install:
#    nltk.download(i)

   








#-----------------------------Other required files----------------------------


#Reading the previously made topic list
sentence_path= '/home/team7/Reddit_Files/'
textfile = open(sentence_path + 'final_topics2.txt','r')
topics_list = textfile.readlines()
textfile.close()
temp = []
for i in list(range(len(topics_list))):
    x = topics_list[i].strip()
    divide = x.index(',')
    word1 = x[:divide]
    word2 = x[divide+2:]
    temp = temp + [[word1,word2]]    
topics_list = temp




stopwordlist = stopwords.words('english')
lemmatizer = WordNetLemmatizer()
p_stemmer = PorterStemmer()
pos_list = ['NN','VB','NNS']


#---------------------------------TOKENIZING---------------------------------




#To Tokenize to words
def strip_tags(comment):
    return(comment.strip())

def sentences(comment):
    return(nltk.sent_tokenize(comment))
    
def unnest_sentences(comment_as_sentences):
    sentences_as_list = []
    for x in list(range(len(comment_as_sentences))):
        sentences_as_list = sentences_as_list + [comment_as_sentences[x]]
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
def file_process(start_point, how_many='ALL'): #NOTE, THIS WILL BE A DATABASE READ LATER
    # Initialize Values. This will have to be a readline in loop
     
    psql_creds = {
    'dbname': 'team7'
    }
    
    conn = psycopg2.connect(**psql_creds)
    
    cur = conn.cursor()
    cur2 = conn.cursor()
    
    if how_many == 'ALL':
        cur.execute("""SELECT * from trial OFFSET (%s);""", (start_point,))
    else:
        cur.execute("""SELECT * from trial OFFSET (%s) LIMIT (%s);""", (start_point, how_many))
    
    for row in cur:
        comment = row[0]
        vote = row[1]
        loc = row[2]
        source = row[3]
        item = row[4]
        print(comment,vote,loc,source,item)
  
        # Get comments as tokenized list  
        sentenceclean = strip_tags(comment)                          
        sentencelist = sentences(sentenceclean)
        sentencelist = unnest_sentences(sentencelist)
        wordlist = singlewords(sentencelist)
   
        # WORD FUNCTIONS
        wordlist = loop_on_tokenized(wordlist,is_char)
        wordlist = loop_on_tokenized(wordlist,lowercase)
        wordlist = loop_on_tokenized(wordlist,is_url)
                         
        # get topics
        sentence_topics = []
        for i in topics_list:
            for j in list(range(len(wordlist))):
                if i[0] in wordlist[j] and i[1] in wordlist[j]:
                    sentence_topics = sentence_topics + [[j, i]]
                
        # Sentiment   
        sentiments = []
        sid = SentimentIntensityAnalyzer()
        for i in list(range(len(sentencelist))): 
            #vs = vaderSentiment(sentencelist[i])
            vs = sid.polarity_scores(sentencelist[i])
            sentiments = sentiments + [[i, vs]]
                
        # Collect sentences with topics
        collected = []
        for i in list(range(len(sentence_topics))):
            for j in list(range(len(sentiments))):
                if sentence_topics[i][0] == sentiments[j][0]:
                    collected = collected + [[sentencelist[sentence_topics[i][0]]] + 
                                             [sentiments[j][1]['compound']] + 
                                              [sentiments[j][1]['neg']] +
                                               [sentiments[j][1]['neu']] + 
                                                [sentiments[j][1]['pos']] +
                                                 [sentence_topics[i][1]]]
        
        for i in list(range(len(collected))):
            row_insert = (str(collected[i][1]*vote), collected[i][5], loc, str(vote), 
                          str(collected[i][1]), collected[i][0], source, sentenceclean, item)
            print(row_insert)
            #comment_score, topic, location, vote, sentiment, sentence, source, orig_comment, comment_id
            cur2.execute("""INSERT INTO final_table VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);""", row_insert)
            conn.commit()
         
    conn.close()


file_process(0,10)


