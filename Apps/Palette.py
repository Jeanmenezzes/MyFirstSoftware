# THIS APP WHERE MADE WITH THE OBJECT TO CHANGE THE CIRCLE CENTER COLOR BY THE USER'S CLICK IN ANOTHER CIRCLE WHAT
# CONTAINS PART OF THE INTONATION THAT WILL BE REMOVED FROM THE CENTRAL CIRCLE

# IMPORTING TKINTER METHODS
from tkinter import *


# CREATES A CLASS TO BEING IMPORTED FROM THE MAIN FILE
class PaletteApp(object):
    # THE WIDTH AND HEIGHT OF THE APP
    xy = '300x200'

    # CREATES A CANVAS HOLDING THE COLORS CIRCLES
    def __init__(self, root):
        master = root

        self.canvas = Canvas(master, width=300, height=200, bg='gray')
        self.canvas.pack()
        self.canvas.focus_force()

        self.green_color = "#%02x%02x%02x" % (0, 255, 0)
        self.red_color = "#%02x%02x%02x" % (0, 0, 255)
        self.blue_color = "#%02x%02x%02x" % (255, 0, 0)
        self.white_RGB = (255, 255, 255)
        self.white_color = "#%02x%02x%02x" % self.white_RGB

        # Center of the central circle is 150 to x and 60 to y, being the radius equal to 50.
        self.central_circle = self.canvas.create_oval((100, 10), (200, 110), fill=self.white_color, tag='bola1')

        # Center of the red circle is 90 to x and 150 to y, being the radius equal to 50.
        self.blue_circle = self.canvas.create_oval((65, 125), (115, 175), fill=self.blue_color)
        
        # Center of the green circle is 150 to x and 150 to y, being the radius equal to 25
        self.green_circle = self.canvas.create_oval((125, 125), (175, 175), fill=self.green_color)
        
        # Center of the blue circle is 210 to x and 150 to y, being the radius equal to 50.
        self.red_circle = self.canvas.create_oval((185, 125), (235, 175), fill=self.red_color)

        # Bind the screen to a function what uses the motion to recognize what circle where pressed
        self.canvas.bind(('<Motion>', '<Button-1>'), func=self.action)

    # That is the function that redirect the color variable to the color of pressed circle
    def action(self, event):
        self.color = ''

        # At the start we just bind the y axis to a variable cause all circles are in the same y axis area and we also
        # reduced by 150 to put this amount in the central y point of circles
        # We verify what part of axis x is pressed  and all the subtractions were made to verify if the click have
        # been done in the circle area
        self.y = event.y-150

        if event.x <= 115:
            self.x = event.x-90
            self.color = 'red'

        elif event.x <= 175:
            self.x = event.x-150
            self.color = 'green'

        elif event.x > 175:
            self.x = event.x-210
            self.color = 'blue'

        # Put x and y in the absolute value (modulus)
        self.x = abs(self.x)
        self.y = abs(self.y)

        # How the circle axis have just 25 pixels of diameter so the circle area should be less than the sum of axis
        # x and y squared. If the y axis is out of circle this if block will not activate
        if (self.x**2 + self.y**2) < 25**2:

            # In this if block we verify what color is in the color variable and reduces from the white central circle
            # the intonation by 10 Hexadecimal unities stopping at zero
            if self.color == 'red':
                self.white_RGB = (self.white_RGB[0]-10, self.white_RGB[1], self.white_RGB[2])
                if self.white_RGB[0] < 0:
                    self.white_RGB = (0, self.white_RGB[1], self.white_RGB[2])

                self.white_color = "#%02x%02x%02x" % self.white_RGB
                self.canvas.itemconfig(self.central_circle, fill=self.white_color)

            elif self.color == 'green':
                self.white_RGB = (self.white_RGB[0], self.white_RGB[1]-10, self.white_RGB[2])
                if self.white_RGB[1] < 0:
                    self.white_RGB = (self.white_RGB[0], 0, self.white_RGB[1])

                self.white_color = "#%02x%02x%02x" % self.white_RGB
                self.canvas.itemconfig(self.central_circle, fill=self.white_color)

            elif self.color == 'blue':
                self.white_RGB = (self.white_RGB[0], self.white_RGB[1], self.white_RGB[2]-10)
                if self.white_RGB[2] < 0:
                    self.white_RGB = (self.white_RGB[0], self.white_RGB[1], 0)

                self.white_color = "#%02x%02x%02x" % self.white_RGB
                self.canvas.itemconfig(self.central_circle, fill=self.white_color)

