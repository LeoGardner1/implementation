
from tkinter import *
from globalFunctions import *
import csv
import tkinter.messagebox
from os import remove, rename
from tempfile import NamedTemporaryFile
import shutil
import ast
import datetime
from datetime import date, timedelta
import time
import os
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
import operator
import string



class LecturerMenu(Frame):

    def __init__(self, master, *args):

        Frame.__init__(self, master)
        self.grid()

        width = 500
        height = 500
        centred_window = centre_app(master, width, height)
        master.geometry(centred_window)

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight = 1)

        #self.lecturerID = args[0]
        self.lecturerID = '100000' #TEMPORARY

        self.mainMenu()

    def mainMenu(self):

        butCreateTest = Button(self, text="Create Test", height=2, width=22, command=lambda:newPage(self, QuestionsSet, "Create Test", self.lecturerID))
        butCreateTest.grid(row=1, column=1)

        new_line = Label(self, text=" ")
        new_line.grid(row=2, columnspan=2, sticky=NSEW)

        butSummative = Button(self, text="My Saved Test", height=2, width=22, command=lambda:newPage(self, SavedTest, "My Saved Test", self.lecturerID))
        butSummative.grid(row=3, column=1)

        new_line1 = Label(self, text=" ")
        new_line1.grid(row=4, columnspan=2, sticky=NSEW)

        butFormative = Button(self, text="Released Formative Test", height=2, width=22, command=lambda:newPage(self, ReleasedFormativeTest, "Released Formative Test", self.lecturerID))
        butFormative.grid(row=5, column=1)

        new_line2 = Label(self, text=" ")
        new_line2.grid(row=6, columnspan=2, sticky=NSEW)

        butFormative = Button(self, text="Released Summative Test", height=2, width=22, command=lambda:newPage(self, ReleasedSummativeTest, "Released Summative Test", self.lecturerID))
        butFormative.grid(row=7, column=1)

class QuestionsSet(Frame):

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
        master.grid_rowconfigure(6, weight = 1)
        master.grid_rowconfigure(9, weight=5)

        self.lecturerID = args[0]

        self.noOfQuestions()

    def noOfQuestions(self):

        new_line = Label(text=" ")
        new_line.grid(row=6)

        noQuestion_label = Label(text="Select Number of Questions that you wish to create.")
        noQuestion_label.grid(row=4, rowspan=3, column=0, columnspan=7, sticky=NSEW)

        questionNumber_list = list(range(1,11))

        questionNumber = StringVar(self.master)
        questionNumber.set(questionNumber_list[0])

        questionNumber_option = OptionMenu(self.master, questionNumber, *questionNumber_list)
        questionNumber_option.grid(row=7, column=4, sticky=NSEW)

        goBack_button = Button(text="Go Back to Homepage", width=20, command=lambda:newPage(self, LecturerMenu, "Lecturer Page", self.lecturerID))
        goBack_button.grid(row=1, column=1, sticky=NSEW)

        cont_button = Button(text="Continue Creating Test", width=20, command=lambda:newPage(self, CreateTest, "Create Test", self.lecturerID, questionNumber.get()))
        cont_button.grid(row=1, column=6, sticky=NSEW)

