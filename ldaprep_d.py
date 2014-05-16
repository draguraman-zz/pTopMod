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


languageMappingList=["de"]
languageMapping={"en":"english","de":"german","da":"danish","fi":"finnish","hu":"hungarian","fr":"french","nl":"dutch","it":"italian","sv":"swedish","pt":"portuguese","es":"spanish"}

for lang in languageMappingList:
	
	fps_dict={}
	i=1
	with codecs.open('./fpg_'+str(lang)+".txt",'r',encoding='utf-8') as fps:
		for line in fps:
			
			line=((line.split(':')[0]).strip()).split()
			if fps_dict.get(frozenset(line),0)==0:
				fps_dict[frozenset(line)]=i
				i=i+1
	
	content=[]
	with codecs.open('./stopwords/'+str(lang), 'r',encoding='utf-8') as stoplist_file:
		    content = stoplist_file.read()
	stoplist = set(content.split())

	f=open("filelist.txt","r")
	files=f.readlines()
	f.close()
	files=["./allLangFiles/"+file.strip()+"_"+str(lang) for file in files]
	#files=glob.glob("./allLangFiles/*.txt_"+str(lang))
	f=codecs.open(lang,"w",encoding="utf-8")
	
	for file in files:
		line_list=[]
		f1=codecs.open(file,'r',encoding='utf-8')
		for line in f1:
			line_list.extend(re.split(';,.?',line.rstrip()))

		f1.close()
		
		line_list_swr = [[word for word in document_line.lower().split() if word not in stoplist]for document_line in line_list]

		
		line_list_swr_stem= [[SnowballStemmer(languageMapping[lang]).stem(list_item)for list_item in title] for title in line_list_swr] # (lambda alist: [stem(word) for word in alist]) for alist in blist
		
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
		
		
		f.write(str(unique_terms))
		
		for w in sorted(fps_dict,key=fps_dict.get, reverse=False):
			if pattern_counts[w]>0:
				f.write(" "+str(fps_dict[w])+":"+str(pattern_counts[w]))

		f.write("\n")
		
	f.close()
	f=codecs.open(lang+"_vocab","w",encoding="utf-8")
	for w in sorted(fps_dict,key=fps_dict.get, reverse=False):
		f.write(str(w))
		f.write("\n")

	f.close()

			
