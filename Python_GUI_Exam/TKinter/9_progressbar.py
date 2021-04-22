import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480") # 가로 * 세로

#progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")
progressbar.start(10) # 10 ms 마다 움직임
progressbar.pack()

def btncmd():
    progressbar.stop()


btn = Button(root, text="선택", command= btncmd)
btn.pack()

root.mainloop()
