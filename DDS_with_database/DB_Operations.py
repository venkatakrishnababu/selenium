#insert,update,delete
insert="insert into student values(104,'kim')"
update="update student set sname='Msys' where sid=102'
delete="delete from student where sid=102"
import mysql.connector
###Connect to the data base
con=mysql.connector.connect(host="localhost",port=3306,user="root",database="mydb")
#create cursor
curs=con.cursor()
##execute query through cursor
curs.execute(insert)
####commit transaction
con.commit()
#close the transaction
con.close()


