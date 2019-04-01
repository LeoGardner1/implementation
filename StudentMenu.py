
from tkinter import *
from globalFunctions import *
import csv
import tkinter.messagebox
from os import remove, rename
from tempfile import NamedTemporaryFile
import shutil
import ast
import datetime
from datetime import date, timedelta, datetime
import time
import os
from tkinter import ttk
from tkcalendar import Calendar, DateEntry

class StudentMenu(Frame):

    def __init__(self, master, *args):

        Frame.__init__(self, master)
        self.grid()

        width = 500
        height = 500
        centred_window = centre_app(master, width, height)        
        master.geometry(centred_window)
        
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight = 1)

        self.studentID = args[0]
        #self.studentID = '100001'

        self.mainMenu()


    def mainMenu(self):

        butFormativeTest = Button(self, text="Formative Test", height=2, width=22, command=lambda:newPage(self, FormativeTest, "Formative Test", self.studentID))
        butFormativeTest.grid(row=1, column=1)

        new_line = Label(self, text=" ")
        new_line.grid(row=2, columnspan=2, sticky=NSEW)

        butSummativeTest = Button(self, text="Summative Test", height=2, width=22, command=lambda:newPage(self, SummativeTest, "Summative Test", self.studentID))
        butSummativeTest.grid(row=3, column=1)

        new_line1 = Label(self, text=" ")
        new_line1.grid(row=4, columnspan=2, sticky=NSEW)

        butMyResults = Button(self, text="My Test Results", height=2, width=22, command=lambda:newPage(self, ReleasedFormativeTest, "Released Formative Test", self.studentID))
        butMyResults.grid(row=5, column=1)

