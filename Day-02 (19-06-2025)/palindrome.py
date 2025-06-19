spaces = 40

for i in range(0,10):
    for j in range(0,spaces):
        print(' ',end='')
    for j in range(1,i+1):
        print(j,end='')
    for j in range(i-1,0,-1):
        print(j,end='')
    print()
    spaces = spaces-1
