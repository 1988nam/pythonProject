import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480") # 가로 * 세로

values = [str(i) + "일" for i in range(1,32)]
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("카드결제일")

readonly_combobox = ttk.Combobox(root, height=5, values=values, state="readonly")
readonly_combobox.pack()
readonly_combobox.current(0)
readonly_combobox.set("카드결제일")

def btncmd():
    print(combobox.get())
    print(readonly_combobox.get())

btn = Button(root, text="선택", command= btncmd)
btn.pack()

root.mainloop()
