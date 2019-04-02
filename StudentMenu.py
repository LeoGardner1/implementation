
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

        butMyResults = Button(self, text="My Test Results", height=2, width=22, command=lambda:newPage(self, ViewMyResults, "My Results", self.studentID))
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

        testTaken = False
 
        errormsg = ""


        with open("ReleasedFormative.csv", "r") as csvfile:
            fieldnames = ["test_name", "student_maxAttempt", "test_duration", "date_released", "released_by", "released_to"]
            reader = csv.DictReader(csvfile, fieldnames = fieldnames)
##            for row in reader:
##                if row["test_name"] == test_name:
##                    deadline = datetime.strptime(row["test_deadline"], "%d/%m/%Y")
##        currentDate = datetime.today()
##        if currentDate > deadline:
##            pastDeadline = True
##            errormsg += "The deadline for this test has passed! "
        with open('formativeStudentResults.csv', 'r') as results:
            fieldnames = ["test_name", "studentID", "studentGroup", "date_released", "attempts_made", "total_scores", "total_question", "answered_correctly"]
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
        if (testTaken == False):
            newPage(self, TestWindow, "Formative Assessment Test", self.studentID, test_details)

       
##        if test_name == ' ':
##            tkinter.messagebox.showwarning("Entry Error", "Please select a test to attempt")
##            return
##
##        newPage(self, TestWindow, "Formative Assessment Test", self.studentID, test_details)

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

        #print(test_details)

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
            errormsg += "The deadline for this test has passed!\n\n"
        with open('studentResults.csv', 'r') as results:
            fieldnames = ["studentID", "studentGroup", "test_name", "date_released", "deadline", "total_score", "total_question", "student_f_name", "student_l_name"]
            reader = csv.DictReader(results, fieldnames)
            for row in reader:
                if (row["studentID"] == self.studentID) and (row["test_name"] == test_name):
                    testTaken = True
                    errormsg += "You have already taken this test!\n"
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


        submitBtn = Button(self.frame, text="Submit Test", command=lambda:self.CheckAnswers())
        submitBtn.grid(row=1, column=2, sticky=E)
        
    def frameConfigure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))   

    def CheckAnswers(self):

        iter_correctAnsA_entries = iter(self.correctAnsA_entries)
        iter_correctAnsB_entries = iter(self.correctAnsB_entries)
        iter_correctAnsC_entries = iter(self.correctAnsC_entries)
        iter_correctAnsD_entries = iter(self.correctAnsD_entries)

        student_answers = {}
        self.score = 0

        for i in range(len(self.the_test)):
            student_answers["Question " + str(i + 1)] = {"given_answer": {"A":next(iter_correctAnsA_entries).get(),
                                                                          "B":next(iter_correctAnsB_entries).get(),
                                                                          "C":next(iter_correctAnsC_entries).get(),
                                                                          "D":next(iter_correctAnsD_entries).get()}}

        studentAns_list = []
        tempAns_holder = []

        for a, b in student_answers.items():
            
            for c, d in b.items():
                for e, f in d.items():
                    if f == True:
                        tempAns_holder.append(e)
                studentAns_list.append(((tempAns_holder)))
                tempAns_holder = []

        for i in studentAns_list:            
            if len(i) == 0:
                tkinter.messagebox.showinfo("Test Submission", "All questions must be attempted!")
                return

        #print(student_answers)

        for i in range(len(self.the_test)):
            if self.the_test["Question " + str(i +1)]["is_correct_answer"] == student_answers["Question " + str(i +1)]["given_answer"]:
                #print("Correct Answer")
                self.score += 1
            #else:
                #print("Wrong Answer")
            
        print("Score: %d/%d"%(self.score, len(self.the_test)))

        self.test_data = [self.the_test, student_answers, self.score]

        if self.test_type == "summative":
            self.WriteSummativeResult()
        else:
            self.WriteFormativeResult()

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
            writer.writerow({"studentID": self.studentID, "studentGroup": self.group, "test_name": self.test_name, "date_released": self.date_released, "deadline": self.deadline, "total_score": self.score, "total_question": len(self.the_test), "student_f_name": self.forename, "student_l_name": self.surname})
            tkinter.messagebox.showinfo("Test Submission" , "The test was submitted successfully!")
        newPage(self, ResultsWindow, "Your Test Result", self.studentID, self.test_data)

    def WriteFormativeResult(self):

        self.GetStuDetails()
        self.GetFormTestDetails()
        
        with open('formativeStudentResults.csv', 'a') as results:
            fieldnames = ["test_name", "studentID", "studentGroup", "date_released", "attempts_made", "total_scores", "total_question", "answered_correctly"]
            writer = csv.DictWriter(results, fieldnames)
            writer.writerow({"test_name": self.test_name, "studentID": self.studentID, "studentGroup": self.group, "date_released": self.date_released, "attempts_made": self.attempts_made,
                             "total_scores": self.totalMark, "total_question": self.totalQuestions, "answered_correctly": self.answered_correctly})
            tkinter.messagebox.showinfo("Test Submission" , "The test was submitted successfully!")

        newPage(self, ResultsWindow, "Your Test Result", self.studentID, self.test_data)
        
        test_file = "ReleasedFormative.csv"
        print(self.totalMark)
        
