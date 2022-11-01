import tkinter as tk
from tkinter import *
from tkinter import messagebox


app = tk.Tk()
app.geometry("800x500")
app.title("WeaDEr APP")

label = tk.Label(app, text='my app would be great', font=('Times New Roman', 20))
label.pack()

my_entry = tk.Entry(app, font=('Times New Roman', 16))
my_entry.pack()

button = tk.Button(app, text='click me!')
button.pack(padx=10, pady=14 )





app.mainloop()


