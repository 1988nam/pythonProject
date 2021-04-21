from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480") # 가로 * 세로

listbox = Listbox(root, selectmode="extended", height=0)
listbox.insert(0,"사과")
listbox.insert(1,"딸기")
listbox.insert(2,"바나나")
listbox.insert(END,"수박")
listbox.insert(END,"포도")
listbox.pack()

def btncmd():
    #listbox.delete(0)

    #print(listbox.size())

    print(listbox.get(0,2))

    print(listbox.curselection())

btn = Button(root, text="클릭", command= btncmd)
btn.pack()

root.mainloop()
