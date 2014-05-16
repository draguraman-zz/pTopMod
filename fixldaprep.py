with open("en_2") as f:
	for line in f:
		subtract=0
		words=line.split()
		for word in words[1:]:
			fields=word.split(':')
			if int(fields[1]) == 0:
				subtract+=1 
		print str(int(words[0])-subtract),
		for word in words[1:]:
			print word,
		print ""