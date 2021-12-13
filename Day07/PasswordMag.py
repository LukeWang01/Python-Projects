import random
import tkinter as tk
import pyperclip

from tkinter import messagebox


# define funs
def add_to_record():
    website = web_entry.get()
    email = email_entry.get()
    password = pd_entry.get()
    # messagebox.showinfo(title="Note", message="Recod Added")
    if website == "" or password == "" or email == "":
        messagebox.showerror(title="Action Needed", message="Please entry the info required")
    else:
        is_ok = messagebox.askokcancel(title="Please confirm the info", message=f"Email:{email}\nPassword:{password}")
        if is_ok:
            with open("data.txt", "a") as date_file:
                date_file.write(f"{website} | {email} | {password}\n")
                web_entry.delete(0)
                pd_entry.delete(0)
        else:
            return


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pd_letter = [random.choice(letters) for _ in range(random.randint(2,10))]
    pd_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    pd_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    temp = pd_symbols + pd_numbers + pd_letter
    random.shuffle(temp)
    password = "".join(temp)
    pd_entry.insert(0, password)
    pyperclip.copy(password)


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

# entry
web_entry = tk.Entry(width=40)
web_entry.grid(row=1, column=1, columnspan=2)
web_entry.focus()
email_entry = tk.Entry(width=40)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(tk.END, "wangzilu9488@gmail.com")
pd_entry = tk.Entry(width=23)
pd_entry.grid(row=3, column=1, columnspan=1)


window.mainloop()
