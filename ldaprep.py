import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
from gensim import corpora,models,similarities
#from fp_growth import find_frequent_itemsets
import re
#from stemming.porter2 import stem
from nltk.stem import SnowballStemmer 
from itertools import chain
import nltk
#from nltk.corpus import europarl
from nltk.probability import LidstoneProbDist, WittenBellProbDist
#import powerlaw
import glob
import codecs
from collections import defaultdict


languageMappingList=["en"]
languageMapping={"en":"english","de":"german","da":"danish","fi":"finnish","hu":"hungarian","fr":"french","nl":"dutch","it":"italian","sv":"swedish","pt":"portuguese","es":"spanish"}
#with open("./langs","r") as f:
#	langs=f.readlines()
for lang in languageMappingList:
	#print lang
	fps_dict={}
	i=1
	with codecs.open('./fpg_'+str(lang)+".txt",'r',encoding='utf-8') as fps:
		for line in fps:
			#print line
			line=((line.split(':')[0]).strip()).split()
			if fps_dict.get(frozenset(line),0)==0:
				fps_dict[frozenset(line)]=i
				i=i+1
	
	content=[]
	with codecs.open('./stopwords/'+str(lang), 'r',encoding='utf-8') as stoplist_file:
		    content = stoplist_file.read()
	stoplist = set(content.split())
	#for w in sorted(fps_dict,key=fps_dict.get):
	#	print w,fps_dict[w]
	files=glob.glob("./allLangFiles/*.txt_"+str(lang))
	#print "Files loaded"
	for file in files:
		line_list=[]
		for line in codecs.open(file,'r',encoding='utf-8'):
			line_list.extend(re.split(';,.?',line.rstrip()))
		

		#print "Starting stop list "    
		
		#removal of stop words
		line_list_swr = [[word for word in document_line.lower().split() if word not in stoplist]for document_line in line_list]

		#stemming these words #[stem(word) for sentence in documents for word in sentence.split(" ")]
		#g=[lambda alist: stem(word) for word in alist]
		#print "starting stemming"
		line_list_swr_stem= [[SnowballStemmer(languageMapping[lang]).stem(list_item)for list_item in title] for title in line_list_swr] # (lambda alist: [stem(word) for word in alist]) for alist in blist
		#removing words that occur only once
		#print "stemming done"
		#all_tokens = sum(line_list_swr_stem, [])
		#print "removing words with counts 1"
		#tokens_once = set(word for word in set(all_tokens) if all_tokens.count(word) == 1)
		#line_list_swr_stem_ofwr= [[word for word in text if word not in tokens_once]for text in line_list_swr_stem] #OneFrequencyWordRemoved
		line_list_swr_stem_ofwr= line_list_swr_stem
		pattern_counts=defaultdict(int)
		for pattern in fps_dict:
			for line in line_list_swr_stem_ofwr:
				if(pattern).issubset(frozenset(line)):
					pattern_counts[pattern]+=1
		unique_terms=0
		for pattern in fps_dict:
			if pattern_counts[pattern]>0:
				unique_terms+=1
		print unique_terms,
		#print str(len(fps_dict)),
		for w in sorted(fps_dict,key=fps_dict.get, reverse=False):
			if pattern_counts[w]>0:
				print str(fps_dict[w])+":"+str(pattern_counts[w]),

		

	for w in sorted(fps_dict,key=fps_dict.get, reverse=False):
			print w

			#	if len(line)<len(line_list_swr_stem_ofwr):
			#		continue
			#	for i in range(0,len(line)):
			#		if line[i:i+len(line_list_swr_stem_ofwr)-1]==line_list_swr_stem_ofwr
