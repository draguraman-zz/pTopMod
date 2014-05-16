#import logging
#logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
from gensim import corpora,models,similarities
from fp_growth import find_frequent_itemsets
import re
#from stemming.porter2 import stem
from nltk.stem import SnowballStemmer 
from itertools import chain
import nltk
#from nltk.corpus import europarl
from nltk.probability import LidstoneProbDist, WittenBellProbDist
import powerlaw
import glob
from nltk.model.ngram import NgramModel
import codecs
import string
estimator = lambda fdist, bins: LidstoneProbDist(fdist, 0.2)

#aux functions
def flatten(listOfLists):
    "Flatten one level of nesting"
    return list(chain.from_iterable(listOfLists))
#brown = nltk.corpus.brown

#determine training data fromlarge files
#diction with 

#lala="If quality is what we care about, then why do we distinguish between small and large producers"
#lal=" ".join([stem(word.lower()) for word in lala.rstrip(',').split()])
#print lal
#print lm.prob("vot",[lal])
languageMappingList=["fr","de"]
languageMapping={"en":"english","de":"german","da":"danish","fi":"finnish","hu":"hungarian","fr":"french","nl":"dutch","it":"italian","sv":"swedish","pt":"portuguese","es":"spanish"}
#with open("./langs","r") as f:
#	langs=f.readlines()
for lang in languageMappingList:
	print lang
	line_list=[]
	files=glob.glob("./allLangFiles/*.txt_"+str(lang))
	print "Files loaded"
	for file in files:
		for line in codecs.open(file,'r',encoding='utf-8'):
			line_list.extend(re.split(';.?',line.rstrip()))
	with codecs.open('./stopwords/'+str(lang), 'r',encoding='utf-8') as stoplist_file:
	    content = stoplist_file.read()
	print "Starting stop list processing "    
	stoplist = set(content.split())
	print stoplist

	#removal of stop words
	#punct='!\"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~' 
	#line_list_swr = [[word for word in re.split('\W+',document_line) if word not in stoplist]for document_line in line_list]

	line_list_swr = [[word for word in document_line.lower().split() if word not in stoplist]for document_line in line_list]
    
	#stemming these words #[stem(word) for sentence in documents for word in sentence.split(" ")]
	#g=[lambda alist: stem(word) for word in alist]
	print "starting stemming"
	line_list_swr_stem= [[SnowballStemmer(languageMapping[lang]).stem(list_item)for list_item in title] for title in line_list_swr] # (lambda alist: [stem(word) for word in alist]) for alist in blist
	#removing words that occur only once
	print "stemming done"
	#all_tokens = sum(line_list_swr_stem, [])
	#print "removing words with counts 1"
	#print "Freq thresholding pruning"
	#tokens_once = set(word for word in set(all_tokens) if all_tokens.count(word) == 1)
	#line_list_swr_stem_ofwr= [[word for word in text if word not in tokens_once]for text in line_list_swr_stem] #OneFrequencyWordRemoved
	print "Freq thresholding pruning done"
	line_list_swr_stem_ofwr= line_list_swr_stem
	#print "Generating token dictionary"
	#token_dictionary = corpora.Dictionary(line_list_swr_stem_ofwr)
	#token_dictionary.save('./dicts/token_'+lang+'.dict')
	#print(token_dictionary.token2id)

	print "Frquent Pattern Mining Phase"
	#trainFileName_lang={}
	#with open("./training_filenames","r") as f:
		#for line in f.readlines():
			#trainFileName_lang[line.split()[0]]=line.split()[1]
	#f = codecs.open("./allLangFiles/"+str(trainFileName_lang[lang]),'r',encoding='utf-8')
	#filewords=f.read()
	#corpus = [SnowballStemmer(languageMapping[lang]).stem(word) for word in re.split(';.?',filewords)]
	#train=corpus
	#fdist = nltk.FreqDist(w for w in corpus)
	#vocabulary = set(map(lambda x: x[0], filter(lambda x: x[1] >= 5, fdist.iteritems())))
	#train = map(lambda x: x if x in vocabulary else "*unknown*", train)
	#estimator = lambda fdist, bins: LidstoneProbDist(fdist, 0.2) 
	#lm2 = NgramModel(2, train, estimator=estimator)
	#lm3=NgramModel(3, train, estimator=estimator)
	g = codecs.open('./fpg'+"_"+str(lang)+".txt",'w',encoding='utf-8')
	frequent_pattern_list=[]
	for itemset,support in find_frequent_itemsets(line_list_swr_stem_ofwr,100,True):
		#if len(itemset)== 2 :
			#print (lm2.prob(itemset[0],itemset[1:])
			#print str(itemset[0])+' ####'+str(itemset[1:])
		for item in itemset:
			g.write(item+" " )
		g.write(': ' + str(support)+' \n')
		#elif len(itemset)== 3 :
			#print (lm3.prob(itemset[0],itemset[1:])
			#print str(itemset[0])+' ####'+str(itemset[1:])
		#	g.write(str(itemset) + ' : ' + str(support)+' \n' ) # + str(lm3.prob(itemset[0],itemset[1:]))+' \n')
		#else: 
		#	g.write(str(itemset) + ' : ' + str(support)+' \n' )
		#frequent_pattern_list.append(str(itemset))
	#dictionary = corpora.Dictionary(frequent_pattern_list)
	#corpus = [dictionary.doc2bow(text) for text in frequent_pattern_list]
	#lda = gensim.models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=10, update_every=1, chunksize=10000, passes=1)

	
	#lm3= NgramModel(3, train, estimator=estimator)
	#lm4=NgramModel(4, train, estimator=estimator)



