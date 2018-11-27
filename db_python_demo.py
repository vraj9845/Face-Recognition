import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="Vraj",
  passwd="root@123",
  database="pyDB1"
)

thisdict =	{
  "TOTAL" : "0",
  "Vraj": "0",
  "Srikar": "0",
  "Sreejit": "0",
  "Suraj": "0",
  "Soha": "0"
}



lines = []             # Declare an empty list named "lines"
with open ('attendance.txt', 'rt') as in_file:  # Open file lorem.txt for reading of text data.
    for line in in_file:   # For each line of text in in_file, where the data is named "line",
        if line not in in_file:
            lines.append(line)     # add that line to our list of lines.
    for y in lines:
         print(y)


    for element in lines:  # For each element in our list,
        thisdict.update({element: "1"})
    for x in thisdict:
      print(thisdict[x])



mycursor = mydb.cursor()

sql = "INSERT INTO student (name,value) VALUES (%s,%s)"
val = ("Sreejit","1")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

print(mycursor.execute("SELECT * FROM student"))

myresult = mycursor.fetchall()
print(myresult)




