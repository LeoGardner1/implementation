from tkinter import *

from LecturerMenu import LecturerMenu
from StudentMenu import StudentMenu, centre_app

class LoginPage(Frame):

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

        self.user_login()


    def user_login(self): 

        username_label = Label(text="Username: ")
        username_label.grid(row=1, column=1)

        self.username = StringVar()
        self.password = StringVar()
        
        usernameEnt = Entry(textvariable = self.username)
        usernameEnt.grid(row=1, column=2)

        pw_label = Label(text="Password: ")
        pw_label.grid(row=2, column=1)
        
        passwordEnt = Entry(textvariable = self.password, show="\u2022")
        passwordEnt.bind('<Return>', self.user_auth)
        passwordEnt.grid(row=2, column=2)

        self.login_button = Button(text="Login", command=self.user_auth)
        self.login_button.grid(row=3, column=2)


    def user_auth(self, event=None):
        import csv

        username = self.username.get()

        password = self.password.get()

        user_list = {}

        with open('users.csv') as users:
            reader = csv.reader(users)

            next(reader, None)

            for row in reader:
                user_list[row[0]] = {"pw":row[1], "user_type": row[4]}


        if username in user_list:
            if user_list[username]["pw"] ==  password:
                self.master.destroy()
                if user_list[username]["user_type"] == "Lecturer":
                    lecturer = Tk()
                    lecturer.title("Lecturer Page")
                    LecturerMenu(lecturer)
                    
                elif user_list[username]["user_type"] == "Student":
                    student = Tk()
                    student.title("Student Page")
                    StudentMenu(student)

                else:
                    #change this into a prompt box
                    print("You don't have authorised access to this program")
            else:
                #needs to be changed into a prompt box
                print("Incorrect Password")
        else:
            #needs to be changed into a prompt box
            print("Incorrect Username / Password")

root = Tk()
app = LoginPage(root)
root.mainloop()        

#print(user_list)
