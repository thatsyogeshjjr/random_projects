import time

s = input("String: ")
st = []

for i in s:
    st+=i

print("original list:",st)

for i in range(0,len(s)):
    if st[i] != " ":
        st[i] = "*"
    # convert list into word
    a = ''.join(str(i) for i in st)

    # print the word
    print("\r"+a,end="")
    time.sleep(0.2)

time.sleep(1)
print("\n\n"+st)
