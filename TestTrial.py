from tkinter import *



class QuestionInfo(Frame):

    def __init__(self, master):

        Frame.__init__(self, master)
        self.grid()

        self.master = master

        master.title("Test Set-up")
        """
        testName = Label(self, text="\nEnter Test Name:\n", font=("Arial", 12, "bold"))
        testName.grid(row=0, column=0, rowspan=3, sticky=NE)

        testNameField=Entry()
        testNameField.grid(row=1, column=1, sticky=W, ipadx="50", columnspan=4)

        testNameBtn = Button(self.master, text="Save", command=save)
        testNameBtn.grid(row=1, column=6) 
        """

        self.testName()
        self.questionForm()

    def questionForm(self):

        #increment when adding another set
        questionNo=1

        questionLbl = Label(self, text="Question " + str(questionNo) + ":", font=("Arial", 10, "bold"))
        questionLbl.grid(row=3, column=0, sticky=E)

        questionField = Entry(self)
        questionField.grid(row=3, column=1, ipadx="100")

        answersLbl = Label(self, text="Answer Choices: (Tick the correct answer)", font=("Tahome", 10, "bold"))
        answersLbl.grid(row=4, column=0, columnspan=6, sticky=W)


        self.correctAns = StringVar()
        
        
        #ansA = Checkbutton(self, text="A.", variable=self.correctAns, onvalue=1, offvalue=1)
        ansA = Checkbutton(self, text="A.", font=("Arial", 10, "bold"))
        ansA.grid(row=5, column=0, sticky=E)

        ansFieldA = Entry(self)
        ansFieldA.grid(row=5, column=1, ipadx="100", sticky=W, columnspan=3)

        ansAcommentlbl = Label(self, text="Answer Comments:")
        ansAcommentlbl.grid(row=6, column=0, rowspan=2, sticky=NE)

        self.ansAcomment = Text(self, height=2, width =40)
        self.ansAcomment.grid(row=6, column=1, sticky=W, columnspan=3)


        ansB = Checkbutton(self, text="B.", font=("Arial", 10, "bold"))
        ansB.grid(row=7, column=0, sticky=E)

        ansFieldB = Entry(self)
        ansFieldB.grid(row=7, column=1, ipadx="100", sticky=W)
        

        #print(self.correctAns.get())
        #print(ansA.cget("text"))
        ansBcommentlbl = Label(self, text="Answer Comments:")
        ansBcommentlbl.grid(row=8, column=0, rowspan=2, sticky=NE)

        self.ansBcomment = Text(self, height=2, width =40)
        self.ansBcomment.grid(row=8, column=1, sticky=W, columnspan=3)

        ansC = Checkbutton(self, text="C.", font=("Arial", 10, "bold"))
        ansC.grid(row=9, column=0, sticky=E)

        ansFieldC = Entry(self)
        ansFieldC.grid(row=9, column=1, ipadx="100", sticky=W, columnspan=3)

        ansCcommentlbl = Label(self, text="Answer Comments:")
        ansCcommentlbl.grid(row=10, column=0, rowspan=2, sticky=NE)

        self.ansCcomment = Text(self, height=2, width =40)
        self.ansCcomment.grid(row=10, column=1, sticky=W, columnspan=3)

        ansD = Checkbutton(self, text="D.", font=("Arial", 10, "bold"))
        ansD.grid(row=11, column=0, sticky=E)

        ansFieldD = Entry(self)
        ansFieldD.grid(row=11, column=1, ipadx="100", sticky=W, columnspan=3)

        ansDcommentlbl = Label(self, text="Answer Comments:")
        ansDcommentlbl.grid(row=12, column=0, rowspan=2, sticky=NE)

        self.ansDcomment = Text(self, height=2, width =40)
        self.ansDcomment.grid(row=12, column=1, sticky=W, columnspan=3)

        addQuestionBtn = Button(self, text="Add Question")
        addQuestionBtn.grid(row=13, column=2)
        

    def addForm():
        pass

    def testName(self):

        testNamelbl = Label(self, text="\nEnter Test Name:\n", font=("Arial", 12, "bold"))
        testNamelbl.grid(row=0, column=0, rowspan=3, sticky=NE)
        
        testNameField=Entry(self)
        testNameField.grid(row=1, column=1, sticky=W, ipadx="100", columnspan=4)

        testNameBtn = Button(self, text="Save", command=self.save)
        testNameBtn.grid(row=1, column=2) 

    def save(self):
        with open(self.testNameField.get(), 'w') as file:
            file.write(self.testNameField.get('1.0', END))

    def save():
        pass

    

