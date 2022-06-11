from math import factorial
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="attendance",
  port=3307
)

# mycursor = mydb.cursor()
# sql="SELECT * FROM `administrator`"
# addclass=mycursor.execute(sql)
# # myresult = mycursor.fetchall()
# print(addclass)
# mydb.close()

# mycursor = mydb.cursor()
# checkUserNamesql = 'SELECT * FROM classsec '
# mycursor.execute(checkUserNamesql)
# myresult = mycursor.fetchall()
# print(myresult)
# for row in myresult:
#     print(str(row[0]))


# sql="select name from teams"
# f=mydb.execute(sql)
# print(f)
# for row in cur:
#     print(str(row[0]))

#  self.takeattendance.clicked.connect.stackedWidget.setCurrentwidget(self.page_2)


# slist=(6, 'ASHA PAL')
# print(slist[0])

# slist=["(4, 'ANIMESH BAGCHI')", "(5, 'ROHIT MALLIK')"]
# print(slist[0][0])
# laura=map(tuple(),)
# print(laura)
lastteacher="select username from teacherloggedin order by username limit 1"
teachercursor=mydb.cursor()
teachercursor.execute(lastteacher)
solved=list(teachercursor.fetchone())[0]
print(solved)


teachername="select first_name,last_name from faculty where username='"+solved+"' "
teachercursor.execute(teachername)
firstlast=list(teachercursor.fetchone())
firstlast=firstlast[0]+" "+firstlast[1]
print(firstlast)