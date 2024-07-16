from tkinter import *
from functools import partial
from calc import *



def create_buttons(root):
    start_x = 100
    start_y = 250
    for i in range(1, 4):
        for j in range(1, 4):
            btn = Button(root, text=str(i+(3*j)-3), command=partial(add_all_input, str(i+(3*j)-3), root), height=2, width=5)
            btn.place(x=start_x+i*50, y=start_y+j*45)

    # 0
    btn = Button(root, text='0', command=partial(add_all_input, '0', root), height=2, width=5)
    btn.place(x=start_x+2*50, y=start_y+45*4)

    # =
    btn = Button(root, text='=', command=partial(get_res, root), height=2, width=5)
    btn.place(x=start_x+3*50, y=start_y+45*4)

    # + - * /
    l = ['+', '-', '*', '/']
    for i in range(4):
        btn = Button(root, text=l[i], command=partial(add_all_input, l[i], root), height=2, width=5)
        btn.place(x=start_x+4*50, y=start_y+i*45+45)
    
    # clear button
    btn = Button(root, text='C', command=partial(clear_all_input, root), height=2, width=5)
    btn.place(x=start_x+1*50, y=start_y+4*45)


    # btn = Button(root, text='debug', command=print_inp, height=2, width=5)
    # btn.place(x=0, y=0)





    
