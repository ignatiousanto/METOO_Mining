###tweet classifier
import pickle
import os

load_data = pickle.load( open( "save.p", "rb" ) )


assault_flag=[]
for i in range(len(loaddata[0])):
	print(loaddata[0][i])
	input_flag = raw_input(loaddata[0][i]+"\n")
	if input_flag=="1" :
		assault_flag[i]=1
	elif input_flag =="2":
		assault_flag[i] = 0
	else :
		print("choose 1 for assault choose 2 for something else")

pickle.dump( [cleaned_body,assault_flag,l_o_links,l_o_refs,l_o_hashtags], open( "Labelled_data.p", "wb" ) )