class CreateTest(QuestionsSet):

    def __init__(self, master, *args):

        Frame.__init__(self, master)
        #self.grid()

        width = 550
        height = 600

        centred_window = centre_app(master, width, height)
        master.geometry(centred_window)

        scrollBar(master, self)

        self.lecturerID = args[0]

        self.questionNo= int(args[1])

        self.createTest()


    def createTest(self):

        rowAdjuster = 0

        self.test_entries = {}

        self.question_entries = []

        self.answers_entriesA = []
        self.answers_entriesB = []
        self.answers_entriesC = []
        self.answers_entriesD = []

        self.correctAnsA_entries = []
        self.correctAnsB_entries = []
        self.correctAnsC_entries = []
        self.correctAnsD_entries = []

        self.ansAcomment_entries = []
        self.ansBcomment_entries = []
        self.ansCcomment_entries = []
        self.ansDcomment_entries = []

        testNamelbl = Label(self.frame, text="\nEnter Test Name:\n", font=("Arial", 14, "bold"))
        testNamelbl.grid(row=0, column=0, rowspan=3, sticky=NE)

        self.testNameField=Entry(self.frame)
        self.testNameField.grid(row=1, column=1, sticky=W, ipadx="100", columnspan=4)

        testNameBtn = Button(self.frame, text="Save", command=self.storeTest)
        testNameBtn.grid(row=1, column=2)

        for i in range(self.questionNo):


            questionLbl = Label(self.frame, text="Question " + str(i+1) + ":", font=("Arial", 12, "bold"))
            questionLbl.grid(row= rowAdjuster + 3, column=0, sticky=E)

            questionField = Entry(self.frame)
            questionField.grid(row=rowAdjuster + 3, column=1, ipadx="100")

            answersLbl = Label(self.frame, text="Answer Choices: (Tick the correct answers)", font=("Tahome", 10, "bold"))
            answersLbl.grid(row=rowAdjuster + 4, column=0, columnspan=6, sticky=W)


            self.correctAnsA = BooleanVar()
            self.correctAnsB = BooleanVar()
            self.correctAnsC = BooleanVar()
            self.correctAnsD = BooleanVar()

            ansA = Checkbutton(self.frame, text="A.", font=("Arial", 10, "bold"), variable=self.correctAnsA)
            ansA.grid(row=rowAdjuster + 5, column=0, sticky=E)

            ansFieldA = Entry(self.frame)
            ansFieldA.grid(row=rowAdjuster + 5, column=1, ipadx="100", sticky=W, columnspan=3)

            ansAcommentlbl = Label(self.frame, text="Answer Comments:")
            ansAcommentlbl.grid(row=rowAdjuster + 6, column=0, rowspan=2, sticky=NE)

            self.ansAcomment = Text(self.frame, height=2, width =40)
            self.ansAcomment.grid(row=rowAdjuster + 6, column=1, sticky=W, columnspan=3)


            ansB = Checkbutton(self.frame, text="B.", font=("Arial", 10, "bold"), variable=self.correctAnsB)
            ansB.grid(row=rowAdjuster + 7, column=0, sticky=E)

            ansFieldB = Entry(self.frame)
            ansFieldB.grid(row=rowAdjuster + 7, column=1, ipadx="100", sticky=W)


            #print(self.correctAns.get())
            #print(ansA.cget("text"))
            ansBcommentlbl = Label(self.frame, text="Answer Comments:")
            ansBcommentlbl.grid(row=rowAdjuster + 8, column=0, rowspan=2, sticky=NE)

            self.ansBcomment = Text(self.frame, height=2, width =40)
            self.ansBcomment.grid(row=rowAdjuster + 8, column=1, sticky=W, columnspan=3)

            ansC = Checkbutton(self.frame, text="C.", font=("Arial", 10, "bold"), variable=self.correctAnsC)
            ansC.grid(row=rowAdjuster + 9, column=0, sticky=E)

            ansFieldC = Entry(self.frame)
            ansFieldC.grid(row=rowAdjuster + 9, column=1, ipadx="100", sticky=W, columnspan=3)

            ansCcommentlbl = Label(self.frame, text="Answer Comments:")
            ansCcommentlbl.grid(row=rowAdjuster + 10, column=0, rowspan=2, sticky=NE)

            self.ansCcomment = Text(self.frame, height=2, width =40)
            self.ansCcomment.grid(row=rowAdjuster + 10, column=1, sticky=W, columnspan=3)

            ansD = Checkbutton(self.frame, text="D.", font=("Arial", 10, "bold"), variable=self.correctAnsD)
            ansD.grid(row=rowAdjuster + 11, column=0, sticky=E)

            ansFieldD = Entry(self.frame)
            ansFieldD.grid(row=rowAdjuster + 11, column=1, ipadx="100", sticky=W, columnspan=3)

            ansDcommentlbl = Label(self.frame, text="Answer Comments:")
            ansDcommentlbl.grid(row=rowAdjuster + 12, column=0, rowspan=2, sticky=NE)

            self.ansDcomment = Text(self.frame, height=2, width =40)
            self.ansDcomment.grid(row=rowAdjuster + 12, column=1, sticky=W, columnspan=3)

            new_line = Label(self.frame, text="-" * 100)
            new_line.grid(row=rowAdjuster +13, column=0, columnspan=4, sticky=NSEW)


            self.test_entries.setdefault(questionLbl.cget("text").replace(":", ""), questionField)

            self.question_entries.append(questionField)

            self.answers_entriesA.append(ansFieldA)
            self.answers_entriesB.append(ansFieldB)
            self.answers_entriesC.append(ansFieldC)
            self.answers_entriesD.append(ansFieldD)

            self.correctAnsA_entries.append(self.correctAnsA)
            self.correctAnsB_entries.append(self.correctAnsB)
            self.correctAnsC_entries.append(self.correctAnsC)
            self.correctAnsD_entries.append(self.correctAnsD)

            self.ansAcomment_entries.append(self.ansAcomment)
            self.ansBcomment_entries.append(self.ansBcomment)
            self.ansCcomment_entries.append(self.ansCcomment)
            self.ansDcomment_entries.append(self.ansDcomment)

            rowAdjuster += 13

    def frameConfigure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))


    def storeTest(self):

        self.test_name = rmv_extra_spaces(self.testNameField.get())

        iter_questions = iter(self.question_entries)

        iter_answers_entriesA = iter(self.answers_entriesA)
        iter_answers_entriesB = iter(self.answers_entriesB)
        iter_answers_entriesC = iter(self.answers_entriesC)
        iter_answers_entriesD = iter(self.answers_entriesD)

        iter_correctAnsA_entries = iter(self.correctAnsA_entries)
        iter_correctAnsB_entries = iter(self.correctAnsB_entries)
        iter_correctAnsC_entries = iter(self.correctAnsC_entries)
        iter_correctAnsD_entries = iter(self.correctAnsD_entries)

        iter_ansAcomment_entries = iter(self.ansAcomment_entries)
        iter_ansBcomment_entries = iter(self.ansBcomment_entries)
        iter_ansCcomment_entries = iter(self.ansCcomment_entries)
        iter_ansDcomment_entries = iter(self.ansDcomment_entries)

        for e, a in self.test_entries.items():

            self.test_entries[e] = {e: rmv_extra_spaces(next(iter_questions).get()), "answer_choices": {
                "A":rmv_extra_spaces(next(iter_answers_entriesA).get()), "B":rmv_extra_spaces(next(iter_answers_entriesB).get()),
                "C":rmv_extra_spaces(next(iter_answers_entriesC).get()), "D":rmv_extra_spaces(next(iter_answers_entriesD).get())}, "is_correct_answer": {
                "A":next(iter_correctAnsA_entries).get(), "B":next(iter_correctAnsB_entries).get(), "C":next(iter_correctAnsC_entries).get(),
                "D":next(iter_correctAnsD_entries).get()}, "answer_feedback": {
                "A":next(iter_ansAcomment_entries).get(1.0,END), "B":next(iter_ansBcomment_entries).get(1.0,END),
                "C":next(iter_ansCcomment_entries).get(1.0,END),"D":next(iter_ansDcomment_entries).get(1.0,END)}}

        error_msgs = ""
        
        for i in range(len(self.test_entries)):
            if self.test_entries["Question " + str(i +1)]["Question " + str(i +1)] == '':
                error_msgs += "Question %d: Please enter a question\n"%(i+1)
            if self.test_entries["Question " + str(i +1)]["is_correct_answer"] == {'A': False, 'B': False, 'C': False, 'D': False}:
                error_msgs += "Question %d: Please select the correct answers\n"%(i+1)
            if self.test_entries["Question " + str(i +1)]["answer_choices"] == {'A': '', 'B': '', 'C': '', 'D': ''}:
                error_msgs += "Question %d: Please enter answer choices\n"%(i+1)
            if self.test_entries["Question " + str(i +1)]["answer_choices"]['A'] == '' and self.test_entries["Question " + str(i +1)]["answer_choices"]['B'] != '' and self.test_entries["Question " + str(i +1)]["answer_choices"]['C'] != '' and self.test_entries["Question " + str(i +1)]["answer_choices"]['D'] != '':
                error_msgs += "Question %d: Answer A must not be blank\n"%(i+1)
            if self.test_entries["Question " + str(i +1)]["answer_choices"]['A'] == '' and self.test_entries["Question " + str(i +1)]["answer_choices"]['B'] != '' and self.test_entries["Question " + str(i +1)]["answer_choices"]['C'] != '' and self.test_entries["Question " + str(i +1)]["answer_choices"]['D'] == '':
                error_msgs += "Question %d: Answer A must not be blank\n"%(i+1)
            if self.test_entries["Question " + str(i +1)]["answer_choices"]['A'] == '' and self.test_entries["Question " + str(i +1)]["answer_choices"]['B'] != '' and self.test_entries["Question " + str(i +1)]["answer_choices"]['C'] == '' and self.test_entries["Question " + str(i +1)]["answer_choices"]['D'] == '':
                error_msgs += "Question %d: Answer A must not be blank\n"%(i+1)
            if self.test_entries["Question " + str(i +1)]["answer_choices"]['B'] == '' and self.test_entries["Question " + str(i +1)]["answer_choices"]['A'] != '' and self.test_entries["Question " + str(i +1)]["answer_choices"]['C'] != '' and self.test_entries["Question " + str(i +1)]["answer_choices"]['D'] != '':
                error_msgs += "Question %d: Answer B must not be blank\n"%(i+1)
            if self.test_entries["Question " + str(i +1)]["answer_choices"]['B'] == '' and self.test_entries["Question " + str(i +1)]["answer_choices"]['A'] != '' and self.test_entries["Question " + str(i +1)]["answer_choices"]['C'] != '' and self.test_entries["Question " + str(i +1)]["answer_choices"]['D'] == '':
                error_msgs += "Question %d: Answer B must not be blank\n"%(i+1)
            if self.test_entries["Question " + str(i +1)]["answer_choices"]['B'] == '' and self.test_entries["Question " + str(i +1)]["answer_choices"]['A'] != '' and self.test_entries["Question " + str(i +1)]["answer_choices"]['C'] == '' and self.test_entries["Question " + str(i +1)]["answer_choices"]['D'] == '':
                error_msgs += "Question %d: Answer B must not be blank\n"%(i+1)
            if self.test_entries["Question " + str(i +1)]["answer_choices"]['C'] == '' and self.test_entries["Question " + str(i +1)]["answer_choices"]['A'] != '' and self.test_entries["Question " + str(i +1)]["answer_choices"]['B'] != '' and self.test_entries["Question " + str(i +1)]["answer_choices"]['D'] != '':
                error_msgs += "Question %d: Answer C must have input if adding answer for D\n"%(i+1)
                
        if error_msgs != "":
            tkinter.messagebox.showwarning("Entry Error", error_msgs)
            return

        if self.check_testName() is True:

            with open(self.test_name + '.csv', 'w') as csvfile:

                fieldnames = ["question_no", "question", "answer_choices", "is_correct_answer", "answer_feedback"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()

                for key, value in self.test_entries.items():
                    writer.writerow({'question_no': key, 'question':value[key], 'answer_choices':value["answer_choices"],
                                    'is_correct_answer':value['is_correct_answer'], 'answer_feedback':value['answer_feedback']})


                tkinter.messagebox.showinfo("Test Created Successfully","Test " + self.test_name + " has been successfully created and can now be found under \"My Saved Test\"")

                newPage(self, LecturerMenu, "Lecturer Page", self.lecturerID)



    def check_testName(self):

        if self.test_name == "":
            tkinter.messagebox.showwarning("Entry Error", "Please enter a test name")
            return False

        #tempfile = NamedTemporaryFile(mode="w", delete=False)
        tempfile = open("lecturers.tmp", "w")

        lectfile = "lecturers.csv"
        with open(lectfile, 'r') as csvfile, tempfile:
            fieldnames = ["lecturerID", "saved_test", "student_cohort"]

            reader = csv.DictReader(csvfile, fieldnames=fieldnames)
            writer = csv.DictWriter(tempfile, fieldnames=fieldnames)

            for row in reader:
                if row["lecturerID"] == self.lecturerID:
                    if self.test_name not in ast.literal_eval(row["saved_test"]):

                        into_list = ast.literal_eval(row["saved_test"])
                        into_list.append(self.test_name)

                        row["saved_test"] = into_list
                    else:
                        tkinter.messagebox.showwarning("Entry Error", "Please choose a different test name")
                        return False
                row = {"lecturerID": row["lecturerID"], "saved_test":row["saved_test"], "student_cohort":row["student_cohort"]}

                writer.writerow(row)

        #shutil.move(tempfile.name, lectfile)


        remove('lecturers.csv')
        rename('lecturers.tmp', 'lecturers.csv')

        return True

class SavedTest(Frame):

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
        master.grid_rowconfigure(2, weight = 1)
        #master.grid_rowconfigure(6, weight = 1)
        master.grid_rowconfigure(12, weight=5)

        self.lecturerID = args[0]

        self.test_list()

    def test_list(self):

        #lecturerID = "100000"

        test_names = []

        with open("lecturers.csv", "r") as csvfile:
            fieldnames = ["lecturerID", "saved_test", "student_cohort"]
            reader = csv.DictReader(csvfile, fieldnames = fieldnames)

            for row in reader:
                if row["lecturerID"] == self.lecturerID:
                    test_names = sorted(ast.literal_eval(row["saved_test"]))

        row_adjuster = 0

        self.getTestName = StringVar()
        self.getTestName.set(' ')

        if len(test_names) == 0:
            empty_testlbl = Label(text="Your dont have any saved test", font=("Arial", 14, "bold"))
            empty_testlbl.grid(row=4, column=1, columnspan=6, rowspan=2, sticky=NSEW)

        else:
            for i, item in enumerate(test_names):
                #testNamelbl = Label(text= str(i + 1) + ". " + item)
                #testNamelbl.grid(row= row_adjuster + 3, column=2, columnspan=3, sticky=W)

                #testName_button = Radiobutton(value=item, variable=self.getTestName)
                #testName_button.grid(row=row_adjuster + 3, column=1, sticky=E)

                testName_button = Radiobutton(value=item, text=str(i + 1) + ". " + item, variable=self.getTestName)
                testName_button.grid(row=row_adjuster + 3, column=1, columnspan=4, sticky=W)


                row_adjuster += 1

        releaseFormative_button = Button(text="Release as Formative Test",width=20, command=self.formative_selection)
        releaseFormative_button.grid(row=1, column=1, sticky=NSEW)

        releaseSummative_button = Button(text="Release as Summative Test",width=20, command=self.summative_selection)
        releaseSummative_button.grid(row=1, column=4, sticky=NSEW)

        goBack_button = Button(text="Go Back to Homepage", width=20, command=lambda:newPage(self, LecturerMenu, "Lecturer Page", self.lecturerID))
        goBack_button.grid(row=1, column=6, sticky=NSEW)

        new_line = Label(text=" ")
        new_line.grid(row=3)

        noQuestion_label = Label(text="Select the test that you wish to release to students.", font=("bold"))
        noQuestion_label.grid(row=2, rowspan=1, column=1, columnspan=6, sticky=NSEW)

    def formative_selection(self):
        if self.getTestName.get() == ' ':
            tkinter.messagebox.showwarning("Entry Error", "Please choose a test to release")
        else:
            newPage(self, ReleaseFormative, "Formative Test Settings", self.lecturerID, self.getTestName.get())

    def summative_selection(self):
        if self.getTestName.get() == ' ':
            tkinter.messagebox.showwarning("Entry Error", "Please choose a test to release")
        else:
            newPage(self, ReleaseSummative, "Summative Test Settings", self.lecturerID, self.getTestName.get())


    def frameConfigure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

class ReleaseFormative(Frame):

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

        self.test_name = args[1]

        self.lecturerID = args[0]

        test_settings(self, self.test_name, self.lecturerID, "formative test")

        self.max_attempt()

    def go_back(self):

        newPage(self, LecturerMenu, "Lecturer Page", self.lecturerID)

    def max_attempt(self):

        max_attempt_lbl = Label(text="Maximum number of attempts\nallowed to students to take this test:")
        max_attempt_lbl.grid(row=3, rowspan=2, column=1, columnspan=6, sticky=NSEW)

        max_attempt_list = ["Unlimited"] + list(map(str, range(1,11)))

        self.max_attemptNumber = StringVar(self.master)
        self.max_attemptNumber.set(max_attempt_list[0])

        max_attemptNumber_option = OptionMenu(self.master, self.max_attemptNumber, *max_attempt_list)
        max_attemptNumber_option.grid(row=5, column=4, sticky=NSEW)

    def release_test(self):

        released_date = currentDate().strftime("%d/%m/%Y")

        error_msg = ""


        if self.getStudent_cohorts.get() == ' ':
            error_msg = "Please select the students cohort\nto whom this test will be released to\n\n"

        if self.test_duration.get() not in self.test_duration_list:
            error_msg = error_msg + "Please choose test duration to be either Untimed\nor between values " + str(self.test_duration_list[1]) + " and " + str(self.test_duration_list[-1])

        if len(error_msg) > 0:
            tkinter.messagebox.showwarning("Entry Error", error_msg)
            return

        check_if_exist = os.path.isfile("ReleasedFormative.csv")

        if not check_if_exist:
            with open('ReleasedFormative.csv', 'w') as csvfile:

                fieldnames = ["test_name", "student_maxAttempt", "test_duration", "date_released", "released_by", "released_to"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()

        with open('ReleasedFormative.csv', 'r') as csvfile:

            fieldnames = ["test_name", "student_maxAttempt", "test_duration", "date_released", "released_by", "released_to"]
            reader = csv.DictReader(csvfile, fieldnames = fieldnames)

            for row in reader:
                if row["released_by"] == self.lecturerID and row["test_name"] == self.test_name and row["released_to"] == self.getStudent_cohorts.get():
                    tkinter.messagebox.showwarning("Entry Error", "This test is already on released to " + self.getStudent_cohorts.get() + " students")
                    return

        with open('ReleasedFormative.csv', 'a+') as csvfile:

            fieldnames = ["test_name", "student_maxAttempt", "test_duration", "date_released", "released_by", "released_to"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if not check_if_exist:
                writer.writeheader()

            writer.writerow({"test_name": self.test_name, "student_maxAttempt": self.max_attemptNumber.get(), "test_duration": self.test_duration.get(),
                             "date_released": released_date, "released_by": self.lecturerID, "released_to": self.getStudent_cohorts.get()})

        tkinter.messagebox.showinfo("Test Release", self.test_name.upper() + " is now released as a formative assessment test to " + self.getStudent_cohorts.get() + " students")

        newPage(self, LecturerMenu, "Lecturer Page", self.lecturerID)

class ReleaseSummative(Frame):

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

        self.test_name = args[1]

        self.lecturerID = args[0]

        test_settings(self, self.test_name, self.lecturerID, "summative test")

        self.test_deadline()

    def go_back(self):

        newPage(self, LecturerMenu, "Lecturer Page", self.lecturerID)

    def test_deadline(self):

        test_deadline_lbl = Label(text="Test Deadline:")
        test_deadline_lbl.grid(row=3, rowspan=2, column=1, columnspan=6, sticky=NSEW)

        self.date_picker = DateEntry(self.master, width=12, borderwidth=1, year=2019, firstweekday="sunday", showweeknumbers=False)
        self.date_picker.grid(row=5, column=4, sticky=NSEW)

        #test_deadline_list = ["Unlimited"] + list(map(str, range(1,11)))

        #self.test_deadlineDate = StringVar(self.master)
        #self.test_deadlineDate.set(max_attempt_list[0])

        #test_deadlineDate_option = OptionMenu(self.master, self.test_deadlineDate, *test_deadline_list)
        #test_deadlineDate_option.grid(row=5, column=4, sticky=NSEW)

    def release_test(self):

        released_date = currentDate().strftime("%d/%m/%Y")

        deadline_date = str(self.date_picker.get_date())

        test_deadline = self.date_picker.get_date().strftime("%d/%m/%Y")

        today = date.today().isoformat()

        tomorrow = (date.today() + timedelta(days=1)).strftime("%B %d, %Y")

        error_msg = ""

        if today >= deadline_date:
            error_msg = "Test deadline must be from tomorrow,\n" + tomorrow + " onwards\n\n"

        if self.getStudent_cohorts.get() == ' ':
            error_msg = error_msg + "Please select the students cohort\nto whom this test will be released to\n\n"

        if self.test_duration.get() not in self.test_duration_list:
            error_msg = error_msg + "Please choose test duration to be either Untimed\nor between values " + str(self.test_duration_list[1]) + " and " + str(self.test_duration_list[-1])

        if len(error_msg) > 0:
            tkinter.messagebox.showwarning("Entry Error", error_msg)
            return

        check_if_exist = os.path.isfile("ReleasedSummative.csv")

        if not check_if_exist:
            with open('ReleasedSummative.csv', 'w') as csvfile:

                fieldnames = ["test_name", "test_deadline", "test_duration", "date_released", "released_by", "released_to"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()

        with open('ReleasedSummative.csv', 'r') as csvfile:

            fieldnames = ["test_name", "test_deadline", "test_duration", "date_released", "released_by", "released_to"]
            reader = csv.DictReader(csvfile, fieldnames = fieldnames)

            for row in reader:
                if row["released_by"] == self.lecturerID and row["test_name"] == self.test_name and row["released_to"] == self.getStudent_cohorts.get():
                    tkinter.messagebox.showwarning("Entry Error", "This test is already on released to " + self.getStudent_cohorts.get() + " students")
                    return

        with open('ReleasedSummative.csv', 'a+') as csvfile:

            fieldnames = ["test_name", "test_deadline", "test_duration", "date_released", "released_by", "released_to"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if not check_if_exist:
                writer.writeheader()

            writer.writerow({"test_name": self.test_name, "test_deadline": test_deadline, "test_duration": self.test_duration.get(),
                             "date_released": released_date, "released_by": self.lecturerID, "released_to": self.getStudent_cohorts.get()})

        tkinter.messagebox.showinfo("Test Release", self.test_name.upper() + " is now released as a summative assessment test to " + self.getStudent_cohorts.get() + " students")

        newPage(self, LecturerMenu, "Lecturer Page", self.lecturerID)

class ReleasedFormativeTest(Frame):

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

        self.lecturerID = args[0]

        self.display_released_formative()

    def display_released_formative(self):

        formative_list = []

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
                if row["released_by"] == self.lecturerID:
                    formative_list.append({"test_name": row["test_name"], "released_to": row["released_to"], "date_released": row["date_released"]})

        row_adjuster = 0

        self.getTestName = StringVar()
        self.getTestName.set(' ')

        if len(formative_list) == 0:
            empty_testlbl = Label(text="You haven't released any formative test", font=("Arial", 14, "bold"))
            empty_testlbl.grid(row=4, column=1, columnspan=6, rowspan=2, sticky=NSEW)

        else:

            test_name_heading = Label(text="Name of Test", font=("MS", 10, "bold"))
            test_name_heading.grid(row=3, column=1, columnspan=2, sticky=NSEW)

            released_to_heading = Label(text="Released To", font=("MS", 10, "bold"))
            released_to_heading.grid(row=3, column=4, sticky=NSEW)

            date_released_heading = Label(text="Date Released", font=("MS", 10, "bold"))
            date_released_heading.grid(row=3, column=6, sticky=NSEW)

            for i, item in enumerate(formative_list):

                testName_button = Radiobutton(value='[\'' + item["released_to"] + "\', " + "\'" + item["test_name"] +  "\', \'"
                                              + item["date_released"] + '\']', text=str(i + 1) + ". " + item["test_name"], variable=self.getTestName)
                testName_button.grid(row=row_adjuster + 4, column=1, sticky=W)

                released_to_lbl = Label(text=item["released_to"])
                released_to_lbl.grid(row=row_adjuster + 4, column=4, sticky=NSEW)

                date_released_lbl = Label(text=item["date_released"])
                date_released_lbl.grid(row=row_adjuster + 4, column=6, sticky=NSEW)

                row_adjuster += 1

        goBack_button = Button(text="Go Back to Homepage", width=20, command=lambda:newPage(self, LecturerMenu, "Lecturer Page", self.lecturerID))
        goBack_button.grid(row=1, column=1, sticky=NSEW)

        view_stats_button = Button(text="View Test Statistics", width=20, command=self.view_stats)
        view_stats_button.grid(row=1, column=6, sticky=NSEW)

        Heading_lbl = Label(text="Formative Test On Released", font=("bold"))
        Heading_lbl.grid(row=2, column=1, columnspan=6, sticky=NSEW)

    def view_stats(self):

        test_name = self.getTestName.get()

        if test_name != ' ':
            test_name = ast.literal_eval(self.getTestName.get())

        #testName = " ".join(test_name.split()[1:])


        print(test_name)

        if test_name == ' ':
            tkinter.messagebox.showwarning("Entry Error", "Please select a test to view statistics")
            return
        else:
            #Change Class Name and Window Title and pass testName
            newPage(self, DisplayFormativeStatistics, "Formative Test Statistics", self.lecturerID, test_name)

class DisplayFormativeStatistics(Frame):
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

        master.grid_rowconfigure(0, weight=1)
        master.grid_rowconfigure(2, weight=2)
        # master.grid_rowconfigure(6, weight = 1)
        master.grid_rowconfigure(14, weight=5)
        
        self.lecturerID = args[0]
        self.group = args[1][0]
        self.test_name = args[1][1]
        self.date_released = args[1][2]
        
        self.display()
        
    def display(self):
        submissions = []
        
        with open('formativeStudentResults.csv', 'r') as csvfile:
        
            fieldnames = ['test_name', 'studentID', 'studentGroup', 'date_released', 'attempts_made', 'total_score', 'total_question', 'answered_correctly']
            reader = csv.DictReader(csvfile, fieldnames = fieldnames)
            for row in reader:
                if self.group == row['studentGroup'] and self.test_name == row['test_name'] and self.date_released == row['date_released']:
                    submissions.append({"attempts_made": row["attempts_made"], "total_score": row["total_score"], "total_question": row["total_question"], "answered_correctly": row["answered_correctly"]})
        
        row_adjuster = 0
        
        test_name_title_lbl = Label(text=self.test_name, font=("Arial", 14, "bold"))
        test_name_title_lbl.grid(row = 2, column = 1, columnspan=6, sticky = NSEW)
        
        if len(submissions) == 0:
            empty_testlbl = Label(text="There have been no submissions made for this test.", font=("Arial", 14, "bold"))
            empty_testlbl.grid(row=4, column=1, columnspan=6, rowspan=2, sticky=NSEW)
        else:
            #attaining the total marks of all students, total number of attempts and number of students answering each Q correctly etc for statistics
            max_mark = int(submissions[0]['total_question'])
            sum_score = 0
            sum_attempts = 0
            no_correct_per_q = {}
        
            for submission in submissions:
                sum_score += int(submission['total_score'])
                sum_attempts += int(submission['attempts_made'])
        
                answered_correctly = submission['answered_correctly']
                for Qnumber, correctBool in ast.literal_eval(answered_correctly).items():
                    if correctBool:
                        if Qnumber in no_correct_per_q:
                            no_correct_per_q[Qnumber] += 1
                        else:
                            no_correct_per_q[Qnumber] = 1
                    else:
                        if Qnumber not in no_correct_per_q:
                            no_correct_per_q[Qnumber] = 0
            
            question_most_correct = max(no_correct_per_q.items(), key=operator.itemgetter(1))[0]
            question_least_correct = min(no_correct_per_q.items(), key=operator.itemgetter(1))[0]
            ave_score = round(sum_score / len(submissions), 1)
            ave_percentage_attainded = round((ave_score / max_mark) * 100, 1)
            ave_no_of_attempts = round(sum_attempts / len(submissions), 1)
            
            percent_correct_per_q = {}
            for question, number in no_correct_per_q.items():
                percent_correct = (number / len(submissions)) * 100
                percent_correct_per_q[question] = round(percent_correct, 1)
            
            no_submissions_lbl = Label(text = "Number of submissions recieved:   {length}".format(length=len(submissions)), font=("Arial", 10))
            no_submissions_lbl.grid(row = 3, column = 1, sticky = NSEW)
            
            ave_attempts_lbl = Label(text = "Average number of attempts:   {attempts}".format(attempts=ave_no_of_attempts), font=("Arial",10))
            ave_attempts_lbl.grid(row = 4, column = 1, sticky = NSEW)
            
            ave_score_lbl = Label(text = "Average score in test:   {score}/{max}  ({percent}%)".format(score=ave_score, max=max_mark, percent=ave_percentage_attainded), font=("Arial",10))
            ave_score_lbl.grid(row = 5, column = 1, sticky = NSEW)
            
            most_correct_lbl = Label(text = "Qustion with most correct answers:   {question}".format(question=question_most_correct), font=("Arial",10))
            most_correct_lbl.grid(row = 6, column = 1, sticky = NSEW)
            
            least_correct_lbl = Label(text = "Question with least correct answers:   {question}".format(question=question_least_correct), font=("Arial",10))
            least_correct_lbl.grid(row = 7, column = 1, sticky = NSEW)
            
            percent_correct_lbl = Label(text = "Percent of students who answered each question correctly:", font=("Arial",10))
            percent_correct_lbl.grid(row = 8, column = 1, sticky = NSEW)
            row_adjuster = 9
            for question, percent in percent_correct_per_q.items():
                percentage_for_q_lbl = Label(text = "{q}:  {p}%".format(q=question, p=percent), font=("Arial",10))
                percentage_for_q_lbl.grid(row = row_adjuster, column = 1, sticky = NSEW)
                
                row_adjuster += 1
            
            home_but = Button(text="Back to Homepage", width=20, command=lambda:newPage(self, LecturerMenu, "Lecturer Page", self.lecturerID))
            home_but.grid(row=1, column=1, sticky=NSEW)
            back_to_formative_but = Button(self, text="Back to Formative Tests", width=20, command=lambda:newPage(self, ReleasedFormativeTest, "Released Formative Test", self.lecturerID))
            back_to_formative_but.grid(row=1, column=6)
            
class ReleasedSummativeTest(Frame):

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

        self.lecturerID = args[0]

        self.display_released_summative()

    def display_released_summative(self):

        summative_list = []

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
                if row["released_by"] == self.lecturerID:
                    summative_list.append({"test_name": row["test_name"], "released_to": row["released_to"],
                                           "date_released": row["date_released"], "test_deadline": row["test_deadline"]})

        row_adjuster = 0

        self.getTestName = StringVar()
        self.getTestName.set(' ')

        if len(summative_list) == 0:
            empty_testlbl = Label(text="You haven't released any summative test", font=("Arial", 14, "bold"))
            empty_testlbl.grid(row=4, column=1, columnspan=6, rowspan=2, sticky=NSEW)

        else:
            test_name_heading = Label(text="Name of Test", font=("MS", 10, "bold"))
            test_name_heading.grid(row=3, column=1, columnspan=2, sticky=NSEW)

            released_to_heading = Label(text="Released To", font=("MS", 10, "bold"))
            released_to_heading.grid(row=3, column=3, sticky=NSEW)

            date_released_heading = Label(text="Date Released", font=("MS", 10, "bold"))
            date_released_heading.grid(row=3, column=5, sticky=NSEW)

            test_deadline_heading = Label(text="Deadline", font=("MS", 10, "bold"))
            test_deadline_heading.grid(row=3, column=6, sticky=NSEW)

            for i, item in enumerate(summative_list):

                testName_button = Radiobutton(value='\"[\'' + item["released_to"] + "\', \'" + item["test_name"] +  "\', \'"
                                              + item["date_released"] + "\', \'" + item["test_deadline"] + '\']\"', text=str(i + 1) + ". " + item["test_name"], variable=self.getTestName)
                testName_button.grid(row=row_adjuster + 4, column=1, sticky=W)

                released_to_lbl = Label(text=item["released_to"])
                released_to_lbl.grid(row=row_adjuster + 4, column=3, sticky=NSEW)

                date_released_lbl = Label(text=item["date_released"])
                date_released_lbl.grid(row=row_adjuster + 4, column=5, sticky=NSEW)

                test_deadline_lbl = Label(text=item["test_deadline"])
                test_deadline_lbl.grid(row=row_adjuster + 4, column=6, sticky=NSEW)


                row_adjuster += 1

        goBack_button = Button(text="Go Back to Homepage", width=20, command=lambda:newPage(self, LecturerMenu, "Lecturer Page", self.lecturerID))
        goBack_button.grid(row=1, column=1, sticky=NSEW)

        view_stats_button = Button(text="View Test Result", width=20, command=self.view_results)
        view_stats_button.grid(row=1, column=6, sticky=NSEW)

        Heading_lbl = Label(text="Released Summative Test", font=("bold"))
        Heading_lbl.grid(row=2, column=1, columnspan=6, sticky=NSEW)

    def view_results(self):
        # test_deadline = self.getTestDeadline.get()
        # print(test_deadline)
        summative_list =[]
        with open("ReleasedSummative.csv", "r") as csvfile:
                    fieldnames = ["test_name", "test_deadline", "test_duration", "date_released", "released_by", "released_to"]
                    reader = csv.DictReader(csvfile, fieldnames = fieldnames)
        
                    for row in reader:
                        if row["released_by"] == self.lecturerID:
                            summative_list.append({"test_name": row["test_name"], "released_to": row["released_to"],
                                           "date_released": row["date_released"], "test_deadline": row["test_deadline"]})
        today = date.today().isoformat()
        today = today.split("-")
        today = today[0].translate(str.maketrans('', '', string.punctuation)) + today[1].translate(str.maketrans('', '', string.punctuation)) + today[2].translate(str.maketrans('', '', string.punctuation))
        print(today)
        test_name = ast.literal_eval(self.getTestName.get())
        test_name = test_name.split()
        deadline = test_name[4].translate(str.maketrans('', '', string.punctuation))
        deadline = deadline[4:8] + deadline[2:4] + deadline[0:2]
        test_title = test_name[2].translate(str.maketrans('', '', string.punctuation))

        for item in summative_list:
            if item["test_name"] == test_title:
                print(today)
                print(deadline)
                if today <= deadline:
                    print("error")
                    error_msg = "Test hasnt passed its deadline"
                    tkinter.messagebox.showwarning("Entry Error", error_msg)
                    return

        

        if test_name != ' ':
            test_name = ast.literal_eval(self.getTestName.get())

        print(test_name)

        if test_name == ' ':
            tkinter.messagebox.showwarning("Entry Error", "Please select a test in order to view its result")
            return
        newPage(self, DisplayStudentPerformance,"Display Student performance", self.lecturerID, test_name)


class DisplayStudentPerformance(Frame):
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
        self.test_name = args[1]
        self.lecturerID = args[0]
        self.display()
        # self.display_completed_tests()

    def display(self):
        studentList =[]

        with open('studentResults.csv', 'r') as csvfile:
            fieldnames = ["studentID", "studentGroup", "test_name", "date_released", "deadline", "total_score", "total_question", "student_f_name", "student_l_name"]
            reader = csv.DictReader(csvfile, fieldnames = fieldnames)
            test_name_list = self.test_name.split()

            group = test_name_list[0].translate(str.maketrans('', '', string.punctuation))
            groupNum = test_name_list[1].translate(str.maketrans('', '', string.punctuation))
            testNameTitle = test_name_list[2].translate(str.maketrans('', '', string.punctuation))

            for row in reader:
                if group + " " + groupNum == row["studentGroup"] and testNameTitle == row["test_name"]:
                    studentList.append({"studentID": row["studentID"], "studentGroup": row["studentGroup"], "test_name": row["test_name"],"total_score": row["total_score"],"total_question": row["total_question"], "student_f_name": row["student_f_name"], "student_l_name": row["student_l_name"] })

        row_adjuster = 0


        if len(studentList) == 0:
            empty_testlbl = Label(text="No students have taken this test yet.", font=("Arial", 14, "bold"))
            empty_testlbl.grid(row=4, column=1, columnspan=6, rowspan=2, sticky=NSEW)

        else:
            for i, item in enumerate(studentList):
                released_to_lbl = Label(text=item["student_f_name"] + " " + item["student_l_name"]  + " Mark: " + item["total_score"]  + "/" + item["total_question"]  )
                released_to_lbl.grid(row=row_adjuster + 4, column=1, sticky=NSEW)

                released_to_but = Button(text="View Student", width=15, command=lambda:newPage(self, DisplayIndividualStudentPerformance, "Individual Student Performance", self.lecturerID, item) )
                released_to_but.grid(row=row_adjuster + 4, column=3, sticky=NSEW)
                row_adjuster += 1

        goBack_button = Button(text="Go Back to Homepage", width=20, command=lambda:newPage(self, LecturerMenu, "Lecturer Page", self.lecturerID))
        goBack_button.grid(row=1, column=1, sticky=NSEW)

        Heading_lbl = Label(text=testNameTitle, font=("bold"))
        Heading_lbl.grid(row=2, column=1, columnspan=6, sticky=NSEW)


class DisplayIndividualStudentPerformance(Frame):
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
        self.student_details = args[1]
        self.lecturerID = args[0]
        self.display()

    def display(self):
        row_adjuster = 0
        goBack_button = Button(text="Go Back to Homepage", width=20, command=lambda:newPage(self, LecturerMenu, "Lecturer Page", self.lecturerID))
        goBack_button.grid(row=1, column=1, sticky=NSEW)
        firstName = list(self.student_details.values())[5]
        secondName = list(self.student_details.values())[6]
        Heading_lbl = Label(text=firstName + " " + secondName, font=("bold"))
        Heading_lbl.grid(row=2, column=1, columnspan=6, sticky=NSEW)

        testList=[]
        with open('studentResults.csv', 'r') as csvfile:
            fieldnames = ["studentID", "studentGroup", "test_name", "date_released", "deadline", "total_score", "total_question", "student_f_name", "student_l_name"]
            reader = csv.DictReader(csvfile, fieldnames = fieldnames)

            for row in reader:
                if row["student_f_name"] == firstName:
                    testList.append({"studentID": row["studentID"], "studentGroup": row["studentGroup"], "test_name": row["test_name"],"total_score": row["total_score"],"total_question": row["total_question"], "student_f_name": row["student_f_name"], "student_l_name": row["student_l_name"] })


        if len(testList) == 0:
            empty_testlbl = Label(text="This student has taken no summative tests yet.", font=("Arial", 14, "bold"))
            empty_testlbl.grid(row=4, column=1, columnspan=6, rowspan=2, sticky=NSEW)
        else:
            for i, item in enumerate(testList):
                released_to_lbl = Label(text=item["test_name"] + " "  + " Mark: " + item["total_score"]  + "/" + item["total_question"]  )
                released_to_lbl.grid(row=row_adjuster + 4, column=1, sticky=NSEW)



root = Tk()
app = LecturerMenu(root)
root.mainloop()

