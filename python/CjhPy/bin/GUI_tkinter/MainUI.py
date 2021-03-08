
import tkinter
import tkinter as tk  # 使用Tkinter前需要先导入
import tkinter.messagebox
import pickle


def mainWindow():
    window = tkinter.Tk()
    window.title("this is a window")
    #设置窗口大小
    window.geometry('400x500')
    tkinter.Label(window, text='Welcome to Create', font=('Arial', 14), width=30, height=2).pack()

    #第5步，用户信息
    tk.Label(window, text='商品名称：', font=('Arial', 14)).place(x=10, y=100)
    tk.Label(window, text='库存量：', font=('Arial', 14)).place(x=10, y=120)
    tk.Label(window, text='起拍价：', font=('Arial', 14)).place(x=10, y=140)
    tk.Label(window, text='商品起拍价：', font=('Arial', 14)).place(x=10, y=160)
    tk.Label(window, text='保证金金额：', font=('Arial', 14)).place(x=10, y=180)
    tk.Label(window, text='最小加价幅度：', font=('Arial', 14)).place(x=10, y=200)
    tk.Label(window, text='延时结束：', font=('Arial', 14)).place(x=10, y=220)
    tk.Label(window, text='循环周期：', font=('Arial', 14)).place(x=10, y=240)
    tk.Label(window, text='开始时间：', font=('Arial', 14)).place(x=10, y=260)
    tk.Label(window, text='结束时间：', font=('Arial', 14)).place(x=10, y=280)
    tk.Button(window, text='创建商品', )
    window.mainloop()

if __name__ == '__main__':
    mainWindow()