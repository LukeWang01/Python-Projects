import tkinter as tk
from tkinter import messagebox
import beepy

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 30
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
not_next_round = True


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    # time_text is a canvas object, using canvas.itemconfig()
    canvas.itemconfig(time_text, text="00:00")
    title_label.config(text="Timer")
    checkmark.config(text="")
    global reps
    reps = 0


def next_round():
    if reps == 0:
        messagebox.showinfo(title="Ops", message="Timer not started, please start the timer first")
    else:
        global not_next_round
        not_next_round = False

        window.after_cancel(timer)
        start_timer()
        check_mark_list = ""
        for i in range(reps // 2):
            check_mark_list += "✅"
            checkmark.config(text=check_mark_list)

        not_next_round = True


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    global not_next_round
    # Just in case click this double twice
    if reps > 0 and not_next_round:
        messagebox.showinfo(title="Ops", message="Already started")
        # print("already started")
        return

    reps += 1
    work_sec = int(WORK_MIN * 60)
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    # count_down(work_sec)
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Long Break", fg=RED)
        beepy.beep(sound="success")

    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Short Break", fg=PINK)
        beepy.beep(sound="ping")

    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)
        if  reps != 1:
            beepy.beep(sound="ping")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    mins = count // 60
    second = count % 60

    if second < 10:
        second = f"0{second}"

    canvas.itemconfig(time_text, text=f"{mins}:{second}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
        # print("run")
    else:
        start_timer()
        check_mark_list = ""
        for i in range(reps // 2):
            check_mark_list += "✅"
            checkmark.config(text=check_mark_list)


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW, width=350, height=224)

title_label = tk.Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50), bg=YELLOW)
title_label.grid(column=1, row=0)

canvas = tk.Canvas(width=350, height=224, bg=YELLOW, highlightthickness=0)
img = tk.PhotoImage(file="tomato.png")
canvas.create_image(175, 112, image=img)
time_text = canvas.create_text(175, 112, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

empty_label1 = tk.Label(text="", bg=YELLOW)
empty_label1.grid(column=1, row=2)

empty_label2 = tk.Label(text="", bg=YELLOW)
empty_label2.grid(column=1, row=4)

start_button = tk.Button(text="Start", highlightthickness=0, bg=YELLOW, command=start_timer)
start_button.grid(column=0, row=3)

reset_button = tk.Button(text="Reset", highlightthickness=0, bg=YELLOW, command=reset_timer)
reset_button.grid(column=2, row=3)

next_round_button = tk.Button(text="Next Round", highlightthickness=0, bg=YELLOW, command=next_round)
next_round_button.grid(column=1, row=3)

checkmark = tk.Label(fg=GREEN, bg=YELLOW)
checkmark.grid(column=1, row=5)

window.mainloop()
