#!/usr/bin/env Python3

def rect(l=9,b=1):
	print("="*l)
	for i in range(b):
		print("="+" "*(l-2)+"=")
	print("="*l)

rect()

