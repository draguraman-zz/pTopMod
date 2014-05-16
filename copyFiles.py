import shutil

for line in open("filelist.txt","r"):
	root=line
	#root=line.split("_")[0]
	shutil.copy("/home/pratik/Downloads/txt/es/"+root,"./allLangFiles/"+root+"_es")