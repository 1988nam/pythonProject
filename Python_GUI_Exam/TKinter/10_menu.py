from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480") # 가로 * 세로

def create_new_file():
    print('새 파일을 만듭니다')

menu = Menu(root)

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New File", command=create_new_file)
menu_file.add_command(label='New window')
menu_file.add_separator()
menu_file.add_command(label="open file...")
menu_file.add_separator()
menu_file.add_command(label="Save ALL", state="disable")
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)


menu.add_cascade(label="File", menu=menu_file)
menu.add_cascade(label="Edit")

menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="python")
menu_lang.add_radiobutton(label="Java")
menu_lang.add_radiobutton(label="C++")

menu.add_cascade(label="Language", menu=menu_lang)

menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="Show Minimap")
menu.add_cascade(label="View", menu=menu_view)

root.config(menu=menu)
root.mainloop()
