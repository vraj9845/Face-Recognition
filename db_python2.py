import sys
import mysql.connector
import datetime

now = datetime.datetime.now()

print(now.strftime("%d-%m-%Y"))
DATE = now.strftime("%d-%m-%Y")

fp = open('attendance.txt','rt')
data = fp.read()
words = data.split()
fp.close()

unwanted_chars = "%.,-_ ()1234567890 "
wordfreq = {}
for raw_word in words:
    word = raw_word.strip(unwanted_chars)
    if word not in wordfreq:
        wordfreq[word] = 0 
    wordfreq[word] = 1

print(wordfreq)

print()
print()

SUBJECT_CODE = {
  "15CS51": "ME",
  "15CS52": "CN",
  "15CS53": "DBMS",
  "15CS54": "ATC",
  "15CS551": "AI",
  "15CS552": "OOMD",
  "15CSL51": "CN_LAB",
  "15CSJ52": "DBMS_LAB"
}
print()
print(SUBJECT_CODE)
print()
code = input("Enter Subject_code ")
print()
p = SUBJECT_CODE[code]
print(p + "," + code + "\tis selected!\n")
print()

thisdict =	{
  "TOTAL:" : "0",
  "Vraj:": "0",
  "Srikar:": "0",
  "Sreejit:": "0",
  "Suraj:": "0",
  "Soha:": "0"
}

otherdict = {
   "TOTAL:" : "1PE16CS000",
  "Vraj:": "1PE16CS179",
  "Srikar:": "1PE16CS161",
  "Sreejit:": "1PE16CS160",
  "Suraj:": "1PE16CS164",
  "Soha:": "1PE16CS157"
}

for x in wordfreq:  # For each element in our list,
	for y in thisdict:
		if y == x:
			thisdict[y] = 1
			
for w, v in thisdict.items():
  print(w, v)


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root@123",
  database="ATTENDANCESYSTEM"
)

mycursor = mydb.cursor()
sql = "INSERT INTO ATTENDS (USN,SUBJECT_CODE,DATE,ATTEND_VALUES) VALUES (%s,%s,%s,%s)"
#val = ("16CS160", "Sreejit","1")
for s,t in thisdict.items():
	if t == 1:
		for d,e in otherdict.items():
			if d == s:
				val  = e,code,DATE,'1'
				mycursor.execute(sql, val)
				mydb.commit()
				print(mycursor.rowcount, "record inserted.")

#mycursor.execute("SELECT * FROM student where name='TOTAL:'")
mycursor.execute("SELECT COUNT(*) FROM ATTENDS where USN='1PE16CS000'")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)










