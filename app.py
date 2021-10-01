from tkinter import *
import pyautogui
from threading import *
import time


class MoveMouse(object):
    def __init__(self):
        self.thread1 = None
        self.stop_threads = Event()

    def run(self):
        while not self.stop_threads.is_set():
            pyautogui.moveRel(100, 0, duration=0.25)
            pyautogui.moveRel(0, 100, duration=0.25)
            pyautogui.moveRel(-100, 0, duration=0.25)
            pyautogui.moveRel(0, -100, duration=0.25)
            sec = None
            try:
                sec = int(number_of_seconds.get())
            except ValueError:
                print('Not an integer')
                self.stop_automation()
            if sec > 10:
                time.sleep(10)
            elif sec < 3:
                time.sleep(3)
            else:
                time.sleep(sec)

    def start_automation(self):
        self.stop_threads.clear()
        self.thread1 = Thread(target=self.run)
        self.thread1.start()

    def stop_automation(self):
        self.stop_threads.set()
        self.thread1.join()
        self.thread1 = None


if __name__ == "__main__" :
 
    gui = Tk()

    global number_of_seconds
    number_of_seconds = StringVar()
    # number_of_seconds = 3
 
    gui.configure(background = "light yellow")
 
    gui.title("Stay Awake")
 
    gui.geometry("400x200")
    gui.resizable(False, False)
 
    enterTask = Label(gui, text = "Delay in seconds", bg = "light green", pady=10, padx=10)
    gap = Label(gui, text = "min 3s and max 10s", bg = "light yellow")

 
    enterTaskField = Entry(gui, textvariable=number_of_seconds)
    enterTaskField.insert(0,"3")

    m = MoveMouse()

 
    Submit = Button(gui, text = "Start", fg = "black", bg = "light green", command = m.start_automation)
    Stop = Button(gui, text = "Stop", fg = "white", bg = "red", command = m.stop_automation)
 
    Exit = Button(gui, text = "Exit", fg = "Black", bg = "Red", command = exit)

    enterTask.pack()
    enterTaskField.pack()
    Submit.pack()
    Stop.pack()
    gap.pack()
    
    gui.mainloop()

    