class ResultsWindow(Frame):

    def __init__(self, master, *args):

        Frame.__init__(self, master)
        #self.grid()

        width = 550
        height = 600

        centred_window = centre_app(master, width, height)
        master.geometry(centred_window)

        scrollBar(master, self)

        self.studentID = args[0]

        self.the_test = args[1][0]

        self.student_answers = args[1][1]

        self.test_score = args[1][2]
        
        self.result_window()

    def result_window(self):

        studentAns_list = []
        tempAns_holder = []

        for a, b in self.student_answers.items():
            
            for c, d in b.items():
                for e, f in d.items():
                    if f == True:
                        tempAns_holder.append(e)
                studentAns_list.append(((tempAns_holder)))
                tempAns_holder = []

        iter_studentAns_list = iter(studentAns_list)

        print(iter_studentAns_list)
	
        new_line0 = Label(self.frame, text="-" * 100)
        new_line0.grid(row=0, column=0, columnspan=3, sticky=EW)
        
        testScorelbl = Label(self.frame, text="Score:  %d / %d"%(self.test_score, len(self.the_test)), font=("Arial", 14, "bold"))
        testScorelbl.grid(row=1, column=0, rowspan=3, sticky=NW)

        #testNamelbl.grid(row=1, column=0, rowspan=3, columnspan=2, sticky=NW)

        #testScore = Label(self.frame, text="Score: ", font=("Arial", 14, "bold"))
        #testScore.grid(row=1, column=1, rowspan=3, sticky=EW)

        #submitBtn = Button(self.frame, text="Submit Test", command=self.check_test)
        #submitBtn.grid(row=1, column=2, sticky=E)

        goBack_button = Button(self.frame, text="Main Menu", command=lambda:newPage(self, StudentMenu, "Student Page", self.studentID))
        goBack_button.grid(row=1, column=2, sticky=W)

        rowAdjuster = 0
        question_no = 1


        for item in self.the_test.values():

            choices = ["A", "B"]

            new_line = Label(self.frame, text="-" * 100)
            new_line.grid(row=rowAdjuster +2, column=0, columnspan=3, sticky=EW)
            
            question_no_lbl = Label(self.frame, text="Question " + str(question_no) + ":", font=("Arial", 12, "bold"))
            question_no_lbl.grid(row= rowAdjuster + 3, column=0, sticky=EW)

            questionlbl = Label(self.frame, text=item['question'], font=("Arial", 12))
            questionlbl.grid(row= rowAdjuster + 3, column=1, sticky=W)


            ansA = Label(self.frame, text="A.", font=("Arial", 10, "bold"))
            ansA.grid(row=rowAdjuster + 5, column=0, sticky=E)

            ansA_lbl = Label(self.frame, text=item['answer_choices']['A'], font=("Arial", 10))
            ansA_lbl.grid(row=rowAdjuster + 5, column=1, sticky=W)

            ansB = Label(self.frame, text="B.", font=("Arial", 10, "bold"))
            ansB.grid(row=rowAdjuster + 6, column=0, sticky=E)

            ansB_lbl = Label(self.frame, text=item['answer_choices']['B'], font=("Arial", 10))
            ansB_lbl.grid(row=rowAdjuster + 6, column=1, sticky=W)

            if item['answer_choices']['C'] != "":
                
                ansC = Label(self.frame, text="C.", font=("Arial", 10, "bold"))
                ansC.grid(row=rowAdjuster + 7, column=0, sticky=E)

                ansC_lbl = Label(self.frame, text=item['answer_choices']['C'], font=("Arial", 10))
                ansC_lbl.grid(row=rowAdjuster + 7, column=1, sticky=W)

                choices.append("C")

            if item['answer_choices']['D'] != "":

                ansD = Label(self.frame, text="D.", font=("Arial", 10, "bold"))
                ansD.grid(row=rowAdjuster + 8, column=0, sticky=E)

                ansD_lbl = Label(self.frame, text=item['answer_choices']['D'], font=("Arial", 10))
                ansD_lbl.grid(row=rowAdjuster + 8, column=1, sticky=W)

                choices.append("D")

            new_line1 = Label(self.frame, text="-" * 100)
            new_line1.grid(row=rowAdjuster +9, column=0, columnspan=3, sticky=EW)

            chosenAns_lbl = Label(self.frame, text="Selected Answer:  %s"%("  ".join(next(iter_studentAns_list))), font=("Arial", 12))
            chosenAns_lbl.grid(row= rowAdjuster + 10, column=0, columnspan=2, sticky=W)

            #chosenAnswers = Label(self.frame, text="  ".join(next(iter_studentAns_list)), font=("Arial", 12))
            #chosenAnswers.grid(row= rowAdjuster + 10, column=1, sticky=W)
            incorrect = ""
            correct = ""

            for i in range(0, len(choices)):
                addstring = "Comment " + choices[i] + ": " + item['answer_feedback'][choices[i]]
                if item['is_correct_answer'][choices[i]] == False:
                    incorrect += addstring
                else:
                    correct += addstring

            if item['is_correct_answer'] == self.student_answers["Question " + str(question_no)]["given_answer"]:
                correctOrWrong = Label(self.frame, text="Correct Answer!", fg="green", font=("Arial", 12, "bold"))
                correctOrWrong.grid(row=rowAdjuster +11, column=1, sticky=SW)
                answercomment = Label(self.frame, text=correct, fg="green", font=("Arial", 12, "bold"))
                answercomment.grid(row=rowAdjuster +12, column=1, sticky=SW)
            else:
                correctOrWrong = Label(self.frame, text="Incorrect Answer!", fg="red", font=("Arial", 12, "bold"))
                correctOrWrong.grid(row=rowAdjuster +11, column=1, sticky=SW)
                answercomment = Label(self.frame, text=incorrect, fg="red", font=("Arial", 12, "bold"))
                answercomment.grid(row=rowAdjuster +12, column=1, sticky=SW)

            rowAdjuster += 12
            question_no += 1

    def frameConfigure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

