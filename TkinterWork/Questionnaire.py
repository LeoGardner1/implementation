
from tkinter import *
import tkinter.messagebox
#from tkinter import tkMessageBox
from Response import Response
from DisplayResults import *

class Questionnaire(Frame):
    #GUI Setup

    def __init__(self, master):
        #initialise Questionnaire class
        
        Frame.__init__(self, master)
        self.grid()
        self.createProgSelect()
        self.createTeamExpQuest()
        self.createProblems()
        self.createComments()
        self.createButtons()

    def createProgSelect(self):
        # create widget to select a degree programme from a list

        lblProg = Label(self, text="Degree Programme:", font=("MS", 8, "bold"))
        lblProg.grid(row=0, column=0, columnspan=2, sticky=NE)

        self.listProg = Listbox(self, height=3)
        scroll = Scrollbar(self, command=self.listProg.yview)
        self.listProg.configure(yscrollcommand=scroll.set)

        self.listProg.grid(row=0, column=2, columnspan=2, sticky=NE)
        scroll.grid(row = 0, column = 4, sticky = W)

        for item in ["CS", "CS with", "BIS", "SE", "Joints",""]:
            self.listProg.insert(END, item)

        self.listProg.selection_set(END)

    def createTeamExpQuest(self):
        # create widget s to ask Team Experience Questions

        lblStrAgr = Label(self, text = "Strongly\n Agree", font=("MS", 8, "bold"))
        lblStrAgr.grid(row=3, column=4, rowspan=2)

        lblPrtAgr = Label(self, text="Partly\n Agree", font=("MS", 8, "bold"))
        lblPrtAgr.grid(row=3, column=5, rowspan=2)

        lblPrtDis = Label(self, text="Partly\n DisAgree", font=("MS", 8, "bold"))
        lblPrtDis.grid(row=3, column=6, rowspan=2)

        lblStrDis = Label(self, text="Stronglyly\n DisAgree", font=("MS", 8, "bold"))
        lblStrDis.grid(row=3, column=7, rowspan=2)

        lblTeamExp = Label(self, text="Team Experience:", font=("MS", 8, "bold"))
        lblTeamExp.grid(row=4, column=0, columnspan = 2, sticky=W)

        lblQuest1 = Label(self, text="\t1. Our team worked together effectively")
        lblQuest1.grid(row=5, column=0, columnspan=3, sticky=W)

        lblQuest1 = Label(self, text="\t1. Our team produced good quality products")
        lblQuest1.grid(row=6, column=0, columnspan=3, sticky=W)

        lblQuest1 = Label(self, text="\t1. I enjoyed working in our team")
        lblQuest1.grid(row=7, column=0, columnspan=3, sticky=W)

        self.varQ1 = IntVar()

        R1Q1 = Radiobutton(self, variable=self.varQ1, value=4)
        R1Q1.grid(row=5, column=4)

        R2Q1 = Radiobutton(self, variable=self.varQ1, value=3)
        R2Q1.grid(row=5, column=5)

        R3Q1 = Radiobutton(self, variable=self.varQ1, value=2)
        R3Q1.grid(row=5, column=6)

        R4Q1 = Radiobutton(self, variable=self.varQ1, value=1)
        R4Q1.grid(row=5, column=7)

        self.varQ2 = IntVar()

        R1Q2 = Radiobutton(self, variable=self.varQ2, value=4)
        R1Q2.grid(row=6, column=4)

        R2Q2 = Radiobutton(self, variable=self.varQ2, value=3)
        R2Q2.grid(row=6, column=5)

        R3Q2 = Radiobutton(self, variable=self.varQ2, value=2)
        R3Q2.grid(row=6, column=6)

        R4Q2 = Radiobutton(self, variable=self.varQ2, value=1)
        R4Q2.grid(row=6, column=7)

        self.varQ3 = IntVar()

        R1Q3 = Radiobutton(self, variable=self.varQ3, value=4)
        R1Q3.grid(row=7, column=4)

        R2Q3 = Radiobutton(self, variable=self.varQ3, value=3)
        R2Q3.grid(row=7, column=5)

        R3Q3 = Radiobutton(self, variable=self.varQ3, value=2)
        R3Q3.grid(row=7, column=6)

        R4Q3 = Radiobutton(self, variable=self.varQ3, value=1)
        R4Q3.grid(row=7, column=7)

    def createProblems(self):
        #create widgets to show Problems experienced

        lblProb1 = Label(self, text="Problems:", font=("MS", 8, "bold"))
        lblProb1.grid(row=8, column=0)

        lblProb2 = Label(self, text="Our team often experienced the " + "following problems (choose all that apply):")
        lblProb2.grid(row=8, column=1, columnspan=6, sticky=W)

        self.varCB1 = IntVar()

        CB1 = Checkbutton(self, text=" Poor Communication", variable=self.varCB1)
        CB1.grid(row=9, column=0, columnspan=4, sticky=W)

        self.varCB2 = IntVar()

        CB2 = Checkbutton(self, text=" Lack of Direction", variable=self.varCB2)
        CB2.grid(row=10, column=0, columnspan=4, sticky=W)

        self.varCB3 = IntVar()

        CB3 = Checkbutton(self, text=" Disagreements Amongst Team", variable=self.varCB3)
        CB3.grid(row=11, column=0, columnspan=4, sticky=W)

        self.varCB4 = IntVar()

        CB4 = Checkbutton(self, text=" Member Missing Meetings", variable=self.varCB4)
        CB4.grid(row=9, column=4, columnspan=4, sticky=W)

        self.varCB5 = IntVar()

        CB5 = Checkbutton(self, text=" Member not Contributing", variable=self.varCB5)
        CB5.grid(row=10, column=4, columnspan=4, sticky=W)

        self.varCB6 = IntVar()

        CB6 = Checkbutton(self, text=" Members not Motivated", variable=self.varCB6)
        CB6.grid(row=11, column=4, columnspan=4, sticky=W)
        

        
    def createComments(self):

        lblComment = Label(self, text="Comments about\n Teamswork:", font=("MS", 8, "bold"))
        lblComment.grid(row=12, column=0, columnspan=2, rowspan=2)

        self.txtComment = Text(self, height=3, width=40)

        scroll = Scrollbar(self, command=self.txtComment.yview)
        self.txtComment.configure(yscrollcommand=scroll.set)

        self.txtComment.grid(row=12, column=2, columnspan=5, sticky=E)
        scroll.grid(row=12, column=7, sticky=W)

        lblName = Label(self, text="Name(optional):")
        lblName.grid(row=15, column=0, sticky=E, columnspan=3)

        self.entName= Entry(self)
        self.entName.grid(row=15, column=3, columnspan=4, sticky=W)

    def createButtons(self):
        
        butSubmit = Button(self, text="Submit", font=("MS", 8, "bold"))
        butSubmit["command"]=self.storeResponse
        butSubmit.grid(row=16, column=1)

        butClear = Button(self, text="Clear", font=("MS", 8, "bold"))
        butClear["command"]=self.clearResponse
        butClear.grid(row=16, column=2)

        butClear = Button(self, text="Show Results", font=("MS", 8, "bold"))
        butClear["command"]=self.openResultsWindow
        butClear.grid(row=16, column=3)

    def openResultsWindow(self):

        t1 = Toplevel(root)
        t1.title("Results")
        DisplayResults(t1)
        

    def clearResponse(self):
        #clears the Questionnaire

        self.listProg.selection_clear(0, END)
        self.listProg.selection_clear(END)

        self.varQ1.set(0)
        self.varQ2.set(0)
        self.varQ3.set(0)

        self.varCB1.set(0)
        self.varCB2.set(0)
        self.varCB3.set(0)
        self.varCB4.set(0)
        self.varCB5.set(0)
        self.varCB6.set(0)

        self.entName.delete(0, END)
        self.txtComment.delete(1.0, END)

    def storeResponse(self):

        index = self.listProg.curselection()[0]
        strProg = str(self.listProg.get(index))
        strMsg=""

        if strProg == "":
            strMsg = "You need to select a Degree Programme. "

        if self.varQ1.get() == 0 or self.varQ2.get() == 0 or self.varQ3.get() == 0:
            strMsg = strMsg + "You need to answer all Team Experience Questions"

        if strMsg == "":
            import shelve
            db = shelve.open("responsedb")

            responseCount = len(db)
            Ans = Response(str(responseCount + 1), strProg, self.varQ1.get(), self.varQ2.get(),
                           self.varQ3.get(), self.varCB1.get(), self.varCB2.get(),
                           self.varCB3.get(), self.varCB4.get(), self.varCB5.get(),
                           self.varCB6.get(), self.txtComment.get(1.0,END), self.entName.get())
            db[Ans.respNo] = Ans
            db.close

            tkinter.messagebox.showinfo("Questionnaire", "Questionnaire Submitted")
            self.clearResponse()

        else:
            tkinter.messagebox.showwarning("Entry Error", strMsg)

#def main():
root = Tk()
#root.geometry("400x300")
root.title("Teamwork Questionnaire")
app = Questionnaire(root)
root.mainloop()

#if __name__ == "__main__":
#    main()
