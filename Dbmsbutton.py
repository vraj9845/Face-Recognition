import sys
import os
import tkinter as tk
import tkinter.messagebox
top=tkinter.Tk()

frame = tk.Frame(top)
frame.pack()


def FaceRecognition():
    os.system('python3 recognize_video.py --detector face_detection_model --embedding-model openface_nn4.small2.v1.t7 --recognizer output/recognizer.pickle --le output/le.pickle')
def AttendanceEntryInDB():
    os.system('python3 db_python2.py')

B1=tkinter.Button(top,text="Face_Recognition",command= FaceRecognition)
B1.pack()
B2=tkinter.Button(top,text="Attendance_Entry",command= AttendanceEntryInDB)
B2.pack()
B3=tkinter.Button(top,text="QUIT",fg="red",command=quit)
B3.pack()
top.mainloop()
