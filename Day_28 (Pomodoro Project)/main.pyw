import tkinter as tk
import math
import winsound as ws
"""MAKING A TOMATO TIMER!!!"""
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
    global timer
    global reps
    window.after_cancel(timer)
    timer_label.config(text="Timer",fg=GREEN)
    canvas.itemconfig(time_text,text="00:00")
    reps = 0
    start_button.config(state="normal")
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    start_button.config(state="disabled")
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps += 1
    if reps % 8 == 0 and reps != 0:
        count_down(long_break_sec)
        timer_label.config(text="Break",fg=RED)
    elif reps % 2 == 1:
        count_down(work_sec)
        timer_label.config(text="Work",fg=GREEN)
    else:
        count_down(short_break_sec)
        timer_label.config(text="Break",fg=PINK)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:                  # This process does work to fix an issue of time appearing as 5:0 by using
        count_sec = f"0{count_sec}"     # dynamic typing. Here, I change count_sec from int to string.
    canvas.itemconfig(time_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000,count_down,count-1)
    else:
        # window.bell()     Bell doesn't seem to work.
        window.lift()
        window.attributes('-topmost',True)
        window.attributes('-topmost',False)
        if reps == 8:
            reps = 0
        start_timer()
        checks.config(text="✔"*math.floor(reps/2))

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)   #YELLOW only changes the color of the window here. We also need to change
                                            #the Canvas color!!
#CREATES TIMER LABEL
timer_label = tk.Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,40,"bold"))
timer_label.grid(column=1,row=0)
#CREATES CHECKMARK LABEL
checks = tk.Label(fg=GREEN,bg=YELLOW,font=(FONT_NAME,20,"bold"))
checks.grid(column=1,row=3)
#CREATES START BUTTON
start_button = tk.Button(text="Start",command=start_timer)
start_button.grid(column=0,row=2)
#CREATES RESET BUTTON
reset_button = tk.Button(text="Reset",command=reset_timer)
reset_button.grid(column=2,row=2)

#CREATES CANVAS WITH TOMATO PICTURE
canvas = tk.Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)    #highlightthickness needed to remove
pomodoro = tk.PhotoImage(file="tomato.png")                                 #white canvas line around pic
canvas.create_image(100,112,image=pomodoro)
time_text = canvas.create_text(102,126,text="00:00", fill="white",font=(FONT_NAME,28,"bold"))
canvas.grid(column=1,row=1)

window.mainloop()