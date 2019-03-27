from tkinter import *
from StudentMenu import StudentMenu
from ViewSummative import ViewSummative
from globalFunctions import *

class SummativeMenu(Frame):

	def __init__(self, master):

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

		self.createButtons()

	def createButtons(self):

		btnViewTest = Button(self, text = "View Summative Tests", command=lambda:newPage(self, ViewSummative, "Summative Test List"))
		btnViewTest.grid(row=0, column=0)

		btnViewResults = Button(self, text = "View Summative Results")
		btnViewResults.grid(row=1, column=0)

		btnBack = Button(self, text = "Back", command=lambda:newPage(self, StudentMenu, "Student Menu"))
		btnBack.grid(row=2, column=0)
# Main
root = Tk()
app = SummativeMenu(root)
root.mainloop()        