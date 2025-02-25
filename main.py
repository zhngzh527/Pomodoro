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
    global reps
    window.after_cancel(timer)
    label.config(text="Timer")
    check_mark.config(text="")
    canvas.itemconfig(timer_text,text="00:00")
    reps = 0
    start_button.config(state="active")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    start_button.config(state="disabled")
    work = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break)
        label.config(fg=RED,text="Break",bg=YELLOW,font=(FONT_NAME,40,"bold"))
    elif reps % 2 == 0:
        count_down(short_break)
        label.config(fg=PINK,text="Break",bg=YELLOW,font=(FONT_NAME,40,"bold"))
    else:
        count_down(work)
        label.config(fg=GREEN,text="Work",bg=YELLOW,font=(FONT_NAME,40,"bold"))
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down,count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for i in range(work_sessions):
            marks += "✔"
        check_mark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window =Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

label = Label()
label.config(fg=GREEN,text="Timer",bg=YELLOW,font=(FONT_NAME,40,"bold"))
label.grid(column=2,row=1)

canvas = Canvas(width=200,height=224, bg=YELLOW,highlightthickness=0)
tomato_pic = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_pic)
timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35, "bold"))
canvas.grid(column=2,row=2)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=1, row=3)
reset_button = Button(text="Reset",command=reset_timer)
reset_button.grid(column=3,row=3)

check_mark = Label(fg=GREEN,bg=YELLOW,font=(FONT_NAME,20,"bold"))
check_mark.grid(column=2,row=4,)

window.mainloop()