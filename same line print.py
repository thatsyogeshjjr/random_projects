import time

i=0

try:
    while True:
	    print("\r[+] Packets Sent: "+str(i),end="")
	    i+=2
	    time.sleep(0.5)
except KeyboardInterrupt:
    print("\n[+] Quitting ...")
