import time

n_star=5
try:
	while True:
		print("Looking for devices "+"."*n_star)
		if n_star <= 5:
			n_star +=1
		else:
			n_star = 1
		time.sleep(1)
except KeyboardInterrupt:
	print("\n[-] Exiting")