class ViewMyResults(Frame):
    def __init__(self, master, *args):

        Frame.__init__(self, master)
        #self.grid()

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

        #scrollBar(master, self)

        self.studentID = args[0]

        self.ShowTestList()

    def ShowTestList(self):
        summative_test_list = []

        check_if_exist = os.path.isfile("studentResults.csv")

        if not check_if_exist:
            with open('studentResults.csv', 'w') as csvfile:

                fieldnames = ["studentID", "studentGroup", "test_name", "date_released", "deadline", "total_score", "total_question", "student_f_name", "student_l_name"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()

        with open("studentResults.csv", "r") as csvfile:
            fieldnames = ["studentID", "studentGroup", "test_name", "date_released", "deadline", "total_score", "total_question", "student_f_name", "student_l_name"]
            reader = csv.DictReader(csvfile, fieldnames = fieldnames)

            for row in reader:
                if row["studentID"] == self.studentID:
                    summative_test_list.append({"studentID": row["studentID"], "studentGroup": row["studentGroup"], "test_name": row["test_name"], "date_released": row["date_released"], "deadline": row["deadline"], "total_score": row["total_score"], "total_question": row["total_question"], "student_f_name": row["student_f_name"], "student_l_name": row["student_l_name"]})
                    self.forename = row["student_f_name"]
                    self.surname = row["student_l_name"]
        row_adjuster = 0

        self.getSumTestName = StringVar()
        self.getSumTestName.set(' ')

        if len(summative_test_list) == 0:
            empty_sumtestlbl = Label(text="No Summative Tests Attempted", font=("Arial", 14, "bold"))
            empty_sumtestlbl.grid(row=4, column=1, columnspan=6, rowspan=2, sticky=NSEW)
            
        else:
            sumtest_name_heading = Label(text="Name of Test", font=("MS", 10, "bold"))
            sumtest_name_heading.grid(row=3, column=1, columnspan=2, sticky=NSEW)

            sumdate_released_heading = Label(text="Date Released", font=("MS", 10, "bold"))
            sumdate_released_heading.grid(row=3, column=4, sticky=NSEW)

            test_deadline_heading = Label(text="Deadline", font=("MS", 10, "bold"))
            test_deadline_heading.grid(row=3, column=6, sticky=NSEW)
            
            for i, item in enumerate(summative_test_list):

                sumtestName_button = Radiobutton(value=item["test_name"], text=str(i + 1) + ". " + item["test_name"], variable=self.getSumTestName)
                sumtestName_button.grid(row=row_adjuster + 4, column=1, sticky=W)

                sumdate_released_lbl = Label(text=item["date_released"])
                sumdate_released_lbl.grid(row=row_adjuster + 4, column=4, sticky=NSEW)

                test_deadline_lbl = Label(text=item["deadline"])
                test_deadline_lbl.grid(row=row_adjuster + 4, column=6, sticky=NSEW)          

                row_adjuster += 1

        FormHeading_lbl = Label(text="Formative Test Results", font=("bold"))
        FormHeading_lbl.grid(row=row_adjuster + 4, column=1, columnspan=6, sticky=NSEW)

        row_adjuster += 4
        formative_test_list = []

        check_if_exist = os.path.isfile("formativeStudentResults.csv")

        if not check_if_exist:
            with open('formativeStudentResults.csv', 'w') as csvfile:

                fieldnames = ["test_name", "studentID", "studentGroup", "date_released", "attempts_made", "total_score", "total_question", "answered_correctly"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()

        with open("formativeStudentResults.csv", "r") as csvfile:
            fieldnames = ["test_name", "studentID", "studentGroup", "date_released", "attempts_made", "total_score", "total_question", "answered_correctly"]
            reader = csv.DictReader(csvfile, fieldnames = fieldnames)

            for row in reader:
                if row["studentID"] == self.studentID:
                    formative_test_list.append({"test_name": row["test_name"], "studentID": row["studentID"], "studentGroup": row["student_group"], "date_released": row["date_released"], "attempts_made": row["attempts_made"], "total_score": row["total_score"], "total_question": row["total_question"], "answered_correctly": row["answered_correctly"]})

        self.getFormTestName = StringVar()
        self.getFormTestName.set(' ')

        if len(formative_test_list) == 0:
            empty_Formtestlbl = Label(text="No Formative Tests Attempted", font=("Arial", 14, "bold"))
            empty_Formtestlbl.grid(row=row_adjuster + 4, column=1, columnspan=6, rowspan=2, sticky=NSEW)
            
        else:
            Formtest_name_heading = Label(text="Name of Test", font=("MS", 10, "bold"))
            Formtest_name_heading.grid(row=row_adjuster + 4, column=1, columnspan=2, sticky=NSEW)

            Formdate_released_heading = Label(text="Date Released", font=("MS", 10, "bold"))
            Formdate_released_heading.grid(row=row_adjuster + 4, column=4, sticky=NSEW)
            
            for i, item in enumerate(formative_test_list):

                FormtestName_button = Radiobutton(value=item["test_name"], text=str(i + 1) + ". " + item["test_name"], variable=self.getFormTestName)
                FormtestName_button.grid(row=row_adjuster + 8, column=1, sticky=W)

                Formdate_released_lbl = Label(text=item["date_released"])
                Formdate_released_lbl.grid(row=row_adjuster + 8, column=4, sticky=NSEW)
                
                row_adjuster += 1
        
        goBack_button = Button(text="Go Back to Homepage", width=20, command=lambda:newPage(self, StudentMenu, "Student Page", self.studentID))
        goBack_button.grid(row=1, column=1, sticky=NSEW)

        view_stats_button = Button(text="View Statistics", width=20, command=lambda:self.LoadStats())
        view_stats_button.grid(row=1, column=6, sticky=NSEW)

        SumHeading_lbl = Label(text="Summative Test Results", font=("bold"))
        SumHeading_lbl.grid(row=2, column=1, columnspan=6, sticky=NSEW)

    def LoadStats(self):
        if (self.getSumTestName.get() == " ") and (self.getFormTestName.get() == " "):
            tkinter.messagebox.showinfo("View Statistics", "Please Select a Test to View!")
        else:
            if self.getSumTestName.get() != " ":
                test_details = self.getSumTestName.get() + " " + "summative"
                title = self.forename + " " + self.surname + " " + self.getSumTestName.get()
            else:
                test_details = self.getFormTestName.get() + " " + "formative"
                title = self.forename + " " + self.surname + " " + self.getFormTestName.get()
            newPage(self, ViewMyStats, title, self.studentID, test_details)
            

class ViewMyStats(Frame):
        def __init__(self, master, *args):

            Frame.__init__(self, master)
            #self.grid()

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

            #scrollBar(master, self)

            self.studentID = args[0]
            test_details = args[1].split()
            self.test_name = test_details[0]
            self.test_type = test_details[1]
            
            self.ReadStats()

        def ReadStats(self):

            def CalcGrade(score, question_total):
                percentage = (score / question_total) * 100
                if percentage >= 70:
                    return("1st")
                elif (percentage < 70) and (percentage >= 60):
                    return("2-1")
                elif (percentage < 60) and (percentage >= 50):
                    return("2-2")
                elif (percentage < 50) and (percentage >= 40):
                    return("3rd")
                else:
                    return("Fail")

            if self.test_type == "summative":
                print("summative")
                with open("studentResults.csv", "r") as csvfile:
                    fieldnames = ["studentID", "studentGroup", "test_name", "date_released", "deadline", "total_score", "total_question", "student_f_name", "student_l_name"]
                    reader = csv.DictReader(csvfile, fieldnames = fieldnames)

                    for row in reader:
                        if (row["studentID"] == self.studentID) and (row["test_name"] == self.test_name):
                            test_details = {"studentID": row["studentID"], "studentGroup": row["studentGroup"], "test_name": row["test_name"], "date_released": row["date_released"], "deadline": row["deadline"], "total_score": row["total_score"], "total_question": row["total_question"], "student_f_name": row["student_f_name"], "student_l_name": row["student_l_name"]}

                test_name_heading = Label(text=test_details["test_name"], font=("bold"))
                test_name_heading.grid(row=2, column=1, columnspan=6, sticky=NSEW)

                Date_released_heading = Label(text="Date Released:", font=("MS", 10, "bold"))
                Date_released_heading.grid(row=6, column=3, sticky=NSEW)

                test_deadline_heading = Label(text="Deadline:", font=("MS", 10, "bold"))
                test_deadline_heading.grid(row=8, column=3, sticky=NSEW)

                test_score_heading = Label(text="Score:", font=("MS", 10, "bold"))
                test_score_heading.grid(row=10, column=3, sticky=NSEW)

                test_grade_heading = Label(text="Grade:", font=("MS", 10, "bold"))
                test_grade_heading.grid(row=12, column=3, sticky=NSEW)

                Date_released = Label(text=test_details["date_released"])
                Date_released.grid(row=6, column=4, sticky=NSEW)

                test_deadline = Label(text=test_details["deadline"])
                test_deadline.grid(row=8, column=4, sticky=NSEW)

                test_score = Label(text=test_details["total_score"] + "/" + test_details["total_question"])
                test_score.grid(row=10, column=4, sticky=NSEW)

                score = int(test_details["total_score"])
                question_total = int(test_details["total_question"])
                
                grade = CalcGrade(score, question_total)

                test_grade = Label(text=grade)
                test_grade.grid(row=12, column=4, sticky=NSEW)



            else:
                print("formative")
                with open("formativeStudentResults.csv", "r") as csvfile:
                    fieldnames = ["test_name", "studentID", "studentGroup", "date_released", "attempts_made", "total_score", "total_question", "answered_correctly"]
                    reader = csv.DictReader(csvfile, fieldnames = fieldnames)

                    for row in reader:
                        if (row["studentID"] == self.studentID) and (row["test_name"] == self.test_name):
                            test_details = {"test_name": row["test_name"], "studentID": row["studentID"], "studentGroup": row["student_group"], "date_released": row["date_released"], "attempts_made": row["attempts_made"], "total_score": row["total_score"], "total_question": row["total_question"], "answered_correctly": row["answered_correctly"]}

                test_name_heading = Label(text=test_details["test_name"], font=("bold"))
                test_name_heading.grid(row=2, column=1, columnspan=6, sticky=NSEW)

                Date_released_heading = Label(text="Date Released:", font=("MS", 10, "bold"))
                Date_released_heading.grid(row=6, column=3, sticky=NSEW)

                test_deadline_heading = Label(text="Number of Attempts:", font=("MS", 10, "bold"))
                test_deadline_heading.grid(row=8, column=3, sticky=NSEW)

                test_score_heading = Label(text="Score:", font=("MS", 10, "bold"))
                test_score_heading.grid(row=10, column=3, sticky=NSEW)

                Date_released = Label(text=test_details["date_released"])
                Date_released.grid(row=6, column=4, sticky=NSEW)

                test_deadline = Label(text=test_details["deadline"])
                test_deadline.grid(row=8, column=4, sticky=NSEW)

                test_score = Label(text=test_details["total_score"] + "/" + test_details["total_question"])
                test_score.grid(row=10, column=4, sticky=NSEW)
            goBack_button = Button(text="Go Back to Homepage", width=20, command=lambda:newPage(self, StudentMenu, "Student Page", self.studentID))
            goBack_button.grid(row=1, column=3, columnspan=2, sticky=NSEW)

class AttemptFormative(Frame):

    pass

class AttemptSummative(Frame):

    pass

'''
root = Tk()
app = StudentMenu(root)
root.mainloop()
'''
