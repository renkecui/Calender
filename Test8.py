import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Checkbox Demo')

agreement = tk.StringVar()


def agreement_changed():
    tk.messagebox.showinfo(title='Result',
                        message=agreement.get())


button1 = ttk.Checkbutton(root,
                text='Done?',
                command=agreement_changed,
                variable=agreement,
                onvalue='Task Completed',
                offvalue='Task Incompolete').pack()
root.mainloop()