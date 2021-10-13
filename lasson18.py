students = {"garo": 5,
            "karo": 10,
            "hamo": 15,
            "gago": 20,
            "tiko": 25,
            "arno": 30,
            "narek": 35}


# for i in students:
# 	if students[i]>15:
# 		print(i,students[i])

# k= 0
# l= 0

# for i in students.values():
# 	k+=i
# 	l+=1

# print(k/l)



# anun = input()

# if anun in students:
# 	print(anun, "ka")
# else:
# 	print(anun, "chka")


s = 'a,2,b,5,c,8,a,4,e,11'.split(",")
thisdict = {}
for i in range(0,len(s),2):
	if s[i] in thisdict:
		thisdict[s[i]]+=int(s[i+1])
		
	else:
		thisdict[s[i]]=int(s[i+1])
	


# print(thisdict)

# word = "exercises"

# thisdict = {}

# for i in word:
#     thisdict[i]=word.count(i)

# print(thisdict)


# old_list = [{'key1':'value1'},{},{},{'key1':'value1'},{'key2':'value2'}]


# thisdict = []

# for i in old_list:
# 	if i not in thisdict:
# 		thisdict.append(i)

# print(thisdict)







