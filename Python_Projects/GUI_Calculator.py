
from tkinter import *
import logging, sys

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
logging.debug('A debug message!')

root = Tk()
root.title("Calculator in Python")

input = Entry(root, width=40)
input.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
input.delete(0, END)

def button_click(number):
    logging.debug('in button_click()')
    current = input.get()
    input.delete(0, END)
    input.insert(0, str(current) + str(number))
    return 0

def button_clear():
    input.delete(0, END)

def button_minus():
    logging.debug('in button_minux()')
    no = int(input.get())
    global first_num
    first_num = no
    input.delete(0, END)
    global operation
    operation = "minus"

def button_add():
    logging.debug('in button_add()')
    no = int(input.get())
    global first_num
    first_num = no
    input.delete(0, END)
    global operation
    operation = 'plus'

def button_div():
    logging.debug('in button_div()')
    no = int(input.get())
    global first_num
    first_num = no
    input.delete(0, END)
    global operation
    operation = 'div'

def button_equal():
    logging.debug('in button_equal()')
    second_num = int(input.get())
    logging.debug('second no is %d', second_num)
    input.delete(0, END)
    global operation
    if(operation == 'minus'):
        result = first_num - second_num
    elif(operation == 'plus'):
        result = first_num + second_num
    elif(operation == 'div'):
        result = first_num / second_num
    else:
        result = 0

    logging.debug('result is %d', result)
    input.insert(0, result)

button1 = Button(root, text="1", padx=20, pady=10,command=lambda:button_click(1))
button2 = Button(root, text="2", padx=20, pady=10,command=lambda:button_click(2))
button3 = Button(root, text="3", padx=20, pady=10,command=lambda:button_click(3))
button4 = Button(root, text="4", padx=20, pady=10,command=lambda:button_click(4))
button5 = Button(root, text="5", padx=20, pady=10,command=lambda:button_click(5))
button6 = Button(root, text="6", padx=20, pady=10,command=lambda:button_click(6))
button7 = Button(root, text="7", padx=20, pady=10,command=lambda:button_click(7))
button8 = Button(root, text="8", padx=20, pady=10,command=lambda:button_click(8))
button9 = Button(root, text="9", padx=20, pady=10,command=lambda:button_click(9))
button0 = Button(root, text="0", padx=20, pady=10,command=lambda:button_click(9))

buttonPlus = Button(root, text="+", padx=20, pady=10, command=button_add)
buttonMinux = Button(root, text="-", padx=20, pady=10, command=button_minus)
buttonMulti = Button(root, text="/", padx=20, pady=10, command=button_div)
buttonResult = Button(root, text="=", padx=20, pady=10, command=button_equal)
buttonClear = Button(root, text="Clear", padx=10, pady=10, command=button_add)

label = Label(root, text="Project by Amit Kumar Singh", padx=10, pady=10)

button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
button3.grid(row=1, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=3, column=0)
button8.grid(row=3, column=1)
button9.grid(row=3, column=2)

button0.grid(row=4, column=0)
buttonPlus.grid(row=4, column=1)
buttonMinux.grid(row=4, column=2)
buttonResult.grid(row=5, column=0)
buttonClear.grid(row=5, column=1)
buttonMulti.grid(row=5, column=2)
label.grid(row=6, column=0, columnspan=3)

root.mainloop()

