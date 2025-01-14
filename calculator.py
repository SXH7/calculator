from tkinter import *

root = Tk()
root.title("Simple Calculator")
root.configure(bg='#161616')

e = Entry(root, width=35 , borderwidth=5 , bg= '#B2BEB5')
e.grid(row=0 , column=0, columnspan=3, padx=10 , pady=10)

def button_click(number):
   
   current= e.get()
   e.delete(0, END)
   e.insert(0,str(current) + str(number))
def button_clear():
    e.delete(0, END)
def button_add():
   first_number = e.get()
   global f_num
   global math
   math="addition"
   f_num = int(first_number)
   e.delete(0, END)

def button_equal():
    second_number=int(e.get())
    first_number = f_num
    e.delete(0, END)
    if math== "addition":
        e.insert(0, f_num + second_number)

    if math== "subtraction":
        e.insert(0, f_num - second_number)

    if math== "multiplication":
        e.insert(0, f_num * second_number)

    if math== "division":
        e.insert(0, f_num / second_number)
        
    if math== "exponential":
        initial = first_number
        e.insert(0, str(initial**second_number))

    if math== "root":
        initial = first_number
        e.insert(0, str(initial**(1/second_number)))

def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math="subtraction"
    f_num = int(first_number)
    e.delete(0, END)
    return

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math="multiplication"
    f_num = int(first_number)
    e.delete(0, END)
    return

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math="division"
    f_num = int(first_number)
    e.delete(0, END)
    return

def button_exponent():
    first_number = e.get()
    global f_num
    global math
    math="exponential"
    f_num = int(first_number)
    e.delete(0, END)
    return

def button_root():
    first_number = e.get()
    global f_num
    global math
    math="root"
    f_num = int(first_number)
    e.delete(0, END)
    return   



button_1 = Button(root, text="1",padx=40,pady=20, command=lambda: button_click(1), bg='#A9A9A9')
button_2 = Button(root, text="2",padx=43,pady=20, command=lambda: button_click(2), bg='#A9A9A9')
button_3 = Button(root, text="3",padx=41,pady=20, command=lambda: button_click(3), bg='#A9A9A9')

button_4 = Button(root, text="4",padx=40,pady=20, command=lambda: button_click(4), bg='#A9A9A9')
button_5 = Button(root, text="5",padx=43,pady=20, command=lambda: button_click(5), bg='#A9A9A9')
button_6 = Button(root, text="6",padx=41,pady=20, command=lambda: button_click(6), bg='#A9A9A9')

button_7 = Button(root, text="7",padx=40,pady=20, command=lambda: button_click(7), bg='#A9A9A9')
button_8 = Button(root, text="8",padx=43,pady=20, command=lambda: button_click(8), bg='#A9A9A9')
button_9 = Button(root, text="9",padx=41,pady=20, command=lambda: button_click(9), bg='#A9A9A9')

button_0 = Button(root, text="0",padx=40,pady=20, command=lambda: button_click(0), bg='#A9A9A9')
button_plus = Button(root, text="+",padx=39,pady=20, command=button_add, bg='#A9A9A9') 
button_equal = Button(root, text="=",padx=91, pady=20, command=button_equal, bg='#A9A9A9')
button_clear = Button(root, text="<-----", padx=79, pady=20, command=button_clear, bg='#A9A9A9')

button_subtract = Button(root, text="-",padx=40,pady=20, command=button_subtract, bg='#A9A9A9') 
button_multiply = Button(root, text="*",padx=44,pady=20, command=button_multiply, bg='#A9A9A9') 
button_divide = Button(root, text="/",padx=41,pady=20, command=button_divide, bg='#A9A9A9') 
button_exponent = Button(root, text="xʸ",padx=140,pady=20, command=button_exponent, bg='#A9A9A9')
button_root = Button(root, text="√", padx=140, pady=20 ,command = button_root, bg='#A9A9A9')

# Putting the button on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
 
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_plus.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

button_subtract.grid(row=6,column=0)
button_multiply.grid(row=6,column=1)
button_divide.grid(row=6,column=2)
button_exponent.grid(row=7, column=0, columnspan=3)
button_root.grid(row=8, column=0, columnspan=3)





mainloop()

