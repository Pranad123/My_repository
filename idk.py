import mysql.connector
a = mysql.connector.connect(host="localhost", user="root", passwd="w0wm0m0", database="pranad")
b = a.cursor()
b.execute("select * from shuper")
f = open("photo", 'a')
for i in b:
   print(i)
