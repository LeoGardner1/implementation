from tkinter import *
from globalFunctions import *
import csv
import ast
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

        #self.user_id = args[0]
        self.user_id = "100001"
        self.createButtons()

    def createButtons(self):

        btnViewTest = Button(self, text = "View Summative Tests", command=lambda:newPage(self, ViewSummative, "Summative Test List", self.user_id))
        btnViewTest.grid(row=0, column=0)

        btnViewResults = Button(self, text = "View Summative Results")
        btnViewResults.grid(row=1, column=0)

        btnBack = Button(self, text = "Back", command=lambda:newPage(self, StudentMenu, "Student Menu", self.user_id))
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
        self.user_id="100001"
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
            if test == 'users.csv' or test == 'lecturers.csv' or test == 'studentResults.csv':
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

        butBack = Button(self, text="Back", command=lambda:newPage(self, SummativeMenu, "Summative Menu", self.user_id))
        butBack.grid()  


class StartTest(Frame):

    def __init__(self, master, *args):
        Frame.__init__(self, master)
        width = 550
        height = 600
    
        centred_window = centre_app(master, width, height)
        master.geometry(centred_window)

        scrollBar(master, self)

        self.user_id = args[0]
        self.testName = args[1]
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
        for i in range(0, numOfQuestions):
            question =  str(i + 1) + ": " + str(self.testQuestions["question"][i])
            choices = ast.literal_eval(self.testQuestions["answer_choices"][i])
            choiceA = 'A: ' + choices["A"]
            choiceB = "B: " + choices["B"]
            choiceC = "C: " + choices["C"]
            choiceD = "D: " + choices["D"]

            lblQuestion = Label(self.frame, text=question)
            lblQuestion.grid()

            radChoiceA = Radiobutton(value=str(i) + "A" ,variable="question" + str(i), text=choiceA, indicatoron=0)
            radChoiceA.pack()

            radChoiceB = Radiobutton(value=str(i) + "B" ,variable="question" + str(i), text=choiceB, indicatoron=0)
            radChoiceB.pack()

            radChoiceC = Radiobutton(value=str(i) + "C" ,variable="question" + str(i), text=choiceC, indicatoron=0)
            radChoiceC.pack()

            radChoiceD = Radiobutton(value=str(i) + "D" ,variable="question" + str(i), text=choiceD, indicatoron=0)
            radChoiceD.pack()



    def frameConfigure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
    
    #def CheckAns(self):

#main
root = Tk()
app = ViewSummative(root)
root.mainloop()     