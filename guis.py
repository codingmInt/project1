from tkinter import *
from tkinter import ttk

def enter_pressed():
    print(entry_value.get())
    writing_entry.delete(0, 'end')

root = Tk()
root.title("mINt gUI")
root.geometry('480x360')

entry_value = StringVar(root, value='')

writing_entry = ttk.Entry(root, textvariable=entry_value, width=20)
writing_entry.grid(row=0,columnspan=3)
enter_btn = ttk.Button(root, text='entr', command=enter_pressed)
enter_btn.grid(row=0, column=4)

root.mainloop()