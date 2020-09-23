import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():
    ''' Open a file for editing.'''
    # Displays an open file dialog and stores selected filepath.
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt"),("All Files", "*.*")])

    # The function does nothing and returns if the dialog is closed or canceled. Filepath will be None in this case.
    if not filepath:
        return

    # Clears conntents of text box
    txt_edit.delete("1.0",tk.END)

    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Simple Text Editor - {filepath}")
    return

def save_file():
    '''Save Current file as a new file'''
    # Displays an save file dialog and stores selected filepath.
    filepath = asksaveasfilename(filetypes=[("Text Files", "*.txt"),("All Files", "*.*")])

    # The function does nothing and returns if the dialog is closed or canceled. Filepath will be None in this case.
    if not filepath:
        return

    with open(filepath, 'w') as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"Simple Text Editor - {filepath}")
    return

window = tk.Tk()
window.title("Simple Text Editor")

window.rowconfigure(0, minsize=700, weight=1)
window.columnconfigure(1, minsize=700, weight=1)

txt_edit = tk.Text(master=window)
side_frm = tk.Frame(master=window)
btn_open = tk.Button(master=side_frm, text="Open", command=open_file)
btn_save = tk.Button(master=side_frm, text='Save As...', command=save_file)
btn_open.grid(row=0, column=0, sticky='ew', padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky='ew', padx=5)
side_frm.grid(row=0, column=0, sticky='ns')
txt_edit.grid(row=0, column=1, sticky='nsew')

window.mainloop()