class FormativeTest(Frame):

    def __init__(self, master, *args):

        Frame.__init__(self, master)
        self.grid()

        width = 500
        height = 500
        centred_window = centre_app(master, width, height)        
        master.geometry(centred_window)

        master.grid_columnconfigure(0, weight=1)
        master.grid_columnconfigure(2, weight=1)
        master.grid_columnconfigure(5, weight=1)
        master.grid_columnconfigure(7, weight=1)

        master.grid_rowconfigure(0, weight = 1)
        master.grid_rowconfigure(2, weight = 2)
        #master.grid_rowconfigure(6, weight = 1)
        master.grid_rowconfigure(14, weight=5)

        self.studentID = args[0]

        self.display_formativeTest()

    def display_formativeTest(self):

        formative_test_list = []

        student_group = ""

        with open('students.csv') as students:
            reader = csv.reader(students)

            next(reader, None)
            
            for row in reader:
                if row[0] == self.studentID:
                    student_group = row[3]

        print(student_group)

        check_if_exist = os.path.isfile("ReleasedFormative.csv")

        if not check_if_exist:
            with open('ReleasedFormative.csv', 'w') as csvfile:

                fieldnames = ["test_name", "student_maxAttempt", "test_duration", "date_released", "released_by", "released_to"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()

        with open("ReleasedFormative.csv", "r") as csvfile:
            fieldnames = ["test_name", "student_maxAttempt", "test_duration", "date_released", "released_by", "released_to"]
            reader = csv.DictReader(csvfile, fieldnames = fieldnames)

            for row in reader:
                if row["released_to"] == student_group:
                    formative_test_list.append({"test_name": row["test_name"], "student_maxAttempt": row["student_maxAttempt"],
                                                "test_duration": row["test_duration"], "released_to": row["released_to"],
                                                "date_released": row["date_released"]})

        row_adjuster = 0

        self.getTestName = StringVar()
        self.getTestName.set(' ')

        if len(formative_test_list) == 0:
            empty_testlbl = Label(text="No Test Available to Attempt", font=("Arial", 14, "bold"))
            empty_testlbl.grid(row=4, column=1, columnspan=6, rowspan=2, sticky=NSEW)
            
        else:
            test_name_heading = Label(text="Name of Test", font=("MS", 10, "bold"))
            test_name_heading.grid(row=3, column=1, columnspan=2, sticky=NSEW)

            test_duration_heading = Label(text="Test Duration", font=("MS", 10, "bold"))
            test_duration_heading.grid(row=3, column=4, sticky=NSEW)

            date_released_heading = Label(text="Date Released", font=("MS", 10, "bold"))
            date_released_heading.grid(row=3, column=6, sticky=NSEW)
            
            for i, item in enumerate(formative_test_list):

                testName_button = Radiobutton(value=item["test_name"], text=str(i + 1) + ". " + item["test_name"], variable=self.getTestName)
                testName_button.grid(row=row_adjuster + 4, column=1, sticky=W)

                test_duration_lbl = Label(text=item["test_duration"])
                test_duration_lbl.grid(row=row_adjuster + 4, column=4, sticky=NSEW)

                date_released_lbl = Label(text=item["date_released"])
                date_released_lbl.grid(row=row_adjuster + 4, column=6, sticky=NSEW)
                
                row_adjuster += 1
        
        goBack_button = Button(text="Go Back to Homepage", width=20, command=lambda:newPage(self, StudentMenu, "Student Page", self.studentID))
        goBack_button.grid(row=1, column=1, sticky=NSEW)

        view_stats_button = Button(text="Attempt Test", width=20, command=self.attempt_formative)
        view_stats_button.grid(row=1, column=6, sticky=NSEW)

        Heading_lbl = Label(text="Formative Test", font=("bold"))
        Heading_lbl.grid(row=2, column=1, columnspan=6, sticky=NSEW)

    def attempt_formative(self):

        test_name = self.getTestName.get()
        test_type = " formative"
        test_details = ""
        test_details = test_name + test_type

        if test_name == ' ':
            tkinter.messagebox.showwarning("Entry Error", "Please select a test to attempt")
            return

        newPage(self, TestWindow, "Formative Assessment Test", self.studentID, test_details)
    

class SummativeTest(Frame):

    def __init__(self, master, *args):

        Frame.__init__(self, master)
        self.grid()

        width = 500
        height = 500
        centred_window = centre_app(master, width, height)        
        master.geometry(centred_window)

        master.grid_columnconfigure(0, weight=1)
        master.grid_columnconfigure(2, weight=1)
        master.grid_columnconfigure(5, weight=1)
        master.grid_columnconfigure(7, weight=1)

        master.grid_rowconfigure(0, weight = 1)
        master.grid_rowconfigure(2, weight = 2)
        #master.grid_rowconfigure(6, weight = 1)
        master.grid_rowconfigure(14, weight=5)

        self.studentID = args[0]

        self.display_summativeTest()

    def display_summativeTest(self):

        summative_test_list = []

        student_group = ""

        with open('students.csv') as students:
            reader = csv.reader(students)

            next(reader, None)
            
            for row in reader:
                if row[0] == self.studentID:
                    student_group = row[3]

        print(student_group)

        check_if_exist = os.path.isfile("ReleasedSummative.csv")

        if not check_if_exist:
            with open('ReleasedSummative.csv', 'w') as csvfile:

                fieldnames = ["test_name", "test_deadline", "test_duration", "date_released", "released_by", "released_to"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()

        with open("ReleasedSummative.csv", "r") as csvfile:
            fieldnames = ["test_name", "test_deadline", "test_duration", "date_released", "released_by", "released_to"]
            reader = csv.DictReader(csvfile, fieldnames = fieldnames)

            for row in reader:
                if row["released_to"] == student_group:
                    summative_test_list.append({"test_name": row["test_name"], "released_to": row["released_to"],
                                               "date_released": row["date_released"], "test_deadline": row["test_deadline"]})

        row_adjuster = 0

        self.getTestName = StringVar()
        self.getTestName.set(' ')

        if len(summative_test_list) == 0:
            empty_testlbl = Label(text="No Test Available to Attempt", font=("Arial", 14, "bold"))
            empty_testlbl.grid(row=4, column=1, columnspan=6, rowspan=2, sticky=NSEW)
            
        else:
            test_name_heading = Label(text="Name of Test", font=("MS", 10, "bold"))
            test_name_heading.grid(row=3, column=1, columnspan=2, sticky=NSEW)

            date_released_heading = Label(text="Date Released", font=("MS", 10, "bold"))
            date_released_heading.grid(row=3, column=4, sticky=NSEW)

            test_deadline_heading = Label(text="Deadline", font=("MS", 10, "bold"))
            test_deadline_heading.grid(row=3, column=6, sticky=NSEW)
            
            for i, item in enumerate(summative_test_list):

                testName_button = Radiobutton(value=item["test_name"], text=str(i + 1) + ". " + item["test_name"], variable=self.getTestName)
                testName_button.grid(row=row_adjuster + 4, column=1, sticky=W)

                date_released_lbl = Label(text=item["date_released"])
                date_released_lbl.grid(row=row_adjuster + 4, column=4, sticky=NSEW)

                test_deadline_lbl = Label(text=item["test_deadline"])
                test_deadline_lbl.grid(row=row_adjuster + 4, column=6, sticky=NSEW)
                

                row_adjuster += 1
        
        goBack_button = Button(text="Go Back to Homepage", width=20, command=lambda:newPage(self, StudentMenu, "Student Page", self.studentID))
        goBack_button.grid(row=1, column=1, sticky=NSEW)

        view_stats_button = Button(text="Attempt Test", width=20, command=self.attempt_summative)
        view_stats_button.grid(row=1, column=6, sticky=NSEW)

        Heading_lbl = Label(text="Summative Test", font=("bold"))
        Heading_lbl.grid(row=2, column=1, columnspan=6, sticky=NSEW)

    def attempt_summative(self):

        test_name = self.getTestName.get()
        test_type = " summative"
        test_details = ""
        test_details = test_name + test_type

        testTaken = False
        pastDeadline = False
        errormsg = ""

        with open("ReleasedSummative.csv", "r") as csvfile:
            fieldnames = ["test_name", "test_deadline", "test_duration", "date_released", "released_by", "released_to"]
            reader = csv.DictReader(csvfile, fieldnames = fieldnames)
            for row in reader:
                if row["test_name"] == test_name:
                    deadline = datetime.strptime(row["test_deadline"], "%d/%m/%Y")
        currentDate = datetime.today()
        if currentDate > deadline:
            pastDeadline = True
            errormsg += "The deadline for this test has passed! "
        with open('studentResults.csv', 'r') as results:
            fieldnames = ["studentID", "studentGroup", "test_name", "date_released", "deadline", "total_score", "total_question", "student_f_name", "student_l_name"]
            reader = csv.DictReader(results, fieldnames)
            for row in reader:
                if (row["studentID"] == self.studentID) and (row["test_name"] == test_name):
                    testTaken = True
                    errormsg += "You have already taken this test! "
            if test_name == ' ':
                errormsg += "Please select a test to attempt!"
                return
        if errormsg != "":
            tkinter.messagebox.showinfo("Test Submission", errormsg)
        if (testTaken == False) and (pastDeadline == False):
            newPage(self, TestWindow, "Summative Assessment Test", self.studentID, test_details)

class TestWindow(Frame):

    def __init__(self, master, *args):

        Frame.__init__(self, master)
        #self.grid()

        width = 550
        height = 600

        centred_window = centre_app(master, width, height)
        master.geometry(centred_window)

        scrollBar(master, self)

        self.studentID = args[0]

        self.test_details = args[1].split()

        self.test_name = self.test_details[0]

        self.test_type = self.test_details[1]
        
        self.test_window()

    def test_window(self):

        self.the_test = {}

        with open( self.test_name + '.csv', 'r') as csvfile:
            fieldnames = ["question_no", "question", "answer_choices", "is_correct_answer", "answer_feedback"]
            reader = csv.DictReader(csvfile, fieldnames = fieldnames)

            next(reader, None)

            for row in reader:
                self.the_test[row["question_no"]] = {"question":row["question"], "answer_choices": ast.literal_eval(row["answer_choices"]),
                                               "is_correct_answer": ast.literal_eval(row["is_correct_answer"]),
                                               "answer_feedback": ast.literal_eval(row["answer_feedback"])}

        print(self.the_test)



        new_line0 = Label(self.frame, text="-" * 100)
        new_line0.grid(row=0, column=0, columnspan=3, sticky=EW)
        
        testNamelbl = Label(self.frame, text= self.test_name, font=("Arial", 14, "bold"))
        testNamelbl.grid(row=1, column=0, rowspan=3, columnspan=2, sticky=NW)

        

        #new_line1 = Label(self.frame, text="-" * 100)
        #new_line1.grid(row=2, column=0, columnspan=3, sticky=EW)

        rowAdjuster = 0
        question_no = 1

        self.correctAnsA_entries = []
        self.correctAnsB_entries = []
        self.correctAnsC_entries = []
        self.correctAnsD_entries = []

        self.answersA = []
        self.answersB = []
        self.answersC = []
        self.answersD = []

        

        for item in self.the_test.values():

            new_line = Label(self.frame, text="-" * 100)
            new_line.grid(row=rowAdjuster +2, column=0, columnspan=5, sticky=EW)
            
            question_no_lbl = Label(self.frame, text="Question " + str(question_no) + ":", font=("Arial", 12, "bold"))
            question_no_lbl.grid(row= rowAdjuster + 3, column=0, sticky=EW)

            questionlbl = Label(self.frame, text=item['question'], font=("Arial", 12))
            questionlbl.grid(row= rowAdjuster + 3, column=1, sticky=W)

            self.correctAnsA = BooleanVar()
            self.correctAnsB = BooleanVar()
            self.correctAnsC = BooleanVar()
            self.correctAnsD = BooleanVar()

            ansA = Checkbutton(self.frame, text="A.", font=("Arial", 10, "bold"), variable=self.correctAnsA)
            ansA.grid(row=rowAdjuster + 5, column=0, sticky=E)

            ansA_lbl = Label(self.frame, text=item['answer_choices']['A'], font=("Arial", 10))
            ansA_lbl.grid(row=rowAdjuster + 5, column=1, sticky=W)

            ansB = Checkbutton(self.frame, text="B.", font=("Arial", 10, "bold"), variable=self.correctAnsB)
            ansB.grid(row=rowAdjuster + 6, column=0, sticky=E)

            ansB_lbl = Label(self.frame, text=item['answer_choices']['B'], font=("Arial", 10))
            ansB_lbl.grid(row=rowAdjuster + 6, column=1, sticky=W)

            if item['answer_choices']['C'] != "":
                
                ansC = Checkbutton(self.frame, text="C.", font=("Arial", 10, "bold"), variable=self.correctAnsC)
                ansC.grid(row=rowAdjuster + 7, column=0, sticky=E)

                ansC_lbl = Label(self.frame, text=item['answer_choices']['C'], font=("Arial", 10))
                ansC_lbl.grid(row=rowAdjuster + 7, column=1, sticky=W)

            if item['answer_choices']['D'] != "":

                ansD = Checkbutton(self.frame, text="D.", font=("Arial", 10, "bold"), variable=self.correctAnsD)
                ansD.grid(row=rowAdjuster + 8, column=0, sticky=E)

                ansD_lbl = Label(self.frame, text=item['answer_choices']['D'], font=("Arial", 10))
                ansD_lbl.grid(row=rowAdjuster + 8, column=1, sticky=W)
            
            rowAdjuster += 9
            question_no += 1

            self.correctAnsA_entries.append(self.correctAnsA)
            self.correctAnsB_entries.append(self.correctAnsB)
            self.correctAnsC_entries.append(self.correctAnsC)
            self.correctAnsD_entries.append(self.correctAnsD)

            self.answersA.append(item['is_correct_answer']['A'])
            self.answersB.append(item['is_correct_answer']['B'])
            self.answersC.append(item['is_correct_answer']['C'])
            self.answersD.append(item['is_correct_answer']['D'])

        self.numOfQuestions = question_no - 1

        submitBtn = Button(self.frame, text="Submit Test", command=lambda:self.CheckAnswers())
        submitBtn.grid(row=1, column=2, sticky=E)
    def frameConfigure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))   

    def CheckAnswers(self):
        self.totalMark = 0
        self.totalQuestions = 0
        allAnswered = True
        for i in range(0, self.numOfQuestions):
            if (self.correctAnsA_entries[i].get() == False) and (self.correctAnsB_entries[i].get() == False) and (self.correctAnsC_entries[i].get() == False) and (self.correctAnsD_entries[i].get() == False):
                allAnswered = False
            if self.correctAnsA_entries[i].get() == True:
                if self.correctAnsA_entries[i].get() == self.answersA[i]:
                    self.totalMark += 1
            if self.correctAnsB_entries[i].get() == True:
                if self.correctAnsB_entries[i].get() == self.answersB[i]:
                    self.totalMark += 1
            if self.correctAnsC_entries[i].get() == True:
                if self.correctAnsC_entries[i].get() == self.answersC[i]:
                    self.totalMark += 1
            if self.correctAnsD_entries[i].get() == True:
                if self.correctAnsD_entries[i].get() == self.answersD[i]:
                    self.totalMark += 1
            self.totalQuestions += 1

        if allAnswered == True:
            if self.test_type == "summative":
                self.WriteSummativeResult()
            else:
                self.WriteFormativeResult()
        else:
            tkinter.messagebox.showinfo("Test Submission", "All questions must be attempted!")

    def GetStuDetails(self):
        with open("students.csv", "r") as students:
            fieldnames = ["studentID", "first_name", "last_name", "student_group"]
            reader = csv.DictReader(students, fieldnames=fieldnames)

            for row in reader:
                if row["studentID"] == self.studentID:
                    self.group = row["student_group"]
                    self.forename = row["first_name"]
                    self.surname = row["last_name"]

    def GetSumTestDetails(self):
        with open("ReleasedSummative.csv", "r") as tests:
            fieldnames = ["test_name", "test_deadline", "test_duration", "date_released", "released_by", "released_to"]
            reader = csv.DictReader(tests, fieldnames=fieldnames)
            for row in reader:
                if row["test_name"] == self.test_name:
                    self.date_released = row["date_released"]
                    self.deadline = row["test_deadline"]

    def GetFormTestDetails(self):
        with open("ReleasedSummative.csv", "r") as tests:
            fieldnames = ["test_name", "student_maxAttempt", "test_duration", "date_released", "released_by", "released_to"]
            reader = csv.DictReader(tests, fieldnames=fieldnames)
            for row in reader:
                if row["test_name"] == self.test_name:
                    self.date_released = row["date_released"]


    def WriteSummativeResult(self):
        self.GetStuDetails()
        self.GetSumTestDetails()
        
        with open('studentResults.csv', 'a') as results:
            fieldnames = ["studentID", "studentGroup", "test_name", "date_released", "deadline", "total_score", "total_question", "student_f_name", "student_l_name"]
            writer = csv.DictWriter(results, fieldnames)
            writer.writerow({"studentID": self.studentID, "studentGroup": self.group, "test_name": self.test_name, "date_released": self.date_released, "deadline": self.deadline, "total_score": self.totalMark, "total_question": self.totalQuestions, "student_f_name": self.forename, "student_l_name": self.surname})
            tkinter.messagebox.showinfo("Test Submission" , "The test was submitted successfully!")
        newPage(self, StudentMenu, "Student Menu", self.studentID)

    def WriteFormativeResult(self):
        test_file = "ReleasedFormative.csv"
        print(self.totalMark)

class AttemptFormative(Frame):

    pass

class AttemptSummative(Frame):

    pass

'''
root = Tk()
app = StudentMenu(root)
root.mainloop()
'''
