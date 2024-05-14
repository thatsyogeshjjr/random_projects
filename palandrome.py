#!/usr/bin/env Python3

# string is Palandrome
st = input("String> ")
stj= st[::-1]
#for i in st[::-1]:
#	stj.append(i)

print("index\tword1\tword2")
for i in range(0,len(stj)):
	print(i,"\t",st[i],"\t",stj[i])

if st == st[::-1]:
	print("Palandrome")
else:
	print("Not Palandrome")
