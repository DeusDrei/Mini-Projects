from tkinter import *
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
    global reps
    window.after_cancel(timer)
    status.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0
    check_mark.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        status.config(text="Break", fg=RED, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
    elif reps % 2 == 0:
        count_down(short_break_sec)
        status.config(text="Break", fg=PINK, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
    else:
        count_down(work_sec)
        status.config(text="Work", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = count // 60
    count_sec = count % 60
    canvas.itemconfig(timer_text, text=f"{count_min:02}:{count_sec:02}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        for _ in range(reps//2):
            marks += "✔"
        check_mark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


# Status of Timer
status = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, "bold"))
status.grid(row=0, column=1)

# Tomate Image and Countdown Timer
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(102, 132, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(row=1, column=1)


# Start Timer Button
start_button = Button(text="Start", width=6, bg=YELLOW, command=start_timer)
start_button.grid(row=2, column=0)

# Reset Button
reset_button = Button(text="Reset", width=6, bg=YELLOW, command=reset_timer)
reset_button.grid(row=2, column=2)

# Check mark
check_mark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
check_mark.grid(row=3,column=1)


window.mainloop()