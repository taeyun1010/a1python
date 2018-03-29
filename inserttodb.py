import pyodbc
from pbkdf2 import PBKDF2

server = 'mynewserver-20180328.database.windows.net'
database = 'assignment1'
username = 'ServerAdmin'
password = 'sec!!7749'
driver= '{ODBC Driver 17 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
cursor.execute("INSERT INTO [dbo].[Hashes]([Plaintext],[Hash])VALUES('Qwerty12','aaaaaaaaa')")
cnxn.commit()
cnxn.close()
