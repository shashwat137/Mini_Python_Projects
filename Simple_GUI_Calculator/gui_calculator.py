'''
Python based GUI calculator
Layout -
Where A is AC or clear
    A^/
    *-+
    789
    456
    123
    .0=
'''
import tkinter as tk

def ac():
    '''Will clear the calculator output'''
    global total
    global operation
    global input_value
    total = 0
    operation = ''
    input_value = '0'
    display_lbl['text'] = f"{str(total)}"
    return
def calculate():
    global input_value
    global total
    global operation
    if (operation == '' and input_value == '0') or input_value == '0':
        return
    elif operation == '':
        total = float(input_value)
    elif operation == '^':
        total = total ** float(input_value)
    elif operation == '/':
        total = total / float(input_value)
    elif operation == '*':
        total *= float(input_value)
    elif operation == '+':
        total += float(input_value)
    elif operation == '-':
        total -= float(input_value)
    elif operation == '=':
        if total != 0:
            input_value = '0'
            display_lbl['text'] = f"{str(total)}"
        else:
            total = float(input_value)
            display_lbl['text'] = f"{str(total)}"
        return
    else:
        pass
    operation = ''
    input_value = '0'
    display_lbl['text'] = f"{str(total)}"
    return

def expo():
    '''Will set operation to exponent'''
    global operation
    calculate()
    operation = "^"
    return
def div():
    '''Will set operation to division'''
    global operation
    calculate()
    operation = '/'
    return
def mul():
    '''Will set operation to multiplication'''
    global operation
    calculate()
    operation = '*'
    return
def add():
    '''Will set operation to addition'''
    global operation
    calculate()
    operation = '+'
    return
def sub():
    '''Will set operation to subtraction'''
    global operation
    calculate()
    operation = '-'
    return
def iseq():
    global operation
    if operation != '':
        calculate()
    operation = '='
    calculate()
    return

def _7():
    '''Adds 7 to input'''
    global input_value
    input_value += '7'
    display_lbl['text'] = f"{float(input_value)}"
    return
def _8():
    '''Adds 8 to input'''
    global input_value
    input_value += '8'
    display_lbl['text'] = f"{float(input_value)}"
    return
def _9():
    '''Adds 9 to input'''
    global input_value
    input_value += '9'
    display_lbl['text'] = f"{float(input_value)}"
    return
def _4():
    '''Adds 4 to input'''
    global input_value
    input_value += '4'
    display_lbl['text'] = f"{float(input_value)}"
    return
def _5():
    '''Adds 5 to input'''
    global input_value
    input_value += '5'
    display_lbl['text'] = f"{float(input_value)}"
    return
def _6():
    '''Adds 6 to input'''
    global input_value
    input_value += '6'
    display_lbl['text'] = f"{float(input_value)}"
    return
def _1():
    '''Adds 1 to input'''
    global input_value
    input_value += '1'
    display_lbl['text'] = f"{float(input_value)}"
    return
def _2():
    '''Adds 2 to input'''
    global input_value
    input_value += '2'
    display_lbl['text'] = f"{float(input_value)}"
    return
def _3():
    '''Adds 3 to input'''
    global input_value
    input_value += '3'
    display_lbl['text'] = f"{float(input_value)}"
    return
def _0():
    '''Adds 0 to input'''
    global input_value
    input_value += '0'
    display_lbl['text'] = f"{float(input_value)}"
    return
def _pnt():
    '''Adds point to input'''
    global input_value
    if '.' in input_value:
        return
    else:
        input_value += '.'
        display_lbl['text'] = f"{float(input_value)}"
    return

window = tk.Tk()
window.title("Simple Calculator")
window.rowconfigure(0, minsize=100, weight=1)
window.columnconfigure(0, minsize=80, weight=1)
window.geometry("280x290")

main_frm = tk.Frame(master=window, bg='Black')
main_frm.pack(padx=5,pady=5, expand=True)

display_frm = tk.Frame(master=main_frm, bg='Black')
display_frm.pack(padx=5,pady=5, expand=True)

