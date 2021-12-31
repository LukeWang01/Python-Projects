import random
import tkinter as tk
import pyperclip
import json
from tkinter import messagebox, END


# define funs
def add_to_record():
    website = web_entry.get()
    email = email_entry.get()
    password = pd_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    # messagebox.showinfo(title="Note", message="Recod Added")
    if website == "" or password == "" or email == "":
        messagebox.showerror(title="Action Needed", message="Please entry the info required")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            web_entry.delete(0, END)
            pd_entry.delete(0, END)
            messagebox.showinfo(title="Nice", message="Record added")


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    pd_letter = [random.choice(letters) for _ in range(random.randint(2, 10))]
    pd_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    pd_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    temp = pd_symbols + pd_numbers + pd_letter
    random.shuffle(temp)
    password = "".join(temp)
    pd_entry.insert(0, password)
    pyperclip.copy(password)


def search_record():
    website = web_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data file found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email:{email}\nPassword:{password}")
            pyperclip.copy(password)
        else:
            messagebox.showinfo(title="Search Result", message=f"No reocrd for{website} found")


window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tk.Canvas(width=200, height=200, highlightthickness=0)
img = tk.PhotoImage(file="Lock_logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

# creat label
website_label = tk.Label(text="Website:")
website_label.grid(row=1, column=0, columnspan=1)

email_label = tk.Label(text="Email/Username:")
email_label.grid(row=2, column=0, columnspan=1)

password_label = tk.Label(text="Password:")
password_label.grid(row=3, column=0, columnspan=1)

# creat button
gen_pd_button = tk.Button(text="Generate Password", command=generate_password)
gen_pd_button.grid(row=3, column=2)
add_button = tk.Button(text="Add To Record", width=35, command=add_to_record)
add_button.grid(row=4, column=1, columnspan=2)
search_button = tk.Button(text="Search", width=13, command=search_record)
search_button.grid(row=1, column=2)

# entry
web_entry = tk.Entry(width=23)
web_entry.grid(row=1, column=1, columnspan=1)
web_entry.focus()
email_entry = tk.Entry(width=40)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(tk.END, "wangzilu9488@gmail.com")
pd_entry = tk.Entry(width=23)
pd_entry.grid(row=3, column=1, columnspan=1)

window.mainloop()
