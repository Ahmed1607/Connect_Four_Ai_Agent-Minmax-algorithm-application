from tkinter import *

root = Tk()  # this is for the form
root.geometry("800x600")  # the size of the form window
root.title("CONNECT-4 GUI")  # title of the form


def ev1():

    if val_1.get() == True and val_3.get() == True:
        root.destroy()
        import minmax
    elif val_2.get() == True and val_3.get() == True:
        root.destroy()
        import alphabeta
    elif val_1.get() == True and val_4.get() == True:
        root.destroy()
        import minmax_hard
    elif val_2.get() == True and val_4.get() == True:
        root.destroy()
        import alphabeta_hard


lb1 = Label(root, text="Choose algorithm ", font="0")
lb1.place(x=10, y=20)

val_1 = BooleanVar()
check_1 = Checkbutton(root, text="MinMax", font="0", variable=val_1)
check_1.place(x=200, y=20)


val_2 = BooleanVar()
check_2 = Checkbutton(root, text="Alpha-Beta", font="0", variable=val_2)
check_2.place(x=350, y=20)


lb2 = Label(root, text="Choose difficulty ", font="0")
lb2.place(x=10, y=150)

val_3 = BooleanVar()
check_3 = Checkbutton(root, text="Easy", font="0", variable=val_3)
check_3.place(x=200, y=150)

val_4 = BooleanVar()
check_4 = Checkbutton(root, text="Hard", font="0", variable=val_4)
check_4.place(x=350, y=150)

st = Button(root, command=ev1, text="start game", fg="Black", font="30")
st.place(x=300, y=260)


root.mainloop()
