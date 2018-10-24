from tkinter import*
def icalc(source, side):
    storeObj = Frame(source, borderwidth=4, bd=4, bg="blue")
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj
def button(source, side, text, command=None):
    storeObj = Button( source, text=text, command=command)
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj

class app(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('Font','arial 20 bold')
        self.pack(expand=YES,fill=BOTH)
        self.master.title('calculator')


        display =StringVar()
        Entry(self, relief=RIDGE,
                 textvariable=display, justify='right', bd=30,bg="blue").pack(side=TOP, expand=YES,
                                                                              fill=BOTH)
        for clearBut in(["CE"],["C"]):
            erase = icalc(self,TOP)
            for ichar in clearBut:
                button(erase, LEFT, ichar,
                       lambda storeObj=display, q=ichar: storeObj.set(''))

        for NumBut in ("789/", "456*", "123-", "0.+"):
            FunctionNum = icalc(self, TOP)
            for char in NumBut:
                button(FuntionNum, LEFT, char,
                       lambda storeObj=display, q=char: storeObj.set(storeObj.get() + q))


if __name__== '__main__':
    app().mainloop()        
