import tkinter as tk

def convert():
    try:
        lbl_value['text'] = f"{float( ( float(ent.get()) - 32) * 5 / 9):.4f} \N{DEGREE CELSIUS}"
    except:
        lbl_value['text'] = f"****** \N{DEGREE CELSIUS}"
    return


window = tk.Tk()
window.title("Temperature Converter")
window.rowconfigure([0,1,2], weight=1, minsize=30)
window.columnconfigure([0,1,2], weight=1, minsize=25)

frm = tk.Frame(master=window)
frm.grid(row=1,column = 1)

ent = tk.Entry(master=frm, width=10)
ent.grid(row=0, column=0, sticky='e')

lbl_f = tk.Label(master=frm,text=f"\N{DEGREE FAHRENHEIT}")
lbl_f.grid(row=0, column=1, sticky='w', ipady=5)

btn_1 = tk.Button(master=frm,text=f"\N{RIGHTWARDS BLACK ARROW}", command=convert)
btn_1.grid(row=0, column=2, padx=15)

lbl_value = tk.Label(master=frm, text=f"\N{DEGREE CELSIUS}")
lbl_value.grid(row=0, column=3,sticky='e',ipady=5)



window.mainloop()
