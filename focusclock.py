import time
import tkinter as tk

# 创建一个新的窗口
root = tk.Tk()
root.title('专注时钟')

# 设置窗口大小
root.geometry('300x150')

# 标签，用于显示倒计时剩余时间
time_left = tk.StringVar()
time_left.set('25:00')

# 定义函数，用于更新倒计时
def countdown():
    # 从 time_left 变量获取剩余秒数
    minutes, seconds = map(int, time_left.get().split(':'))
    remaining_seconds = minutes * 60 + seconds - 1
    
    # 将剩余秒数格式化为字符串
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    time_left.set(f'{minutes:02}:{seconds:02}')
    
    # 如果倒计时未结束，更新时间并计划下一次更新
    if remaining_seconds > 0:
        root.after(1000, countdown)
    # 如果倒计时结束，显示“时间到”信息
    else:
        time_left.set('时间到！')

# 创建标签，并将其绑定到 time_left 变量
timer_label = tk.Label(root, textvariable=time_left, font=('Helvetica', 36))
timer_label.pack(pady=20)

# 创建“开始”按钮
start_button = tk.Button(root, text='开始', command=countdown)
start_button.pack()

# 运行窗口循环
root.mainloop()
