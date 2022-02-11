import tkinter as tk
from tkinter import END


def convert_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    result_label.config(text=f"{km}")


window = tk.Tk()
window.title("converter")
window.config(padx=20, pady=20)

miles_input = tk.Entry(width=8)
miles_input.grid(column=1, row=0)
miles_input.insert(END, "input here")
miles_input.focus()

miles_label = tk.Label(text="miles")
miles_label.grid(column=2, row=0)

is_equal_label = tk.Label(text="is equal to ")
is_equal_label.grid(column=0, row=1)

km_label = tk.Label(text="KM")
km_label.grid(column=2, row=1)

calculate = tk.Button(text="Calculate", command=convert_km)
calculate.grid(column=1, row=2)

result_label = tk.Label()
result_label.grid(column=1, row=1)


window.mainloop()

