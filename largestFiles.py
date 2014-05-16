import glob
import os
with open("./langs") as f:
	for line in f:
		lang=line.rstrip()
		largestFile=""
		largestFileSize=0
		for file in glob.glob("./allLangFiles/*.txt_"+str(lang)):
			statinfo=os.stat(file)
			if statinfo.st_size>largestFileSize:
				largestFileSize=statinfo.st_size
				largestFile=file
		print largestFile