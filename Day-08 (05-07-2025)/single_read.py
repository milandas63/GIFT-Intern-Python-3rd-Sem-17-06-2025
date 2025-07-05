# Reading one-by-one character from the file
try:
    with open("personal-data.txt", "r") as r:
        for i in iter(lambda : r.read(1), ""):
            print(i)
except Exception as e:
    print("There is an error",e)
