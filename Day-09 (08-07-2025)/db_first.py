import mysql.connector;

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'root',
    database = 'gift3sem'
);

curr = conn.cursor()
curr.execute("SELECT c.con_id,c.con_name,c.mobile_no,l.loc_name,r.rel_name FROM contact AS c LEFT JOIN location AS l ON c.loc_id=l.loc_id LEFT JOIN relation AS r ON c.rel_id=r.rel_id")

for row in curr:
    for col in row:
        print(col,end='  ')
    print()
