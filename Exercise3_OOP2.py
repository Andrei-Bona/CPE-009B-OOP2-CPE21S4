from tkinter import *

class MyWindow:
    def __init__(self, win):

        win.config(bg = "Black")
        self.Label1 = Label(win, bg = "Black", fg="Blue", text="Calculator", font = ("Impact",20))
        self.Label1.place(x=130, y=10)

        self.Label2 = Label(win, text="Number 1:")
        self.Label2.place(x=50, y=50)

        self.Entry1 = Entry(win, bd=5)
        self.Entry1.place(x=125, y=50)

        self.Label3 = Label(win, text="Number 2:")
        self.Label3.place(x=50, y=100)

        self.Entry2 = Entry(win, bd=5)
        self.Entry2.place(x=125, y=100)

        self.Label4 = Label(win, text="Result:")
        self.Label4.place(x=50, y=150)

        self.Entry3 = Entry(win, bd=5)
        self.Entry3.place(x=125, y=150)

        self.Button1 = Button(win, fg = "Red", text = "Addition", command=self.add)
        self.Button1.place(x=50, y=200)
        self.Button2 = Button(win, fg = "Red", text = "Subtraction", command=self.sub)
        self.Button2.place(x=110, y=200)
        self.Button3 = Button(win, fg = "Red", text = "Multiplication", command=self.mul)
        self.Button3.place(x=185, y=200)
        self.Button3 = Button(win, fg = "Red", text = "Division", command=self.div)
        self.Button3.place(x=273, y=200)
        self.Button4 = Button(win, fg = "Red", text = "Clear", command=self.clear)
        self.Button4.place(x=160, y=240)

    def add (self):
        self.Entry3.delete(0, 'end')
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 + num2
        self.Entry3.insert(END, str(result))
    def sub (self):
        self.Entry3.delete(0, 'end')
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 - num2
        self.Entry3.insert(END, str(result))

    def mul (self):
        self.Entry3.delete(0, 'end')
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 * num2
        self.Entry3.insert(END, str(result))

    def div (self):
        self.Entry3.delete(0, 'end')
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 / num2
        self.Entry3.insert(END, str(result))

    def clear(self):
        self.Entry1.delete(0, 'end')
        self.Entry2.delete(0, 'end')
        self.Entry3.delete(0, 'end')



window = Tk()
MyWin = MyWindow(window)

window.geometry("400x300+10+10")
window.title("Standard Calculator")
window.mainloop()
