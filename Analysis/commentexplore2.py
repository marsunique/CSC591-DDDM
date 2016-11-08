# MUST DOWNLOAD PUNKT, AVG_perceptron, tagsets(?), maxent_treebank, stopwords, 
# brown Corpus, corpora_worldnet
 
#nltk.download()

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

def combine_comment_files(start):
    i = start
    input_path= 'C:/Users/Tim Sawicki/Documents/Python Scripts/output/'
    comment_path = Path(input_path + str(i) + ' comments.txt')
    with open(input_path + 'combinedfile.txt', 'w') as outfile:
        while comment_path.is_file():
            with open(input_path + str(i) + ' comments.txt') as infile:
                for line in infile:
                    outfile.write(line)
            infile.close()
            i = i+1
            comment_path = Path(input_path + str(i) + ' comments.txt')
    outfile.close()
    return()
    
combine_comment_files(1)




input_path= 'C:/Users/Tim Sawicki/Documents/Python Scripts/title grab/'
textfile = open(input_path + 'COMBINED.txt','r')
commentlist = textfile.readlines()
textfile.close()









stopwordlist = stopwords.words('english')
lemmatizer = WordNetLemmatizer()
p_stemmer = PorterStemmer()
pos_list = ['NN','VB','NNS']





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
wordlist = loop_on_tokenized(wordlist,lowercase)
wordlist = loop_on_tokenized(wordlist,stopwords)
wordlist = loop_on_tokenized(wordlist,fix_contractions,False)
wordlist = loop_on_tokenized(wordlist,is_url)
#wordlist = loop_on_tokenized(wordlist,lemmatize_func)                          

wordlist = pos_finder(wordlist)                        
wordlist = loop_on_tokenized(wordlist,pos_filter) 
wordlist = clear_empty(wordlist)                









#--------------------------------ANALYSIS-------------------------------------

#SENTIMENT
sentence_path= 'C:/Users/Tim Sawicki/Documents/Python Scripts/output/'
textfile = open(sentence_path + '1 comments.txt','r')
raw_sentences = textfile.readlines()
textfile.close()
rawsentences = strip_tags(raw_sentences)                          
rawsentences = sentences(rawsentences)
rawsentences = unnest_sentences(rawsentences)
sentiments = []
for sentence in rawsentences: 
    vs = vaderSentiment(sentence)
    sentiments = sentiments +  [(sentence, vs)]




# BASIC FREQUENCY ANALYSIS
wordlist2 = make_single_list(wordlist)
freq = nltk.FreqDist(wordlist2)
print(freq.most_common(250))


# COLLOCATIONS - requires wordlist2
#bigram_measures = nltk.collocations.BigramAssocMeasures()
#trigram_measures = nltk.collocations.TrigramAssocMeasures()
#finder = BigramCollocationFinder.from_words(wordlist2)
#finder2 = TrigramCollocationFinder.from_words(wordlist2)
#finder.nbest(bigram_measures.likelihood_ratio,50)
#finder2.nbest(trigram_measures.likelihood_ratio,50)



# Topic extraction (from manually-combed text file) and bigram filter
topic_path= 'C:/Users/Tim Sawicki/Documents/Python Scripts/'
textfile = open(topic_path + 'topics.txt','r')
topics = textfile.readlines()
textfile.close()
topics = strip_tags(topics) 
bigram_measures = nltk.collocations.BigramAssocMeasures() 
bigram_list = [] 
for i in topics:
    finder = BigramCollocationFinder.from_words(wordlist2)
    finder.apply_ngram_filter(lambda w1, w2: i not in (w1, w2))
    for j in finder.score_ngrams(bigram_measures.likelihood_ratio)[0:3]:
        bigram_list = bigram_list + [j[0]]

sentence_topics = []
for i in bigram_list:
    for j in wordlist:
        if i[0] in j and i[1] in j:
            sentence_topics = sentence_topics + [[j,i]]
    
d = defaultdict(int)
for i in sentence_topics:
        d[i[1]] += 1        



# LDA MODEL
dictionary = corpora.Dictionary(wordlist)
corpus = [dictionary.doc2bow(text) for text in wordlist]        
ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=50, id2word = dictionary, passes=50)    
print(ldamodel.print_topics(num_topics=50, num_words=10))

# WORD2VEC MODEL
model = gensim.models.Word2Vec(wordlist, size=100, window=3, min_count=50, workers=4)
#model.most_similar(positive=['vote','trump']) 

model.most_similar(positive=['clinton','lies'])
model.most_similar(negative=['obamacare'])

  
#nltk.word_tokenize(commentslist.translate(dict.fromkeys(string.p‌​unctuation)))