import tkinter as tk
from tkinter import END

window = tk.Tk()
window.title("My first GUI Python")
window.minsize(500, 300)

# label
label = tk.Label(text="I am a label", font=("Arial", 24))
label.place(x=100, y=190)
label["text"] = "Luke"
label.config(text=" Lu k e")

# button


def button_clicked():
    print("clicked luke")
    new_text = input_box.get()
    label["text"] = new_text


button = tk.Button(text="click me", command=button_clicked)
button.grid(column=5, row=1)
button2 = tk.Button(text="2nd one")
button2.grid(column=2, row=1)
button2.config(padx=5, pady=5)

# entry
input_box = tk.Entry(width=10)
a = input_box.get()
input_box.insert(END, string="type here")
input_box.focus()
input_box.grid(column=1, row=2)


window.mainloop()
