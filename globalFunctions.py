
from tkinter import *

#from StudentMenu import StudentMenu
'''
def lecturerHomePage():
    lecturer = Tk()
    lecturer.title("Lecturer Page")
    LecturerMenu(lecturer)

def studentHomePage():
    student = Tk()
    student.title("Student Page")
    StudentMenu(student)
'''
def centre_app(m, w, h):

    ws = m.winfo_screenwidth()
    hs = m.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)        
    return ("%dx%d+%d+%d" %(w, h , x, y))

def newPage(self, PageName, title, var=None):
    self.master.destroy()
    root = Tk()
    root.title(title)
    PageName(root, var)
