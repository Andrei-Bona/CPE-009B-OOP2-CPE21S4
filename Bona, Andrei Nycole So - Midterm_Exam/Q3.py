from tkinter import *

class MyWindow:
    def __init__(self, win):
        self.Label1 = Label(win, text="Enter your fullname: ", fg = 'red')
        self.Label1.place(x=70, y=100)

        self.Entry1 = Entry(win, bd=5)
        self.Entry1.place(x=300, y=100)

        self.Button = Button(win, fg="Red", text="Click to display you Fullname", command = self.output)
        self.Button.place(x=70, y=150)

        self.Entry2 = Entry(win, bd=5)
        self.Entry2.place(x=300, y=150)

    def output(self):
        print1 = self.Entry1.get()
        output1 = print1
        self.Entry2.insert(END, str(output1))

window = Tk()
MyWin = MyWindow(window)

window.geometry("600x300+10+10")
window.title("Midterm in OOP")
window.mainloop()