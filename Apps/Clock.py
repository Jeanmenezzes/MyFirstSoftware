# CONTINUE CHANGING THE LANGUAGE TO ENGLISH AND TO PUT IN CANVAS THE EXECUTION TIME

# Importing functions what are needed for the execution
from tkinter import *
import time


# Class what contains the commands to create the clock and count the time of the execution
class ClockApp(object):
    # This is the variable to resize Program's Screen
    xy = '800x550'

    # The initialize function used to create the canvas, buttons and count the back-end time execution
    def __init__(self, branch):
        # The font what will be used along the app
        self.font = ('Calibre', 60, 'bold')

        # Setting the labels and canvas after create them
        self.clock_screen = Canvas(branch, bg='blue', width=360, height=180)
        self.clock_screen.pack(pady=20)

        self.button_Time = Button(branch, text='Show the Time', fg='white', bg='gray', command=self.show_the_time)
        self.button_Time.pack()

        self.execution_time_screen = Canvas(branch, bg='blue', width=360, height=180)
        self.execution_time_screen.pack(pady=20)

        self.exec_time_button = Button(branch, text='Show the Execution Time', fg='white', bg='gray',
                                       command=self.show_et)
        self.exec_time_button.pack()

    # Function responsible to show the time numbers
    def show_the_time(self):
        # Variable counted_time contains a local struct time what the numbers used were distributed in.
        counted_time = time.localtime()
        hour = counted_time.tm_hour
        minute = counted_time.tm_min
        second = counted_time.tm_sec

        # Deletes the tags of a possible previous time showed
        self.clock_screen.delete('hour', 'minute', 'second')

        # Creates ID's to every number of the time
        self.text_hour = self.clock_screen.create_text((80, 90), text='%.2i:' % hour, font=self.font, tag='hour')
        self.text_minute = self.clock_screen.create_text((190, 90), text='%.2i:' % minute, font=self.font, tag='minute')
        self.text_second = self.clock_screen.create_text((290, 90), text='%.2i' % second, font=self.font, tag='second')

        # Calls again the same function by each second to show the time running
        self.clock_screen.after(1000, self.show_the_time)

    # Function responsible to show the time of software execution
    def show_et(self):
        self.execution_time_screen.delete('time_ex')
        self.exec_time = self.execution_time_screen.create_text((185, 90), text='%.5f' % time.process_time(),
                                                                font=self.font, tag='time_ex')

