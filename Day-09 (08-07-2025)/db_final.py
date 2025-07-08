import mysql.connector

def padL(data, width):
    buf = str(data)
    for i in range(len(buf),width):
        buf = buf + ' '
    return buf

def padC(data, width):
    buf = str(data)
    for i in range(len(buf),width):
        if(i%2==0):
            buf = buf + ' '
        else:
            buf = ' ' + buf
    return buf

def padR(data, width):
    buf = str(data)
    for i in range(len(buf),width):
        buf = ' ' + buf
    return buf

def replicate(whichChar, times):
    buf = ''
    for i in range(0,times):
        buf = buf + whichChar
    return buf

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'root',
    database = 'gift3sem'
)

curs = conn.cursor()
curs.execute("SELECT c.con_id,c.con_name,c.mobile_no,l.loc_name,r.rel_name FROM contact AS c LEFT JOIN location AS l ON c.loc_id=l.loc_id LEFT JOIN relation AS r ON c.rel_id=r.rel_id")

list = ((4,'ID','C'),(30,'CONTACT-NAME','L'),(12,'MOBILE-NO','C'),(20,'RELATION','L'),(20,'LOCATION','L'))

print('+',end='')
for index, item in enumerate(list):
    print(replicate('-',item[0]),end='+')
print()

print('|',end='')
for index, item in enumerate(list):
    print(padC(item[1],item[0]),end='|')
print()

print('+',end='')
for index, item in enumerate(list):
    print(replicate('-',item[0]),end='+')
print()

for row in curs:
    print('|',end='')
    for index, col in enumerate(row):
        list_index = list[index]
        width = list_index[0]
        padtype = list_index[2]
        if padtype=='L':
            print(padL(col,width), end='|')
        elif padtype=='C':
            print(padC(col,width), end='|')
        elif padtype=='R':
            print(padR(col,width), end='|')
    print()

print('+',end='')
for index, item in enumerate(list):
    print(replicate('-',item[0]),end='+')
print()

conn.close()
