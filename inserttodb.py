import pyodbc
from pbkdf2 import PBKDF2

server = 'mynewserver-20180328.database.windows.net'
database = 'assignment1'
username = 'ServerAdmin'
password = 'sec!!7749'
driver= '{ODBC Driver 17 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

salt = "seclab"   

# with open("dictionaries/passwords.txt") as f:
with open("dictionaries/english.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

#calculate hash and store to db for every pw

#for i in range(0,1000):
for i in range(len(content)):
    try:
        thiscontent = content[i]
        key = PBKDF2(thiscontent, salt, 500).hexread(16)
       
        # "INSERT INTO [dbo].[Hashes]([Plaintext],[Hash])VALUES('Qwerty12','aaaaaaaaa')"
        query = "INSERT INTO [dbo].[Hashes]([Plaintext],[Hash])VALUES('"
        query = query + thiscontent + "','" + key + "')"
        cursor.execute(query)
        #print(key)
    except:
        continue
         
 



#cursor.execute("INSERT INTO [dbo].[Hashes]([Plaintext],[Hash])VALUES('Qwerty12','aaaaaaaaa')")
cnxn.commit()
cnxn.close()

f.close()
