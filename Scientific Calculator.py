from tkinter import *
import math

def iCalc(source, side):
    storeObj = Frame(source, borderwidth=4, bd=4, bg="pink")
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj

def button(source, side, text, command=None):
    storeObj = Button(source, text=text, command=command)
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj

class app(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font', 'arial 20 bold')
        self.pack(expand=YES, fill=BOTH)
        self.master.title('Scientific Calculator')

        display = StringVar()
        Entry(self, relief=RIDGE, textvariable=display,
              justify='right', bd=30, bg="pink").pack(side=TOP,
                                                            expand=YES, fill=BOTH)

        # add scientific calculator buttons
        clearButtons = iCalc(self, TOP)
        for clearButton in (["C"]):
            erase = iCalc(clearButtons, LEFT)
            for ichar in clearButton:
                button(erase, LEFT, ichar, lambda storeObj=display, q=ichar: storeObj.set(''))

        sciButtons = iCalc(self, TOP)
        button(sciButtons, LEFT, "sin", lambda storeObj=display: storeObj.set(math.sin(float(display.get()))))
        button(sciButtons, LEFT, "cos", lambda storeObj=display: storeObj.set(math.cos(float(display.get()))))
        button(sciButtons, LEFT, "tan", lambda storeObj=display: storeObj.set(math.tan(float(display.get()))))
        button(sciButtons, LEFT, "√", lambda storeObj=display: storeObj.set(math.sqrt(float(display.get()))))
        button(sciButtons, LEFT, "log", lambda storeObj=display: storeObj.set(math.log10(float(display.get()))))
        button(sciButtons, LEFT, "ln", lambda storeObj=display: storeObj.set(math.log(float(display.get()))))
        button(sciButtons, LEFT, "pi", lambda storeObj=display: storeObj.set(math.pi))
        button(sciButtons, LEFT, "e", lambda storeObj=display: storeObj.set(math.e))

        for numButton in ("789/", "456*", "123-", "0.+"):
            FunctionNum = iCalc(self, TOP)
            for iEquals in numButton:
                button(FunctionNum, LEFT, iEquals, lambda storeObj=display, q=iEquals: storeObj.set(storeObj.get() + q))

        EqualButton = iCalc(self, TOP)
        for iEquals in "=":
            if iEquals == '=':
                btniEquals = button(EqualButton, LEFT, iEquals)
                btniEquals.bind('<ButtonRelease-1>', lambda e,s=self, storeObj=display: s.calc(storeObj), '+')

            else:
                btniEquals = button(EqualButton, LEFT, iEquals,
                                    lambda storeObj=display, s=' %s ' % iEquals: storeObj.set(storeObj.get() + s))

    def calc(self, display):
        try:
            display.set(eval(display.get()))
        except:
            display.set("ERROR")


if __name__=='__main__':
    app().mainloop()