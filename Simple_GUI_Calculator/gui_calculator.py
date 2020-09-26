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

def all_operations(key):
    '''
    Will consider all operations
    Takes the operation as a string in input.
    '''
    global operation
    calculate()
    operation = key
    if operation == '=':
        calculate()
    return

def numpad(num):
    '''
    Write any value from the numpad.
    Takes the numpad value as input.
    '''
    num = str(num)
    global input_value
    if num == '.' and '.' in input_value:
        return
    else:
        input_value += num
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
btn_power = tk.Button(master=key_frm, text="^", command=lambda:all_operations('^'), bg='Black', fg='White')
btn_power.grid(row=0, column=1, ipadx=11, padx=5, pady=5)
btn_div = tk.Button(master=key_frm, text='/', command=lambda:all_operations('/'), bg='Black', fg='White')
btn_div.grid(row=0, column=2, ipadx=11, padx=5, pady=5)
btn_mul = tk.Button(master=key_frm, text="*", command=lambda:all_operations('*'), bg='Black', fg='White')
btn_mul.grid(row=1, column=0, ipadx=10, padx=5, pady=5)
btn_sub = tk.Button(master=key_frm, text="-", command=lambda:all_operations('-'), bg='Black', fg='White')
btn_sub.grid(row=1, column=1, ipadx=11, padx=5, pady=5)
btn_add = tk.Button(master=key_frm, text="+", command=lambda:all_operations('+'), bg='Black', fg='White')
btn_add.grid(row=1, column=2, ipadx=11, padx=5, pady=5)
btn_7 = tk.Button(master=key_frm, text="7", command=lambda:numpad(7), bg='Black', fg='White')
btn_7.grid(row=2, column=0, ipadx=10, padx=5, pady=5)
btn_8 = tk.Button(master=key_frm, text="8", command=lambda:numpad(8), bg='Black', fg='White')
btn_8.grid(row=2, column=1, ipadx=11, padx=5, pady=5)
btn_9 = tk.Button(master=key_frm, text="9", command=lambda:numpad(9), bg='Black', fg='White')
btn_9.grid(row=2, column=2, ipadx=11, padx=5, pady=5)
btn_4 = tk.Button(master=key_frm, text="4", command=lambda:numpad(4), bg='Black', fg='White')
btn_4.grid(row=3, column=0, ipadx=10, padx=5, pady=5)
btn_5 = tk.Button(master=key_frm, text="5", command=lambda:numpad(5), bg='Black', fg='White')
btn_5.grid(row=3, column=1, ipadx=11, padx=5, pady=5)
btn_6 = tk.Button(master=key_frm, text="6", command=lambda:numpad(6), bg='Black', fg='White')
btn_6.grid(row=3, column=2, ipadx=11, padx=5, pady=5)
btn_1 = tk.Button(master=key_frm, text="1", command=lambda:numpad(1), bg='Black', fg='White')
btn_1.grid(row=4, column=0, ipadx=10, padx=5, pady=5)
btn_2 = tk.Button(master=key_frm, text="2", command=lambda:numpad(2), bg='Black', fg='White')
btn_2.grid(row=4, column=1, ipadx=11, padx=5, pady=5)
btn_3 = tk.Button(master=key_frm, text="3", command=lambda:numpad(3), bg='Black', fg='White')
btn_3.grid(row=4, column=2, ipadx=11, padx=5, pady=5)
btn_pnt = tk.Button(master=key_frm, text=".", command=lambda:numpad('.'), bg='Black', fg='White')
btn_pnt.grid(row=5, column=0, ipadx=11, padx=5, pady=5)
btn_0 = tk.Button(master=key_frm, text="0", command=lambda:numpad(0), bg='Black', fg='White')
btn_0.grid(row=5, column=1, ipadx=11, padx=5, pady=5)
btn_eq = tk.Button(master=key_frm, text="=", command=lambda:all_operations('='), bg='Black', fg='White')
btn_eq.grid(row=5, column=2, ipadx=11, padx=5, pady=5)

window.mainloop()
