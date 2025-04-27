import tkinter as tk
from tkinter import colorchooser

currx,curry=0,0
pen=5
color="white"
gbg="black"

def cbg():
    global gbg
    new_bg=colorchooser.askcolor()[1]
    if new_bg:
        gbg=new_bg
        canvas.config(bg=gbg)

def color_picker():
    global color
    new_color=colorchooser.askcolor()[1]
    if new_color:
        color=new_color

def clear_canvas():
    canvas.delete("all")

def Large_pen():
    global pen 
    pen=10

def Medium_pen():
    global pen
    pen =5

def Small_pen():
    global pen 
    pen = 3

def start_position(event):
    global currx,curry
    currx,curry=event.x,event.y

def draw_line(event):
    global currx,curry
    canvas.create_line(currx,curry,event.x,event.y,fill=color,width=pen,smooth=True)
    currx,curry=event.x,event.y

window=tk.Tk()
window.title("Nikhil's Canvas")
window.geometry("900x700")

Sapp=tk.Label(window,text="Nikhil's Canvas",font=('areal',18))
Sapp.pack(pady=10)

toolbar=tk.Frame(window)
toolbar.pack(pady=10)

choose_color=tk.Button(toolbar,text="Choose Color",command=color_picker)
choose_color.pack(side=tk.LEFT,padx=10)

change_bg=tk.Button(toolbar,text="Change Background",command=cbg)
change_bg.pack(side=tk.LEFT,padx=10)

clear_canvas=tk.Button(toolbar,text="Clear Canvas",command=clear_canvas)
clear_canvas.pack(side=tk.LEFT,padx=10)

pen_size=tk.Label(toolbar,text="Pen Size:",font=("Areal",12))
pen_size.pack(side=tk.LEFT,padx=10)

small=tk.Button(toolbar,text="Small",command=Small_pen)
small.pack(side=tk.LEFT,padx=10)

Medium=tk.Button(toolbar,text="Medium",command=Medium_pen)
Medium.pack(side=tk.LEFT,padx=10)

Large=tk.Button(toolbar,text="Large",command=Large_pen)
Large.pack(side=tk.LEFT,padx=10)

canvas=tk.Canvas(window,bg=gbg)
canvas.pack(expand=True,fill=tk.BOTH,padx=10,pady=10)

canvas.bind("<Button-1>", start_position)
canvas.bind("<B1-Motion>", draw_line)

instruction=tk.Label(window,text="Click and Drag to draw")
instruction.pack(pady=10)

window.mainloop()
