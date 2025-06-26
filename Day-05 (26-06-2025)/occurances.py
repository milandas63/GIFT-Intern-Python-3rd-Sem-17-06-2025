text = input("Enter some text: ")

totlist = []
for i in range(0,26):
    totlist.append(0)
print(totlist)

for i in text:
    asc = ord(i)
    if asc>=65 and asc<=90:
        totlist[asc-65] += 1
    elif asc>=97 and asc<=122:
        totlist[asc-97] += 1

for i in range(0,len(totlist)):
    if totlist[i]>0:
        print(chr(i+65), "=", totlist[i])
