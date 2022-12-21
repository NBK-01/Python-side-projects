from tkinter import *
from tkinter import ttk
import math

def click():
    entered_text=textentry.get()

def search():
    print(a.get())
    print(b.get())
    print(c.get())
    return ''

#Window and Title
root = Tk()
root.title("Quadratic Calculator")
root.configure(background="black")
Label (root, text="Quadratic Calculator", bg="black", fg="grey", font="none 18 bold") .grid(row=1, column=0, sticky=N)

a=float()
b=float()
c=float()

#inputs
Label (root, text="Enter your A value!", bg="black", fg="grey", font="none 12 bold") .grid(row=2, column=0, sticky=N)
textentry = Entry(root, width=20, bg="white", textvariable=a)
textentry.grid(row=3, column=0, sticky=N)
Label (root, text="Enter your B value!", bg="black", fg="grey", font="none 12 bold") .grid(row=4, column=0, sticky=N)
textentry = Entry(root, width=20, bg="white", textvariable=b)
textentry.grid(row=5, column=0, sticky=N)
Label (root, text="Enter your c value!", bg="black", fg="grey", font="none 12 bold") .grid(row=6, column=0, sticky=N)
textentry = Entry(root, width=20, bg="white", textvariable=c)
textentry.grid(row=7, column=0, sticky=N)

#Answer
Label (root, text="Answer!", bg="black", fg="grey", font="none 12 bold").grid(row=8, column=0, sticky=N)
output = Text(root, width=75, height=6, wrap=WORD, bg="white")
output.grid(row=9, column=0, columnspan=2, sticky=N)
a = float(a)
b = float(b)
c = float(c)
d = (math.pow(b,2)-4*a*c)
if d < 0:
   print("There is no answer")
elif d == 0:
     x =(-b + (d))/ (2*a)
     print("There is one answer:",x)

else:
    x1 = ( -b + (math.sqrt(d)))/ (2*a)
    x2 = ( -b - (math.sqrt(d)))/ (2*a)
    print("There are two answers:", x1,"and" ,x2)

#Solve Button
Button(root, text="Solve", width=6, command=search) .grid(row=10, column=0,
sticky=N)

root.mainloop()
