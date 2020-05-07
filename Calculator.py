# -*- coding: utf-8 -*-
"""
Created on Wed Apr 8 18:20:41 2020

@author: BHASKAR NEOGI 
"""
from tkinter import*
import math

# Click Method :
def btnClick(numbers) :
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

# Clear Method :
def btnClear() :
    global operator
    operator = " "
    text_Input.set(" ")

# Equal Method :
def btnEquals() :
    global operator
    ans = str(eval(operator))
    text_Input.set(ans)
    operator = " "

# Square Method :
def btnSquare() :
    global operator
    operator = float(operator)
    ans1 = operator*operator
    text_Input.set(ans1)

# Sqrt Method : 
def btnSqrt() :
    global operator
    operator = float (operator)
    ans2 = math.sqrt(operator)
    text_Input.set(ans2)

# Deletion Method :
def btnDel() :
    global operator
    ans3 = operator[ : -1]
    text_Input.set(ans3)
    operator = ans3

# Percentage Method :
def btnPercent() :
    global operator    
    ans4 = eval(operator)/100
    text_Input.set(ans4)


cal = Tk()

cal.title("Calculator")
operator = ""
text_Input = StringVar()

txtDisplay = Entry(cal, font=('arial', 20, 'bold'), textvariable = text_Input, bd = 10, insertwidth = 6,
                                               bg = 'grey', fg = 'yellow', justify = 'right').grid(columnspan=4)
######################################  row1 :

button7 = Button(cal, padx=12, pady=12, bd=8, fg='black',  font=('arial', 10, 'bold'),
                             text='7', command = lambda : btnClick(7))
button7.grid(row=1, column=0)

button8 = Button(cal, padx=12, pady=12, bd=8, fg='black',  font=('arial', 10, 'bold'),
                             text='8', command = lambda : btnClick(8))
button8.grid(row=1, column=1)

button9 = Button(cal, padx=12, pady=12, bd=8, fg='black',  font=('arial', 10, 'bold'),
                             text='9', command = lambda : btnClick(9))
button9.grid(row=1, column=2)


buttonAdd = Button(cal, padx=11, pady=16, bd=9, fg='black',  font=('arial', 14, 'bold'),
                             text='+', command = lambda : btnClick('+'))
buttonAdd.grid(row=1, column=3)

#######################################  row2 ;

button4 = Button(cal, padx=12, pady=12, bd=8, fg='black',  font=('arial', 10, 'bold'),
                             text='4', command = lambda : btnClick(4))
button4.grid(row=2, column=0)

button5 = Button(cal, padx=12, pady=12, bd=8, fg='black',  font=('arial', 10, 'bold'),
                             text='5', command = lambda : btnClick(5))
button5.grid(row=2, column=1)

button6 = Button(cal, padx=12, pady=12, bd=8, fg='black',  font=('arial', 10, 'bold'),
                             text='6', command = lambda : btnClick(6))
button6.grid(row=2, column=2)

buttonSub = Button(cal, padx=12, pady=16, bd=9, fg='black',  font=('arial', 14, 'bold'),
                             text='-', command = lambda : btnClick('-'))
buttonSub.grid(row=2, column=3)

#######################################  row3 :

button1 = Button(cal, padx=12, pady=12, bd=8, fg='black',  font=('arial', 10, 'bold'),
                             text='1', command = lambda : btnClick(1))
button1.grid(row=3, column=0)

button2 = Button(cal, padx=12, pady=12, bd=8, fg='black',  font=('arial', 10, 'bold'),
                             text='2', command = lambda : btnClick(2))
button2.grid(row=3, column=1)

button3 = Button(cal, padx=12, pady=12, bd=8, fg='black', font=('arial', 10, 'bold'),
                             text='3', command = lambda : btnClick(3))
button3.grid(row=3, column=2)

buttonMul = Button(cal, padx=12, pady=16, bd=9, fg='black', font=('arial', 14, 'bold'),
                             text='*', command = lambda : btnClick('*'))
buttonMul.grid(row=3, column=3)

######################################  row4 :


buttonPower = Button(cal,padx=9, pady=7, bd=8, fg='black', font=('arial', 14, 'bold'),
                                   text='^', command =lambda : btnClick('**'))
buttonPower.grid(row=4, column=0)

buttonPercent = Button(cal, padx=8, pady=6, bd=8, fg='black', font=('arial', 14, 'bold'),
                                      text='%', command = btnPercent)
buttonPercent.grid(row=4, column=1)

buttonDiv = Button(cal, padx=14, pady=7, bd=8, fg='black',  font=('arial', 14, 'bold'),
                             text='/', command = lambda : btnClick('/'))
buttonDiv.grid(row=4, column=2)

buttonDel = Button(cal, padx=8, pady=20, bd=9, fg='black',bg='red', font=('arial', 10, 'bold'),
                              text='DEL', command = btnDel)
buttonDel.grid(row=4, column=3)


#######################################  row5 :

buttonSquare = Button(cal, padx=8, pady=12, bd=8, fg='black', font=('arial', 10, 'bold'),
                                     text='x^2', command = btnSquare)
buttonSquare.grid(row=5, column=0)

buttonSqrt = Button(cal, padx=10, pady=11, bd=8, fg='black', font=('arial', 10, 'bold'),
                                  text='sqrt', command = btnSqrt)
buttonSqrt.grid(row=5, column=1)

buttonClr = Button(cal, padx=16, pady=12, bd=10, fg='black',bg='sky blue',  font=('arial', 10, 'bold'),
                             text='Clr', command = btnClear)
buttonClr.grid(row=5, column=2)

buttonEqu = Button(cal, padx=12, pady=21, bd=9, fg='black',bg='light pink',  font=('arial', 14, 'bold'),
                             text='=', command = btnEquals)
buttonEqu.grid(row=5, column=3)

#######################################  row6 :


buttonPoint = Button(cal, padx=13, pady=10, bd=8, fg='black', font=('arial', 14, 'bold'),
                           text='.', command = lambda : btnClick('.'))
buttonPoint.grid(row=6, column=0)

button0 = Button(cal, padx=13, pady=14, bd=8, fg='black',  font=('arial', 10, 'bold'),
                             text='0', command = lambda : btnClick(0))
button0.grid(row=6, column=1)

buttonDzero = Button(cal, padx=14, pady=13, bd=6, fg='black', font=('arial', 14, 'bold'),
                     text='00', command = lambda : btnClick('00'))
buttonDzero.grid(row=6, column=2)

buttonTzero = Button(cal, padx=14, pady=13, bd=6, fg='black', font=('arial', 14, 'bold'),
                     text='000', command = lambda : btnClick('000'))
buttonTzero.grid(row=6, column=3)




cal.mainloop()
