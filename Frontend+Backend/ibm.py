import ibm_db
import ibm_db_dbi
# Connect to DB2
conn_str='database=BLUDB;hostname=dashdb-txn-sbox-yp-dal09-08.services.dal.bluemix.net;port=50000;protocol=tcpip;uid=dps35835;pwd=PleaseGoCovid19@2020'
ibm_db_conn = ibm_db.connect(conn_str,'','')
conn = ibm_db_dbi.Connection(ibm_db_conn)


# conn.tables('DPS35835', 'EMPLOYER')

select="select * from EMPLOYER"
cur = conn.cursor()
cur.execute(select)
row = cur.fetchall()
print("Initial values in EMPLOYER table")
for i in row:
	print(i)


u = int(input("Enter new USER_ID: "))
name = input("Enter new COMPANY_NAME: ")
si = input("Enter new COMPANY_SIZE: ")
pos = input("Enter new POSITION: ")
sec = input("Enter new SECTOR: ")
sec_type = int(input("Enter new SECTOR_TYPE: "))
web = input("Enter new WEBSITE: ")


insert = "insert into EMPLOYER values(?,?,?,?,?,?,?)"
params = (u,name,si,pos,sec,sec_type,web)

stmt_insert = ibm_db.prepare(ibm_db_conn, insert)
ibm_db.execute(stmt_insert,params)

select="select * from EMPLOYER"
cur = conn.cursor()
cur.execute(select)
row = cur.fetchall()
print("Final values in EMPLOYER table")
for i in row:
	print(i)


# name = request.form.get('name')
# email = request.form.get('mail')
# insert = "insert into EMPLOYER values(?,?,?,?,?,?,?)"
# params = (u,name,si,pos,sec,sec_type,web)