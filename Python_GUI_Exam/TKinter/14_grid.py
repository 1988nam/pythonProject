from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480") # 가로 * 세로

btn_f16 = Button(root, text="F16")
btn_f17 = Button(root, text="F17")
btn_f18 = Button(root, text="F18")
btn_f19 = Button(root, text="F19")

btn_f16.grid(row=0, column=0)
btn_f17.grid(row=0, column=1)
btn_f18.grid(row=0, column=2)
btn_f19.grid(row=0, column=3)

btn_clear = Button(root, text="clear")
btn_f17 = Button(root, text="F17")
btn_f18 = Button(root, text="F18")
btn_f19 = Button(root, text="F19")

root.mainloop()
