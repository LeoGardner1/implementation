
from tkinter import *
import datetime
import csv
import ast

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

def newPage(self, PageName, title, user_id, var=None):
    self.master.destroy()
    root = Tk()
    root.title(title)
    PageName(root, user_id, var)

def currentDate():
    now = datetime.datetime.now()
    return now
    

def scrollBar(master, self):

        # Code to add scrollbar to a group of widgets in Tkinter
        # using frame-embedded-in-canvas solution 
        # taken from Stack Overflow post by Bryan Oakley
        # accessed 13/03/2019
        # https://stackoverflow.com/a/3092341
        self.canvas = Canvas(master, borderwidth=0)
        self.frame = Frame(self.canvas)
        self.scrollbar = Scrollbar(master, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4,4), window=self.frame, anchor="nw", tags="self.frame")

        self.frame.bind("<Configure>", self.frameConfigure)
        self.canvas.bind_all('<MouseWheel>', lambda event: self.canvas.yview_scroll(int(-1*(event.delta/50)), "units"))

        # end referenced code

    #Add frameConfigure function into your class
'''
    def frameConfigure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))    
'''

def rmv_extra_spaces(words):
    return " ".join(words.split()).strip()

def test_settings(self, test_name, lecturerID, test_type):

    student_cohorts = []

    with open("lecturers.csv", "r") as csvfile:
        fieldnames = ["lecturerID", "saved_test", "student_cohort"]
        reader = csv.DictReader(csvfile, fieldnames = fieldnames)

        for row in reader:
            if row["lecturerID"] == lecturerID:
                student_cohorts = sorted(ast.literal_eval(row["student_cohort"]))

    testName_lbl = Label(text="Releasing " + test_type.title() +"\n\"" +test_name + "\"", font=("bold"))
    testName_lbl.grid(row=2, column=1, columnspan=6, sticky=NSEW)

    new_line = Label(text=" ")
    new_line.grid(row=6)

    student_cohorts_lbl = Label(text="Group of students this test will be released to:")
    student_cohorts_lbl.grid(row=11, rowspan=2, column=1, columnspan=6, sticky=NSEW)
    
    self.getStudent_cohorts = StringVar(self.master)
    self.getStudent_cohorts.set(" ")

    student_cohorts_option = OptionMenu(self.master, self.getStudent_cohorts, *student_cohorts)
    student_cohorts_option.grid(row=13, column=4, sticky=NSEW)

    new_line = Label(text=" ")
    new_line.grid(row=10)

    test_duration_lbl = Label(text="Test Duration (in minutes):")
    test_duration_lbl.grid(row=7, rowspan=2, column=1, columnspan=6, sticky=NSEW)

    self.test_duration_list = ["Untimed"] + list(map(str, range(1,601)))
    
    self.test_duration = StringVar(self.master)
    self.test_duration.set("Untimed")   

    test_duration_option = Spinbox(self.master, textvariable=self.test_duration, values=self.test_duration_list)
    test_duration_option.grid(row=9, column=4, sticky=NSEW)

    goBack_button = Button(text="Go Back to Homepage", width=20, command=self.go_back)
    goBack_button.grid(row=1, column=1, sticky=NSEW)

    release_button = Button(text="Release Test", width=20, command=self.release_test)
    release_button.grid(row=1, column=6, sticky=NSEW)