display_lbl = tk.Label(master=display_frm, text='0', relief=tk.SUNKEN, borderwidth=3, anchor='e', bg='Black', fg='White')
display_lbl.pack(side=tk.RIGHT, padx=5, pady=5, ipadx=30, expand=True)

# Calculator memory units
total = 0   # Will hold the value to be displayed on label
operation = '' # Will keep track of the operation to be performed.
input_value = '0' # Will keep track of new numeric input values. Will be considered until next operation key is pressed.

key_frm = tk.Frame(master=main_frm, bg='Black')
key_frm.pack(padx=5, pady=5)

btn_ac = tk.Button(master=key_frm, text='Clear', command=ac, bg='Black', fg='White')
btn_ac.grid(row=0, column=0, padx=5, pady=5)
btn_power = tk.Button(master=key_frm, text="^", command=expo, bg='Black', fg='White')
btn_power.grid(row=0, column=1, ipadx=11, padx=5, pady=5)
btn_div = tk.Button(master=key_frm, text='/', command=div, bg='Black', fg='White')
btn_div.grid(row=0, column=2, ipadx=11, padx=5, pady=5)
btn_mul = tk.Button(master=key_frm, text="*", command=mul, bg='Black', fg='White')
btn_mul.grid(row=1, column=0, ipadx=10, padx=5, pady=5)
btn_sub = tk.Button(master=key_frm, text="-", command=sub, bg='Black', fg='White')
btn_sub.grid(row=1, column=1, ipadx=11, padx=5, pady=5)
btn_add = tk.Button(master=key_frm, text="+", command=add, bg='Black', fg='White')
btn_add.grid(row=1, column=2, ipadx=11, padx=5, pady=5)
btn_7 = tk.Button(master=key_frm, text="7", command=_7, bg='Black', fg='White')
btn_7.grid(row=2, column=0, ipadx=10, padx=5, pady=5)
btn_8 = tk.Button(master=key_frm, text="8", command=_8, bg='Black', fg='White')
btn_8.grid(row=2, column=1, ipadx=11, padx=5, pady=5)
btn_9 = tk.Button(master=key_frm, text="9", command=_9, bg='Black', fg='White')
btn_9.grid(row=2, column=2, ipadx=11, padx=5, pady=5)
btn_4 = tk.Button(master=key_frm, text="4", command=_4, bg='Black', fg='White')
btn_4.grid(row=3, column=0, ipadx=10, padx=5, pady=5)
btn_5 = tk.Button(master=key_frm, text="5", command=_5, bg='Black', fg='White')
btn_5.grid(row=3, column=1, ipadx=11, padx=5, pady=5)
btn_6 = tk.Button(master=key_frm, text="6", command=_6, bg='Black', fg='White')
btn_6.grid(row=3, column=2, ipadx=11, padx=5, pady=5)
btn_1 = tk.Button(master=key_frm, text="1", command=_1, bg='Black', fg='White')
btn_1.grid(row=4, column=0, ipadx=10, padx=5, pady=5)
btn_2 = tk.Button(master=key_frm, text="2", command=_2, bg='Black', fg='White')
btn_2.grid(row=4, column=1, ipadx=11, padx=5, pady=5)
btn_3 = tk.Button(master=key_frm, text="3", command=_3, bg='Black', fg='White')
btn_3.grid(row=4, column=2, ipadx=11, padx=5, pady=5)
btn_pnt = tk.Button(master=key_frm, text=".", command=_pnt, bg='Black', fg='White')
btn_pnt.grid(row=5, column=0, ipadx=11, padx=5, pady=5)
btn_0 = tk.Button(master=key_frm, text="0", command=_0, bg='Black', fg='White')
btn_0.grid(row=5, column=1, ipadx=11, padx=5, pady=5)
btn_eq = tk.Button(master=key_frm, text="=", command=iseq, bg='Black', fg='White')
btn_eq.grid(row=5, column=2, ipadx=11, padx=5, pady=5)

window.mainloop()
