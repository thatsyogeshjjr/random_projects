n = input("Enter number: ")
if n:	
	n = int(n)
	for i in range(0,n+1):
		print(i,end=" ")
else:
	print("[-] An Error occured. Bad input!")
