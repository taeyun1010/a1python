import pip

def install(package):
    pip.main(['install', package])

# Example
install('pyodbc')

import pyodbc


server = 'mynewserver-20180328.database.windows.net'
database = 'assignment1'
username = 'ServerAdmin'
password = 'sec!!7749'
driver= '{ODBC Driver 17 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
#cursor.execute("SELECT TOP 20 pc.Name as CategoryName, p.name as ProductName FROM [SalesLT].[ProductCategory] pc JOIN [SalesLT].[Product] p ON pc.productcategoryid = p.productcategoryid")
# cursor.execute("SELECT TOP (1000) [Plaintext],[Hash] FROM [dbo].[Hashes]")


# 
# cursor.execute("SELECT [Plaintext] FROM [dbo].[Hashes] h WHERE [Hash] = 'c99290aefb4180683226def6a9ee58bf'")

# row = cursor.fetchone()
# while row:
#     #print (str(row[0]) + " " + str(row[1]))
#     print (str(row[0]))
#     row = cursor.fetchone()
      
     
with open("hashedPasswords.txt") as f:
#with open("Yahoo_accounts_md5_rainbowtable.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

filetowrite = open("Passwords.txt","w")

counter = 1;
for i in range(len(content)):
    thiscontent = content[i]
    #for split in thiscontent.split(":"):
    split = thiscontent.split(":")
    #print("split len = " + str(len(split)))
    hash = split[(len(split) - 1)]
    hash = "'" + hash + "'"
    query = "SELECT [Plaintext] FROM [dbo].[Hashes] h WHERE [Hash] = " 
    query = query + hash
    cursor.execute(query)
    row = cursor.fetchone()
    
    while row:
        #print (str(row[0]) + " " + str(row[1]))
        print (str(row[0]))
        filetowrite.write(str(counter) + ":" + split[1] + ":" + row[0] + "\n")
        row = cursor.fetchone()
        counter = counter + 1
#     print ("hash = " + hash)
#     print("thiscontent = " + thiscontent)

f.close()
filetowrite.close()