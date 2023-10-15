import time
import tkinter as tk

def display_text():
    string = entry.get()
    label.configure(text=string)

def countdown(mtime):
    for x in range(mtime, 0, -1):
        seconds = x % 60
        minutes = (x // 60) % 60
        hours = x // 3600
        time_string = f"{hours:02}:{minutes:02}:{seconds:02}"
        label.configure(text=time_string)
        win.update()  # Update the tkinter window
        time.sleep(1)
    label.configure(text="Time's UP!")

win = tk.Tk()
win.geometry("750x250")

label = tk.Label(win, font=("Courier 22 bold"))
label.pack()

entry = tk.Entry(win, width=40)
entry.pack()

start_button = tk.Button(win, text="Start Countdown", command=lambda: countdown(int(entry.get())))
start_button.pack()
win.mainloop()
