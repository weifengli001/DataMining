import tkinter
window = tkinter.Tk()
index = 0


def myprint(index):
    print(index)

def button1_click(event):
    global index
    index = event.x
    myprint(index)
canvas = tkinter.Canvas(window, width=200, height=100)
canvas.pack()
canvas.bind("<Button>", button1_click)

myprint(index)
window.mainloop()


