import tkinter as tk
from data import *
from PIL import ImageTk, Image
import math
import tkinter.font as font
# imports the tkinter library as tk for reference

# TO DO:
# add a marker on smith chart for typed in values
# fix dictionary (add negative half for values, just negate y-value)
# Mirror dot/marker for admittance
# line connecting complex impedance to admittance


win = tk.Tk()
canvas = tk.Canvas(win)
#print(font.families())

# print(coords)
# sets alias for tk

def getorigin(eventorigin):
    global x0, y0, text
    x0 = eventorigin.x
    y0 = eventorigin.y
    xy_coord = (x0, y0)
    #text.set(xy_coord)
    #click_dot = Canvas.create_oval(x0,y0,x0-7,y0-7,fill="red")
    # print(xy_coord)

win.title("Interactive Smith Chart")
# sets the title for the GUI

win.resizable(True, True)
# take boolean argument for x and y resize

win.minsize(width=100, height=100)
# sets the size of the GUI
win.configure(background='white')

# Code for the line

img = Image.open("sc.png")  # PIL solution
img = img.resize((805, 805), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)  # convert to PhotoImage

Canvas = tk.Canvas(win, width=805, height=805)
Canvas.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
image = Canvas.create_image(403, 404, anchor=tk.CENTER, image=img)

# Introduction
introduction = tk.Label(win, text="Welcome to the Interactive Smith Chart designed by Vickie Wu and Alex Mahon", font = ("Bahnschrift Light", 15, "bold"), bg = "white")
description = tk.Label(win,
                       text="This program is designed to help you understand the function of a Smith Chart. Enter the following values to begin.", font = ("Bahnschrift Light", 15, "bold"), bg = "white")
exit = tk.Button(win, text="Exit", font = ("Bahnschrift Light", 15, "bold"), bg = "white", command=win.quit)

"""
# Coordinate Value Output
button1 = tk.Button(win, text="Coords:%", command=getorigin)
text = tk.StringVar()
label = tk.Label(win, textvariable=text)
label.place(relx=0.9, rely=0.5, anchor=tk.E)
"""

# Placement of Description labels and buttons
introduction.place(relx=0.5, rely=0.03, anchor=tk.N)
description.place(relx=0.5, rely=0.06, anchor=tk.N)
exit.place(relx=0.02, rely=0.98, anchor=tk.SW)

# Characteristic Impedance Entry
entry1 = tk.Entry(win)
tk.Label(win, font = ("Bahnschrift Light", 10, "bold"), bg = "white",text="Z0").place(relx=0.03, rely=0.20, anchor=tk.NW)
entry1.grid(row=0, column=1)
entry1.place(relx=0.05, rely=0.2, anchor=tk.NW)

# Load Impedance Entry
entry2 = tk.Entry(win)
tk.Label(win, font = ("Bahnschrift Light", 10, "bold"), bg = "white",text="ZL").place(relx=0.03, rely=0.25, anchor=tk.NW)
entry2.grid(row=0, column=1)
entry2.place(relx=0.05, rely=0.25, anchor=tk.NW)

# Complex Impedance Entry
tk.Label(win, font = ("Bahnschrift Light", 10, "bold"), bg = "white",text="Enter complex impedance in the form a+bi:").place(relx=0.03, rely=0.46, anchor=tk.NW)
# Real Entry
tk.Label(win, font = ("Bahnschrift Light", 10, "bold"),bg = "white",text="a").place(relx=0.03, rely=0.48, anchor=tk.NW)
entry3 = tk.Entry(win)

entry3.grid(row=0, column=1)
entry3.place(relx=0.08, rely=0.48, anchor=tk.N)

# Complex Entry
entry4 = tk.Entry(win)

tk.Label(win, font = ("Bahnschrift Light", 10, "bold"),bg = "white",text="b").place(relx=0.03, rely=0.52, anchor=tk.NW)
entry4.grid(row=0, column=1)
entry4.place(relx=0.08, rely=0.52, anchor=tk.N)

