
from tkinter import *
from globalFunctions import *


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

        self.mainMenu()

    def mainMenu(self):

        butCreateTest = Button(self, text="Create Test", command=lambda:newPage(self, QuestionsSet, "Create Test"))
        butCreateTest.grid()

        butSummative = Button(self, text="Summative Test", command="")
        butSummative.grid()

        butFormative = Button(self, text="Formative Test", command="")
        butFormative.grid()

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

        goBack_button = Button(text="Back to Homepage", command=lambda:newPage(self, LecturerMenu, "Lecturer Page"))
        goBack_button.grid(row=1, column=1, sticky=NSEW)

        cont_button = Button(text="Continue Creating Test", command=lambda:newPage(self, CreateTest, "Create Test", questionNumber.get()))
        cont_button.grid(row=1, column=6, sticky=NSEW)
        
class CreateTest(QuestionsSet):

    def __init__(self, master, *args):

        Frame.__init__(self, master)
        #self.grid()

        width = 550
        height = 600
    
        centred_window = centre_app(master, width, height)
        master.geometry(centred_window)

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

        

        self.questionNo= int(args[0])
        self.createTest()

        
    def createTest(self):

        rowAdjuster = 0

        testNamelbl = Label(self.frame, text="\nEnter Test Name:\n", font=("Arial", 14, "bold"))
        testNamelbl.grid(row=0, column=0, rowspan=3, sticky=NE)
        
        testNameField=Entry(self.frame)
        testNameField.grid(row=1, column=1, sticky=W, ipadx="100", columnspan=4)

        testNameBtn = Button(self.frame, text="Save", command=self.saveTest)
        testNameBtn.grid(row=1, column=2)

        for i in range(self.questionNo):
        

            questionLbl = Label(self.frame, text="Question " + str(i+1) + ":", font=("Arial", 12, "bold"))
            questionLbl.grid(row= rowAdjuster + 3, column=0, sticky=E)

            questionField = Entry(self.frame)
            questionField.grid(row=rowAdjuster + 3, column=1, ipadx="100")

            answersLbl = Label(self.frame, text="Answer Choices: (Tick the correct answers)", font=("Tahome", 10, "bold"))
            answersLbl.grid(row=rowAdjuster + 4, column=0, columnspan=6, sticky=W)


            self.correctAns = StringVar()
            
            
            #ansA = Checkbutton(self, text="A.", variable=self.correctAns, onvalue=1, offvalue=1)
            ansA = Checkbutton(self.frame, text="A.", font=("Arial", 10, "bold"))
            ansA.grid(row=rowAdjuster + 5, column=0, sticky=E)

            ansFieldA = Entry(self.frame)
            ansFieldA.grid(row=rowAdjuster + 5, column=1, ipadx="100", sticky=W, columnspan=3)

            ansAcommentlbl = Label(self.frame, text="Answer Comments:")
            ansAcommentlbl.grid(row=rowAdjuster + 6, column=0, rowspan=2, sticky=NE)

            self.ansAcomment = Text(self.frame, height=2, width =40)
            self.ansAcomment.grid(row=rowAdjuster + 6, column=1, sticky=W, columnspan=3)


            ansB = Checkbutton(self.frame, text="B.", font=("Arial", 10, "bold"))
            ansB.grid(row=rowAdjuster + 7, column=0, sticky=E)

            ansFieldB = Entry(self.frame)
            ansFieldB.grid(row=rowAdjuster + 7, column=1, ipadx="100", sticky=W)
            

            #print(self.correctAns.get())
            #print(ansA.cget("text"))
            ansBcommentlbl = Label(self.frame, text="Answer Comments:")
            ansBcommentlbl.grid(row=rowAdjuster + 8, column=0, rowspan=2, sticky=NE)

            self.ansBcomment = Text(self.frame, height=2, width =40)
            self.ansBcomment.grid(row=rowAdjuster + 8, column=1, sticky=W, columnspan=3)

            ansC = Checkbutton(self.frame, text="C.", font=("Arial", 10, "bold"))
            ansC.grid(row=rowAdjuster + 9, column=0, sticky=E)

            ansFieldC = Entry(self.frame)
            ansFieldC.grid(row=rowAdjuster + 9, column=1, ipadx="100", sticky=W, columnspan=3)

            ansCcommentlbl = Label(self.frame, text="Answer Comments:")
            ansCcommentlbl.grid(row=rowAdjuster + 10, column=0, rowspan=2, sticky=NE)

            self.ansCcomment = Text(self.frame, height=2, width =40)
            self.ansCcomment.grid(row=rowAdjuster + 10, column=1, sticky=W, columnspan=3)

            ansD = Checkbutton(self.frame, text="D.", font=("Arial", 10, "bold"))
            ansD.grid(row=rowAdjuster + 11, column=0, sticky=E)

            ansFieldD = Entry(self.frame)
            ansFieldD.grid(row=rowAdjuster + 11, column=1, ipadx="100", sticky=W, columnspan=3)

            ansDcommentlbl = Label(self.frame, text="Answer Comments:")
            ansDcommentlbl.grid(row=rowAdjuster + 12, column=0, rowspan=2, sticky=NE)

            self.ansDcomment = Text(self.frame, height=2, width =40)
            self.ansDcomment.grid(row=rowAdjuster + 12, column=1, sticky=W, columnspan=3)

            new_line = Label(self.frame, text="-" * 100)
            new_line.grid(row=rowAdjuster +13, column=0, columnspan=4, sticky=NSEW)

            rowAdjuster += 13

    def frameConfigure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))    

    def saveTest(self):
        with open(self.testNameField.get(), 'w') as file:
            file.write(self.testNameField.get('1.0', END))


'''
root = Tk()
app = LecturerMenu(root)
root.mainloop()
'''

