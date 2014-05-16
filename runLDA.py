import gensim
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

for lang in ["en"]:
	corpus=gensim.corpora.bleicorpus.BleiCorpus(lang+"_tfidf",lang+"_vocab")
	#print corpus.dictionary
	#print corpus
	#print corpus.docbyoffset(0)
	lda=gensim.models.ldamodel.LdaModel(corpus,num_topics=20,alpha='auto',iterations=1000, passes=2, eval_every=1,update_every=1,chunksize=10)
	#tfidf=gensim.models.tfidfmodel.TfidfModel(corpus)
	#tfidf.save("./en.tfidf")
	#print lda.num_topics
	#lda.update(corpus)
	for topic in lda.print_topics(topics=-1,topn=10):
		print topic
	#for i in range(0,lda.num_topics-1):
	#	lda.print_topics(i)
	#lda.show_topics(topics=-1,topn=10,log=False,formatted=False)
	#corpus_lda = lda[corpus]
	#for doc in corpus_lda: print doc
