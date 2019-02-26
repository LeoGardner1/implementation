from tkinter import *
from TestTrial import QuestionInfo, AttemptTest


class TempSelectMenu(Frame): # This will eventually be a login page e.g. depending on the login used you will be taken to either student or lecturer main menu 
	
	def __init__ (self, master):
		Frame.__init__ (self, master)
		self.grid()	
		self.createButtons()

	def createButtons(self):
		butOpenLecturerMenu = Button(self, text='Lecturer Main Menu',font=('MS', 8,'bold'))
		butOpenLecturerMenu['command']= self.openLecturerMainMenu #method is in Test.py in class test
		butOpenLecturerMenu.grid(row=16, column=2, columnspan=1) 

		butOpenStudentMenu = Button(self, text='Student Main Menu',font=('MS', 8,'bold'))
		butOpenStudentMenu['command']= self.openStudentMainMenu #method is in Test.py in class test
		butOpenStudentMenu.grid(row=18, column=2, columnspan=1) 

	def openLecturerMainMenu(self):
		t1 = Toplevel(root)
		t1.title("Lecturer Main Menu")
		LecturerMainMenu(t1)

	def openStudentMainMenu(self):
		t1 = Toplevel(root)
		t1.title("Student Main Menu")
		StudentMainMenu(t1)


class LecturerMainMenu(Frame):

	def __init__ (self, master):
		Frame.__init__ (self, master)
		self.grid()
		self.createButtons()

	def createButtons(self):
		butCreateTest = Button(self, text='Create Test',font=('MS', 8,'bold'))
		butCreateTest['command']= self.openCreateTestWindow #method is in Test.py in class test
		butCreateTest.grid(row=16, column=2, columnspan=1) 


	def openCreateTestWindow(self):
		t1 = Toplevel(root)
		t1.title("Create Test")
		QuestionInfo(t1)




class StudentMainMenu(Frame):

	def __init__ (self, master):
		Frame.__init__ (self, master)
		self.grid()
		self.createButtons()

	def createButtons(self):
		butAttemptTest = Button(self, text='Attempt Test',font=('MS', 8,'bold'))
		butAttemptTest['command']= self.openAttemptTestWindow
		butAttemptTest.grid(row=16, column=2, columnspan=1)

	def openAttemptTestWindow(self):
		t1 = Toplevel(root)
		t1.title("Attempt Test")
		AttemptTest(t1)


# root = Tk()
# root.title("Main Menu")
# app = LecturerMainMenu(root)
# root.mainloop() 

root = Tk()
root.title("Temporary Select Menu")
app = TempSelectMenu(root)
root.mainloop() 