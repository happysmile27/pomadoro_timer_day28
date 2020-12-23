from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer")
    check.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break)
        label.config(text="Break", bg=PINK, fg=RED, font=(FONT_NAME, 35, "normal"))
    if reps % 2 == 0:
        count_down(short_break)
        label.config(text="Break", bg=PINK, fg=RED, font=(FONT_NAME, 35, "normal"))
    else:
        count_down(work_sec)
        label.config(text="Work", bg=PINK, fg=GREEN, font=(FONT_NAME, 35, "normal"))


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global  timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += "\u2714"
        check.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=PINK)


# TODO 1 Import image
canvas = Canvas(width=200, height=224, bg=PINK, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)
# canvas.place(x=150, y=150)


# TODO 2 Label
label = Label(text="Timer", bg=PINK, fg=GREEN, font=(FONT_NAME, 35, "normal"))
label.grid(column=1, row=0)

check = Label(text="", bg=PINK, fg=GREEN, font=(FONT_NAME, 30, "normal"))
check.grid(column=1, row=3)

# TODO 3 Buttons
start = Button(text="Start", highlightthickness=0, command=start_timer, font=(FONT_NAME, 20, "normal"))
start.grid(column=0, row=2)

reset = Button(text="Reset", highlightthickness=0, command=reset_timer, font=(FONT_NAME, 20, "normal"))
reset.grid(column=2, row=2)

window.mainloop()