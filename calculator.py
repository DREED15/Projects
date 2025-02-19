from tkinter import *
import math

root = Tk()
blank_space = " "
root.title(50 * blank_space + "VS Code Calculation")
root.resizable(width=False, height=False)
root.geometry("438x573+460+40")

coverFrame = Frame(root, bd=20, pady=2, relief=RIDGE)
coverFrame.grid()

coverMainFrame = Frame(coverFrame, bd=10, pady=2, bg = 'cadetblue', relief=RIDGE)
coverMainFrame.grid()

MainFrame = Frame(coverMainFrame, bd=5, pady=2, relief=RIDGE)
MainFrame.grid()

class Calculator():
    def __init__(self):
        self.total = 0
        self.current =""
        self.input_value = True
        self.check_sum = False
        self.op = ""
        self.result = False

    def numberEnter(self,num):
        self.result = False
        firstnum = entDisplay.get()
        secondnum = str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value = False
        else:
            if secondnum == '.':
                if secondnum in firstnum:
                    return
            self.current = firstnum + secondnum
            self.display(self.current)
    def display(self,value):
        entDisplay.delete(0, END)
        entDisplay.insert(0, value)

    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.valid_function()
        else:
            self.total = float(entDisplay.get())

    def valid_function(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "sub":
            self.total -= self.current
        if self.op == "multi":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        if self.op == "mod":
            self.total %= self.current
        self.input_value = True
        self.check_sum = False
        self.display(self.total)

    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = False

    def backspace(self):
        numLen = len(entDisplay.get())
        entDisplay.delete(numLen - 1, 'end')
        if numLen == 1:
            entDisplay.insert(0, "0")

    def Clear_Entry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value = True

    def all_Clear_Entry(self):
        self.Clear_Entry()
        self.total = 0

    def mathsPM(self):
        self.result = False
        self.current = -(float(entDisplay.get())) 
        self.display(self.current)

    def squared(self):
        self.result = False
        self.current = math.sqrt(float(entDisplay.get()))
        self.display(self.current)

    def cos(self):
        self.result = False
        self.current = math.cos(math.radians(float(entDisplay.get())))
        self.display(self.current)

    def tan(self):
        self.result = False
        self.current = math.tan(math.radians(float(entDisplay.get())))
        self.display(self.current)

    def sin(self):
        self.result = False
        self.current = math.sin(math.radians(float(entDisplay.get())))
        self.display(self.current)

added_value = Calculator()
entDisplay = Entry (MainFrame, font = ('arial',18, 'bold'), bd = 14, width = 30, bg = 'cadetblue', justify = RIGHT)
entDisplay.grid(row=0, column=0, columnspan=4, pady=1)
entDisplay.insert(0, "0")

numberpad = "789456123"
i = 0
btn = []

for j in range (3,6):
    for k in range(3):
        btn.append(Button(MainFrame, width = 6, height = 2, font = ('arial',16, 'bold'), bd = 4, text = numberpad[i]) )
        btn[i].grid(row = j, column = k, pady = 1)
        btn[i]["command"] = lambda x = numberpad[i]: added_value.numberEnter(x)
        i += 1

btnBackSpace = Button(MainFrame, width = 6, height = 2, font = ('arial',16, 'bold'), bd = 4, text = "Delete", 
bg = 'cadetblue', command = added_value.backspace) 
btnBackSpace.grid(row = 1, column = 0, pady = 1)

btnClear = Button(MainFrame, width = 6, height = 2, font = ('arial',16, 'bold'), bd = 4, text = chr(67),
bg = 'cadetblue', command = added_value.Clear_Entry)
btnClear.grid(row = 1, column = 1, pady = 1)

btnClearAll = Button(MainFrame, width = 6, height = 2, font = ('arial',16, 'bold'), bd = 4, 
text = chr(67) + chr(69), bg = 'cadetblue', command = added_value.all_Clear_Entry)
btnClearAll.grid(row = 1, column = 2, pady = 1)

btnPM = Button(MainFrame, width = 6, height = 2, font = ('arial',16, 'bold'), bd = 4, text = chr(177),
bg = 'cadetblue', command = added_value.mathsPM)
btnPM.grid(row = 1, column = 3, pady = 1)

#=====================================Scientific================================================================

btnSq = Button(MainFrame, width = 6, height = 2, font = ('arial',16, 'bold'), bd = 4, text = "√", command = added_value.squared)
btnSq.grid(row = 2, column = 0, pady = 1)

btnCos = Button(MainFrame, width = 6, height = 2, font = ('arial',16, 'bold'), bd = 4, text = "Cos", command = added_value.cos)
btnCos.grid(row = 2, column = 1, pady = 1)

btnTan = Button(MainFrame, width = 6, height = 2, font = ('arial',16, 'bold'), bd = 4, text = "Tan", command = added_value.tan)
btnTan.grid(row = 2, column = 2, pady = 1)

btnSin = Button(MainFrame, width = 6, height = 2, font = ('arial',16, 'bold'), bd = 4, text = "Sin",
bg = 'cadetblue', command = added_value.sin)
btnSin.grid(row = 2, column = 3, pady = 1)

#========================Normal Operations===========================================================================

btnAdd = Button(MainFrame, width = 6, height = 2, font = ('arial',16, 'bold'), bd = 4, text = "+",
bg = 'cadetblue', command = lambda:added_value.operation("add"))
btnAdd.grid(row = 3, column = 3, pady = 1)

btnSub = Button(MainFrame, width = 6, height = 2, font = ('arial',16, 'bold'), bd = 4, text = "-",
bg = 'cadetblue', command = lambda:added_value.operation("sub"))
btnSub.grid(row = 4, column = 3, pady = 1)

btnMult = Button(MainFrame, width = 6, height = 2, font = ('arial',16, 'bold'), bd = 4, text = "*",
bg = 'cadetblue', command = lambda:added_value.operation("multi"))
btnMult.grid(row = 5, column = 3, pady = 1)

btnDiv = Button(MainFrame, width = 6, height = 2, font = ('arial',16, 'bold'), bd = 4, text = chr(247),
bg = 'cadetblue', command = lambda:added_value.operation("divide"))
btnDiv.grid(row = 6, column = 3, pady = 1)

btnZero = Button(MainFrame, width = 6, height = 2, font = ('arial',16, 'bold'), bd = 4, text = "0",
bg = 'cadetblue')
btnZero.grid(row = 6, column = 0, pady = 1)

btnDot = Button(MainFrame, width = 6, height = 2, font = ('arial',16, 'bold'), bd = 4, text = ".",
bg = 'cadetblue')
btnDot.grid(row = 6, column = 1, pady = 1)

btnEquals = Button(MainFrame, width = 6, height = 2, font = ('arial',16, 'bold'), bd = 4, text = "=",
bg = 'cadetblue', command = added_value.sum_of_total)
btnEquals.grid(row = 6, column = 2, pady = 1)

#======================================================================================================




root.mainloop()
