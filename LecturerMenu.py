
from tkinter import *

from StudentMenu import centre_app

class LecturerMenu(Frame):

    def __init__(self, master):

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

        butCreateTest = Button(self, text="Create Test", command="")
        butCreateTest.grid()

        butSummative = Button(self, text="Summative Test", command="")
        butSummative.grid()

        butFormative = Button(self, text="Formative Test", command="")
        butFormative.grid()
'''
root = Tk()
app = LecturerMenu(root)
root.mainloop()
        
'''        
