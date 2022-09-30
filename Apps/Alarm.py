from tkinter import *
import winsound, time


class Alarm(object):
    xy = '600x400'

    def __init__(self, root):
        self.root = root
        self.standard_font = ('Arial', '18', 'bold')

        # Creating the widgets
        self.hour_screen = Label(self.root, text='Hour')
        self.minute_screen = Label(self.root, text='Minute')
        self.second_screen = Label(self.root, text='Second')

        self.entry_hour = Entry(self.root)
        self.entry_minute = Entry(self.root)
        self.entry_second = Entry(self.root)

        self.alarm_screen = Canvas(self.root, width=550, height=300, bg='gray')

        self.button_set = Button(self.root, text='Set Alarm', command=self.set_alarm)

        # Set all widgets in the master root.
        self.hour_screen.grid(column=0, row=0, pady=5)
        self.minute_screen.grid(column=2, row=0)
        self.second_screen.grid(column=4, row=0)

        self.entry_hour.grid(column=1, row=0)
        self.entry_minute.grid(column=3, row=0)
        self.entry_second.grid(column=5, row=0)

        self.button_set.grid(row=1, column=2, columnspan=2, pady=4)
        self.alarm_screen.grid(column=0, columnspan=6, row=2)

        # Create all graphics
        for i in range(1,3):
            self.alarm_screen.create_polygon((55, 80*i), (40, 50+80*i), (170, 50+80*i), (155, 80*i))
            self.alarm_screen.create_polygon((210, 80*i), (225, 50+80*i), (325, 50+80*i), (340, 80*i))
            self.alarm_screen.create_polygon((395, 80*i), (380, 50+80*i), (510, 50+80*i), (495, 80*i))

        for i in range(1,22):
            self.alarm_screen.create_line((25*i,1),(25*i,300))

    def set_alarm(self):
        # Try to delete the marked alarm timers
        try:
            self.alarm_screen.delete(self.marked_hour)
            self.alarm_screen.delete(self.marked_minute)
            self.alarm_screen.delete(self.marked_second)

            self.alarm_screen.delete(self.second_timer)
            self.alarm_screen.delete(self.minute_timer)
            self.alarm_screen.delete(self.hour_timer)
        except AttributeError:
            pass

        # Receives all entries and if it isn't appropriate.set to number 0.
        if self.entry_hour.get().isnumeric():
            self.hour = int(self.entry_hour.get())
        else:
            self.hour = 0
        if self.entry_minute.get().isnumeric():
            self.minute = int(self.entry_minute.get())
        else:
            self.minute = 0
        if self.entry_second.get().isnumeric():
            self.second = int(self.entry_second.get())
        else:
            self.second = 0

        # Convert the entries and the current date to an instance object struct time
        the_time = time.localtime()
        self.time_alarm = time.strptime(
            '%.4i %.2i %.2i %.2i %.2i %.2i'
            %(int(the_time.tm_year), int(the_time.tm_mon), int(the_time.tm_mday), self.hour, self.minute,
              self.second),'%Y %m %d %H %M %S')
        # Defines the difference between the marked time and the current time.
        self.delta_time = time.mktime(self.time_alarm) - time.mktime(time.localtime())

        # Created the numbers of the alarm and how much time need to arouse
        self.marked_hour = self.alarm_screen.create_text(
            105,105, text = '%.2i'%int(self.time_alarm.tm_hour), fill='white', font= self.standard_font)
        self.marked_minute = self.alarm_screen.create_text(
            275,105, text = '%.2i'%int(self.time_alarm.tm_min), fill='white', font= self.standard_font)
        self.marked_second = self.alarm_screen.create_text(
            445, 105, text='%.2i' % int(self.time_alarm.tm_sec), fill='white', font=self.standard_font)

        # Redefines the timers after it's texts were used
        self.hour_timer = 0
        self.minute_timer = 0
        self.second_timer = 0

        if self.delta_time >= 0:
            self.timer()

    # Function timer what roam the timer at each second
    def timer(self):
        # Deletes and redefines seconds
        self.delta_time = time.mktime(self.time_alarm) - time.mktime(time.localtime())

        self.alarm_screen.delete(self.second_timer)
        self.alarm_screen.delete(self.minute_timer)
        self.alarm_screen.delete(self.hour_timer)

        self.second_timer = self.alarm_screen.create_text(
            445, 185, text='%.2i' % ((self.delta_time % 60) % 60), fill='white', font=self.standard_font)
        self.minute_timer = self.alarm_screen.create_text(
            275, 185, text='%.2i' % ((self.delta_time % 3600) // 60), fill='white', font=self.standard_font)
        self.hour_timer = self.alarm_screen.create_text(
            105, 185, text='%.2i' % (self.delta_time // 3600), fill='white', font=self.standard_font)

        # If all time scales were zeroed the alarm is played
        if int(self.alarm_screen.itemcget(self.second_timer, 'text')) == 0 and int(
                self.alarm_screen.itemcget(self.minute_timer, 'text')) == 0 and int(
                self.alarm_screen.itemcget(self.hour_timer, 'text')) == 0:
            self.play()
        else:
            self.root.after(1000, func=self.timer)

    # Touches the music referenced
    def play(self):
        winsound.PlaySound('Music/Mozart_Sonata_11.wav', winsound.SND_FILENAME+winsound.SND_ASYNC)

