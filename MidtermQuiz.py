from tkinter import *
class MyWindow:
    def __init__(self,win):

#widgets start from here
        self.lbl1 = Label(win,text="Enter Number:")
        self.lbl1.place(x=100,y=50)
        self.lbl3 = Label(win, text="Result")
        self.lbl3.place(x=100,y=150)
        self.txt1 = Entry(win,bd=1)
        self.txt1.place(x=200,y=50)
        self.txt2 = Entry(win,bd=3)
        self.txt2.place(x=200,y=150)
        self.btnfahrtocel = Button(win,text="Fahrenheit to Celsius", fg = "Purple")
        self.btnfahrtocel.place(x=100,y=200)
        self.btnfahrtocel.bind('<Button-1>',self.fahrtocel)
        self.btnkelvtocel = Button(win,text="Kelvin to Celsius", fg = "Orange",command = self.kelvtocel)
        self.btnkelvtocel.place(x=300,y=200)
        self.btnclr = Button(win,text="Clear",fg = "Red",command= self.clr)
        self.btnclr.place(x=400,y=100)



    def fahrtocel(self,fahrtocel):
        self.txt2.delete(0,'end')
        num1 = int(self.txt1.get())
        result = (num1-32)*.556
        self.txt2.insert(END,str(result))

    def kelvtocel(self):
        self.txt2.delete(0, 'end')
        num1 = int(self.txt1.get())
        result = num1-273.15
        self.txt2.insert(END, str(result))

    def clr(self):
        self.txt1.delete(0, 'end')
        self.txt2.delete(0, 'end')



window = Tk()
mywin = MyWindow(window)
window.geometry("600x400+10+10")
window.title("Conversion Methods")
window.mainloop()







