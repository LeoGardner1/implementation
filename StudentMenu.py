
from tkinter import *
from globalFunctions import *

class StudentMenu(Frame):

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

        butCreateTest = Button(self, text="Formative Test", command="")
        butCreateTest.grid()

        butSummative = Button(self, text="Summative Test", command="")
        butSummative.grid()

        butFormative = Button(self, text="My Results", command="")
        butFormative.grid()
'''
root = Tk()
app = LecturerMenu(root)
root.mainloop()
        
     
def centre_app(m, w, h):

    ws = m.winfo_screenwidth()
    hs = m.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)        
    return ("%dx%d+%d+%d" %(w, h , x, y))

'''    
