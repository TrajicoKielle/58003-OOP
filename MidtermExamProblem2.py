from tkinter import *
class MyWindow:
    def __init__(self,win):

        self.lbl1 = Label(win, text="Metrics Units of Length")
        self.lbl1.place(x=200, y=50)
        self.lbl2 = Label(win,text="Enter the distance in centimeter(cm):")
        self.lbl2.place(x=100,y=100)
        self.lbl3 = Label(win, text= "Convert into meter(m):")
        self.lbl3.place(x=100,y=150)
        self.lbl4 = Label(win, text="Conversion into kilometer(km):")
        self.lbl4.place(x=100,y=200)
        self.txt1 = Entry(win,bd=1)
        self.txt1.place(x=300,y=100)
        self.txt2 = Entry(win,bd=1)
        self.txt2.place(x=300,y=150)
        self.txt3 = Entry(win,bd=3)
        self.txt3.place(x=300,y=200)
        self.btncon = Button(win,text="Convert", command = self.con)
        self.btncon.place(x=300,y=250)

    def con(self):
        self.txt2.delete(0, 'end')
        num1 = int(self.txt1.get())
        result1 = num1 * 0.01
        self.txt2.insert(END, str(result1))
        self.txt3.delete(0, 'end')
        num1 = int(self.txt1.get())
        result2 = num1 * 0.00001
        self.txt3.insert(END, str(result2))



window = Tk()
mywin = MyWindow(window)
window.geometry("600x400+10+10")
window.title("Midterm Exam Problem 2")
window.mainloop()
