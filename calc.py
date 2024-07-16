import tkinter as tk
from button_functions import *

WIDTH, HEIGHT = 350, 500
all_input = ''

def clear_all_input(root):
    global all_input
    all_input = ''
    w = Label(root, text=all_input, width=WIDTH, height=5)
    w.place(x=0, y=0)
    add_all_input('', root)

def add_all_input(char, root):
    global all_input
    all_input += char
    w = Label(root, text=all_input)
    w.place(x=0, y=0)

def get_res(root):
    try:
        t = eval(all_input)
    except:
        t = 'Math error'
    w = Label(root, text=t)
    w.place(x=0, y=50)

def main():
    global w
    root = Tk()
    root.geometry(f"{WIDTH}x{HEIGHT}")
    root.title('calculator')
    root.config(bg='lightgrey')

    w = Label(root, text=all_input, width=WIDTH, height=5)
    w.place(x=0, y=0)
    
    create_buttons(root)

    exec("res = 1+1")

    root.mainloop()




if __name__ == "__main__":
    main()