#comp_num =(entry3, entry4)
#print(comp_num)
def RLC_calc():
    global RLC, text2, characteristic_admittance, text1, load_admittance, text3
    characteristic_impedance = entry1.get()
    load_impedance = entry2.get()
    if (characteristic_impedance and load_impedance) != '':
        characteristic_impedance = float(characteristic_impedance)
        load_impedance = float(load_impedance)
        normalized_impedance = float(load_impedance) / float(characteristic_impedance)
        RLC = float(normalized_impedance - 1) / float(normalized_impedance + 1)
        characteristic_admittance = (1 / float(characteristic_impedance))
        load_admittance = (1 / float(load_impedance))
        text1.set(characteristic_admittance)
        text2.set(RLC)
        text3.set(load_admittance)


def Points():
    global a, b, rounded_a, rounded_b
    a = entry3.get()
    b = entry4.get()
    if (a and b) != '':
        a = float(a)
        b = float(b)
        rounded_a = round(a, 1)
        rounded_b = round(b, 1)
        print(rounded_a, rounded_b)
        x_spos = coords.get((rounded_a, rounded_b))[0]
        y_spos = coords.get((rounded_a, rounded_b))[1]
        x_center = abs(405-x_spos)
        y_center = abs(405-y_spos)
        x = x_spos - 405
        y = y_spos - 405

        print(coords.get((rounded_a, rounded_b)))
        dot = Canvas.create_oval(x_spos,y_spos,x_spos-7,y_spos-7,fill="red")
        line = Canvas.create_line(x_spos, y_spos, 405, 405, fill="red", width = 2, arrow=tk.LAST)

        if(x_spos > 405 and y_spos > 405):
        	admittance_line = Canvas.create_line(405,405,405-x_center,405-y_center, fill="blue", width = 2, arrow=tk.FIRST)
        elif(x_spos < 405 and y_spos > 405):
        	admittance_line = Canvas.create_line(405,405,405+x_center,405-y_center, fill="blue", width = 2, arrow=tk.FIRST)
        elif(x_spos < 405 and y_spos < 405):
        	admittance_line = Canvas.create_line(405,405,405+x_center,405+y_center, fill="blue", width = 2, arrow=tk.FIRST)
        elif(x_spos > 405 and y_spos < 405):
        	admittance_line = Canvas.create_line(405,405,405-x_center,405+y_center, fill="blue", width = 2, arrow=tk.FIRST)

run = tk.Button(win, text="Run", font = ("Bahnschrift Light", 15, "bold"), bg = "white", command=lambda: [RLC_calc(), Points()])
run.place(relx=0.02, rely=0.14, anchor=tk.NW)

text2 = tk.StringVar()
label2 = tk.Label(win, font = ("Bahnschrift Light", 10, "bold"), bg = "white", textvariable=text2)
label2.place(relx=0.03, rely=0.3, anchor=tk.NW)

# Label for reflected load coefficient
rlc_label = tk.Label(win, font = ("Bahnschrift Light", 10, "bold"),bg = "white",text="Reflected Load Coefficient:")
rlc_label.place(relx=0.03, rely=0.28, anchor=tk.NW)

# Label for characteristic admittance
adm_label = tk.Label(win, font = ("Bahnschrift Light", 10, "bold"),bg = "white",text="Characteristic Admittance:")
adm_label.place(relx=0.03, rely=0.34, anchor=tk.NW)

# Label for load admittance
load_adm_label = tk.Label(win, font = ("Bahnschrift Light", 10, "bold"),bg = "white",text="Load Admittance")
load_adm_label.place(relx=0.03, rely=0.4, anchor=tk.NW)

text3 = tk.StringVar()
label3 = tk.Label(win, font = ("Bahnschrift Light", 10, "bold"),bg = "white",textvariable=text3)
label3.place(relx=0.03, rely=0.42, anchor=tk.NW)

# Label for characteristic impedance
text1 = tk.StringVar()
label1 = tk.Label(win, font = ("Bahnschrift Light", 10, "bold"),bg = "white",textvariable=text1)
label1.place(relx=0.03, rely=0.36, anchor=tk.NW)
# mouseclick event
win.bind("<Button 1>", getorigin)
win.mainloop()
# main loop needed for all GUIs





