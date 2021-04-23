import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480") # 가로 * 세로

def info():
    msgbox.showinfo("알림","정상적으로 예매 완료")

def warn():
    msgbox.showwarning("경고","해당 좌석은 매진")

def error():
    msgbox.showerror("에러","결제 오류 발생")

def okcancle():
    msgbox.askokcancel("확인 / 취소","해당 좌석은 유아 동반 좌석이다")

def retrycancle():
    msgbox.askretrycancel("재시도 / 취소","일시적 오류, 다시 시도 하겠습니까??")

def yesno():
    msgbox.askyesno("예 / 아니오","해당 좌석 역 방향입니다 예매 하겠습니까?")

def yesnocancle():
    response = msgbox.askyesnocancel(title=None, message="삐리리")
    print(response)
    if response == 1:
        print('예')
    elif response == 0:
        print('아니오')
    else:
        print('취소')

Button(root, command=info, text="알림").pack()
Button(root, command=warn, text="경고").pack()
Button(root, command=error, text="에러").pack()

Button(root, command=okcancle, text="확인 취소").pack()
Button(root, command=retrycancle, text="재시도 취소").pack()
Button(root, command=yesno, text="예 아니오").pack()
Button(root, command=yesnocancle, text="예 아니오 취소").pack()

root.mainloop()
