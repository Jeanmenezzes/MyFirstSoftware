# THIS PROGRAM WILL BE UPLOADED WITH JUST THE FOUR APPS ALREADY SET

# THIS PROGRAM WILL BE UPLOADED WITHOUT BUT IT NEEDS TO HAVE USER'S NAME AND A WELLCOME MESSAGE
# THIS PROGRAM WILL BE UPLOADED WITHOUT BUT IT NEEDS TO HAVE A USER PROFILE SCREEN
# THIS PROGRAM WILL BE UPLOADED WITHOUT BUT IT NEEDS TO HAVE A BACK SCREEN BUTTON AT CREATE USER SCREEN AND APPS SCREEN

# IT'S NEEDED TO FINISH THE CLOCK APP. FIX ALARM AND MARIO APPS. VERIFY IF THERE IS ERRORS IN THE PALETTE APP
# IT'S NEEDED TO CHANGE TO ENGLISH AND FIX ALL CODE CONVECTION ERRORS IN THE PROGRAM AND APPS

# CREATE A VIDEO WITH THE EXECUTION OF THE PROGRAM AND UPLOAD THI IN TO YOUTUBE
# LEARN HOW TO UPLOAD IN TO GITHUB TO SOMEONE A PROGRAM WITH THE PILLOW LIBRARY
# LEARN HOW TO CREATE A EXECUTABLE PROGRAM IN PYTHON

# Importing All Modules
import os
import sys
from tkinter import *


# Adding to path files with other functions
sys.path.append('Apps')
sys.path.append('Images')


# The main object Program
class Program(object):
    def __init__(self, root):
        # Parameters to the window
        self.axis_x = 500
        self.axis_y = 500
        self.main_Color = '#c3c3c3'

        # Construction of main screen
        self.root = root
        self.root.geometry('%ix%i' % (self.axis_x, self.axis_y))
        self.root.resizable(0, 0)
        self.root.title('Python - My First Software')
        self.root.wm_iconbitmap('Images/icon.ico')
        self.root['bg'] = self.main_Color
        self.main_Frame = Frame(root, bg=self.main_Color)
        self.main_Frame.pack()

        # Calling the function what constructs the heading
        self.main_screen()

    # Function that contains the fixed logo, frame with login, apps options and a checker variable
    def main_screen(self):
        self.f_logo = PhotoImage(file='Images/main_logo.png')
        self.title = Label(self.main_Frame, image=self.f_logo, bg=self.main_Color)
        self.title.grid(column=0, row=0)

        self.frame_foptions = Frame(self.main_Frame, bg=self.main_Color)
        self.frame_foptions.grid(column=0, row=1)

        self.variable = BooleanVar(value=False, name='Any')
        self.variable.trace('w', self.checker_variable)

        # Importing and execute the login function
        from Func_Login import Login
        self.branch = Login(self.frame_foptions, self.main_Color, self.variable)

    def account_screen(self):
        pass

    def app_executing(self, *args):
        self.root.resizable(1, 1)

        if self.var.name == 'Clock':
            import time
            from Clock import ClockApp as App
        elif self.var.name == 'Alarm':
            from Alarm import Alarm as App
            import time, winsound
            sys.path.append('Music')
        elif self.var.name == 'Mario':
            from Mario import Mario_App as App
        elif self.var.name == 'Palette':
            from Palette import Palette_App as App

        self.main_Frame.destroy()
        self.main_Frame = Frame(self.root, bg=self.main_Color)
        self.main_Frame.pack()
        self.root.geometry(App.xy)
        App(self.main_Frame)


    def directing(self):
        pass

    def checker_variable(self, *args):
        # CONTINUE FROM HERE
        # For Apps Screen
        if self.variable.name == 'Apps':
            self.variable.name = 'Apps Menu'
            from creating_button_function import new_button
            self.frame_options = Frame(self.main_Frame, bg=self.main_Color)
            self.frame_options.grid(column=0, row=1)

            self.var = BooleanVar(value=False, name='Any')
            self.var.name = 'Any'
            self.var.trace('w', self.app_executing)

            self.buttons_dict = {}
            cont = 0
            for app in os.listdir('Apps'):
                if app == 'To Organize' or app == '__pycache__':
                    continue
                cont += 1
                self.buttons_dict[app] = new_button('Images/%s_ico.png'%app[:-3], self.frame_options, self.main_Color,
                                                    self.var)
                self.buttons_dict[app].grid(row=(cont-1)//2, column=cont % 2, pady=2)

        # For the create user menu's screen
        elif self.variable.name == 'Create':
            from Func_Login import Create
            self.frame_foptions = Frame(self.main_Frame, bg=self.main_Color)
            self.frame_foptions.grid(column=0, row=1)
            Create(self.frame_foptions, self.main_Color, self.variable)

        # For the login screen
        elif self.variable.name == 'Login':
            from Func_Login import Login
            self.frame_foptions = Frame(self.main_Frame, bg=self.main_Color)
            self.frame_foptions.grid(column=0, row=1)
            Login(self.frame_foptions, self.main_Color, self.variable)


if __name__ == '__main__':
    constructor = Tk()
    inst = Program(constructor)
    constructor.mainloop()
