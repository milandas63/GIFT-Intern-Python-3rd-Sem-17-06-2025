start = 2
end = 40

for i in range(start, end+1, 5):
    for j in range(1, 11):
        for k in range(i, i+5):
            if k>end:
                break
            print(str(k).rjust(2),'x',str(j).rjust(2),'=',str(j*k).rjust(3),'  ', end='')
        print()
    print()
print()
