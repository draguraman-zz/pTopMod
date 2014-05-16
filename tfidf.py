from math import log
import copy
f=open("en","r")
idf_dict={}
tfidf=[]
original_tokens=[[]]
num_docs=0
for line in f:
	num_docs+=1
	original_tokens.append(line.split())
	tf_dict={}
	total_count=0
	max_freq=0
	for word in line.split()[1:]:
		fields=word.split(':')
		idf_dict[fields[0]]=idf_dict.get(fields[0],0)+1
		tf_dict[fields[0]]=fields[1]
		total_count+=int(fields[1])
		if max_freq<fields[1]:
			max_freq=fields[1]
	for key in tf_dict:
		tf_dict[key]=(0.5+((0.5*int(tf_dict[key])/int(max_freq))))
	tfidf.append(copy.deepcopy(tf_dict))
for key in idf_dict:
	idf_dict[key]=log(idf_dict[key],2)
f.close()
dic_index=1
#print original_tokens[1]
f1=open("en_tfidf","w")
for dic in tfidf:
	for key in dic:
		dic[key]=dic[key]*idf_dict[key]
	sorted_dic_list=sorted(dic,key=dic.get,reverse=True)
	sorted_dic_list=sorted_dic_list[0:int(0.95*(len(sorted_dic_list)))]
	line=original_tokens[dic_index]
	dic_index+=1
	
	f1.write(str(len(sorted_dic_list)))
	for word in line[1:]:
		fields=word.split(':')
		if fields[0] in sorted_dic_list:
			f1.write(" "+word)
	f1.write("\n")		
f1.close()
