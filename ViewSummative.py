from tkinter import *
from globalFunctions import *
import csv
import os
import glob


class SummativeMenu(Frame):

    def __init__(self, master, *args):

        Frame.__init__(self, master)
        self.grid()
        master.title("Summative Test Menu")

        width = 400
        height = 300

        centred_window = centre_app(master, width, height)

        master.geometry(centred_window)

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        master.grid_columnconfigure(3, weight=1)
        master.grid_rowconfigure(4, weight=1)

        self.student_id = args[0]
        self.createButtons()

    def createButtons(self):

        btnViewTest = Button(self, text = "View Summative Tests", command=lambda:newPage(self, ViewSummative, "Summative Test List"))
        btnViewTest.grid(row=0, column=0)

        btnViewResults = Button(self, text = "View Summative Results")
        btnViewResults.grid(row=1, column=0)

        btnBack = Button(self, text = "Back", command=lambda:newPage(self, StudentMenu, "Student Menu"))
        btnBack.grid(row=2, column=0)


class ViewSummative(Frame):
    def __init__(self, master, *args):

        Frame.__init__(self, master)
        self.grid()
        master.title("Summative Test List")

        #codes to centre the app on the screen
        width = 400
        height = 300

        centred_window = centre_app(master, width, height)
        
        master.geometry(centred_window)

        #codes to centre the contents on the window
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight = 1)
        master.grid_columnconfigure(3, weight=1)
        master.grid_rowconfigure(4, weight = 1)

        
        #self.user_id = args[0]
        self.user_id="110000"
        self.CreateList()
    def CreateList(self):
        path = os.getcwd()
        #Code adapted from: https://stackoverflow.com/questions/9234560/find-all-csv-files-in-a-directory-using-python/12280052
        #Used to search for the available csv files in the dir.
        ext = 'csv'
        os.chdir(path)
        tests = [i for i in glob.glob('*.{}'.format(ext))]
        #End of referenced code

        Testlist = Listbox(self)
        Testlist.pack()

        for test in tests:
            if test == 'users.csv' or test == 'lecturers.csv':
                tests.pop(tests.index(test))
            else:
                Testlist.insert(END, test[:-4])
        Testlist.grid()

        def ReadSelection():
            selection = Testlist.get(ACTIVE)
            selection += ".csv"
            newPage(self, StartTest, "Take Test", self.user_id, selection)
                
        butTakeTest = Button(self, text="Take Test", command=lambda:ReadSelection())
        butTakeTest.grid()

        if Testlist.size() == 0:
            butTakeTest.config(state=DISABLED)

        butBack = Button(self, text="Back", command=lambda:newPage(self, SummativeMenu, self.user_id, "Summative Menu"))
        butBack.grid()  


class StartTest(Frame):

    def __init__(self, master, selection):
        Frame.__init__(self)
        width = 550
        height = 600
    
        centred_window = centre_app(master, width, height)
        master.geometry(centred_window)

        self.testName = selection
        self.testQuestions = {"question_no":[], "question":[], "answer_choices":[], "is_correct_answer":[], "answer_feedback":[]}
        self.LoadQuestion()
        self.DisplayQuestion()

    def LoadQuestion(self):
        import csv
        #print(self.testName)
        with open(self.testName, 'r') as test:
            questions = csv.reader(test)
            for question in questions:
                if (question != []) and ("question_no" not in question):
                    self.testQuestions["question_no"].append(question[0])
                    self.testQuestions["question"].append(question[1])
                    self.testQuestions["answer_choices"].append(question[2])
                    self.testQuestions["is_correct_answer"].append(question[3])
                    self.testQuestions["answer_feedback"].append(question[4])
            #print(self.testQuestions)



    def DisplayQuestion(self):
        numOfQuestions = len(self.testQuestions["question_no"])

        for i in range(0, numOfQuestions-1):
            print(self.testQuestions["question_no"][i])
            #lblQuestion_no = 

    
    #def CheckAns(self):

#main
root = Tk()
app = ViewSummative(root)
root.mainloop()     