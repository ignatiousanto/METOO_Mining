import pickle

body= pickle.load(open( "body.p", "rb" ))
print(len(body))
body = list(set(body))
print(len(body))

l_o_ass = []

keywords= ["i was","yr", "yrs" "year","years" ]
for i in range(len(body)):
    if any(x in body[i].lower() for x in keywords):
        l_o_ass.append(body[i])

print(len(l_o_ass))

assault_flag=[]
for i in range(len(l_o_ass)):
	input_flag = input(l_o_ass[i]+"\n")
	if input_flag=="1" :
		assault_flag.append(1)
	elif input_flag =="2":
		assault_flag.append(0)
	else :
		print("choose 1 for assault choose 2 for something else")

pickle.dump( [l_o_ass, assault_flag], open( "Labelled_data.p", "wb" ) )