class AttemptTest(Frame):

    def __init__(self, master):

        Frame.__init__(self, master)
        self.grid()

        self.master = master

        master.title("Attempt Test")
        self.questionForm()
        self.testName
    
    def questionForm(self):

        #increment when adding another set
        questionNo=1

        questionLbl = Label(self, text="Question " + str(questionNo) + ":", font=("Arial", 10, "bold"))
        questionLbl.grid(row=3, column=0, sticky=E)

        questionTitleLbl = Label(self, text="'Question from DB goes here'", font=("Arial", 10, "bold", "italic"))
        questionTitleLbl.grid(row=3, column=1, sticky=E)


        # questionField = Entry(self)
        # questionField.grid(row=3, column=1, ipadx="100")

        answersLbl = Label(self, text="Answer Choices: (Tick the correct answer)", font=("Tahome", 10, "bold"))
        answersLbl.grid(row=4, column=0, columnspan=6, sticky=W)


        self.correctAns = StringVar()
        
        
        #ansA = Checkbutton(self, text="A.", variable=self.correctAns, onvalue=1, offvalue=1)
        ansA = Checkbutton(self, text="A.", font=("Arial", 10, "bold"))
        ansA.grid(row=5, column=0, sticky=E)

        questionALbl = Label(self, text="'Answer from DB goes here'", font=("Arial", 10, "bold", "italic"))
        questionALbl.grid(row=5, column=1, sticky=E)


        ansB = Checkbutton(self, text="B.", font=("Arial", 10, "bold"))
        ansB.grid(row=7, column=0, sticky=E)

        questionBLbl = Label(self, text="'Answer from DB goes here'", font=("Arial", 10, "bold", "italic"))
        questionBLbl.grid(row=7, column=1, sticky=E)
        

        ansC = Checkbutton(self, text="C.", font=("Arial", 10, "bold"))
        ansC.grid(row=9, column=0, sticky=E)

        questionCLbl = Label(self, text="'Answer from DB goes here'", font=("Arial", 10, "bold", "italic"))
        questionCLbl.grid(row=9, column=1, sticky=E)

        ansD = Checkbutton(self, text="D.", font=("Arial", 10, "bold"))
        ansD.grid(row=11, column=0, sticky=E)

        questionDLbl = Label(self, text="'Answer from DB goes here'", font=("Arial", 10, "bold", "italic"))
        questionDLbl.grid(row=11, column=1, sticky=E)


        addQuestionBtn = Button(self, text="Submit Answer")
        addQuestionBtn.grid(row=13, column=2)



    def addForm():
        pass

    def testName(self):

        testNamelbl = Label(self, text="\nEnter Test Name:\n", font=("Arial", 12, "bold"))
        testNamelbl.grid(row=0, column=0, rowspan=3, sticky=NE)
        
        testNameField=Entry(self)
        testNameField.grid(row=1, column=1, sticky=W, ipadx="100", columnspan=4)

        testNameBtn = Button(self, text="Save", command=self.save)
        testNameBtn.grid(row=1, column=2) 








    

def create(self, csvfile):
    pass


#def main():
#
#    root = Tk()
#    createQuestion = QuestionInfo(root)
#    root.mainloop()
#
#if __name__ == "__main__":
#    main()

root = Tk()
root.title("Attempt Test")
app = AttemptTest(root)
root.mainloop() 