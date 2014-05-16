import codecs
import numpy
from random import shuffle
for lang in ["fr"]:
	
	f=open(lang+"_mallet","w")
	
	with open(lang+"_tfidf",'r') as l:
		for line in l:
			file_sequence=[]
			for word in line.split()[1:]:
				fields=word.split(':')
				for i in range(int(fields[1])):
					file_sequence.append(fields[0])

			shuffle(file_sequence)
			for word in file_sequence:
				f.write(word+" ")

			f.write("\n")	
			#while total_count!=0:
			#	index=numpy.random_integers(1,max_index)
			#	if pattern_counts.get(index,0)==0:
			#		continue

			#	f.write(index)

