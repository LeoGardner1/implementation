from tkinter import *
from globalFunctions import *

class ViewSummative(Frame):

    def __init__(self, master):

        Frame.__init__(self, master)
        self.grid()
        master.title("CM1102 Automated Assessment")

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

    def CreateList(self):
    	


#main

root = Tk()
app = ViewSummative(root)
root.mainloop()     