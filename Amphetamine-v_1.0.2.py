adition="1.0.2"
print('日志:正在加载组件中,请务必耐心等待！...')
import tkinter as tk#GUI
print("日志:tkinter已就绪")
import tkinter.messagebox#弹窗
print("日志:tkinter.messagebox已就绪")
#import datetime as dt#时间
#print("日志:datetime已就绪")
#import socket#本机信息
#print("日志:socket已就绪")
#import time#砸瓦鲁多！
#print("日志:time已就绪,砸瓦鲁多！")
import requests
#backdoor?
ip=(requests.get('http://ifconfig.me/ip', timeout=1).text.strip())
window=tk.Tk()
window.title('Amphetamine')
window.geometry('1200x500')
print("日志:窗口已生成")
#窗口基本信息 标题|分辨率
txt=tk.Label(window,text='登陆您的LCC账号',font=('微软雅黑',20),width=15,height=1)
txt.place(x=480, y=50)
print("日志:总标题已放置")
#总标题
anew=tk.Label(window,text='暂不支持注册新用户',font=('微软雅黑',10),width=15,height=1)
anew.place(x=680, y=250)
print("日志:注册信息已放置")
#暂不支持注册
entryone=tk.Entry(window, show="●", font=('微软雅黑', 14))
entrytwo=tk.Entry(window, show=None, font=('微软雅黑', 14))
entrytwo.place(x=500, y=150)
entryone.place(x=500, y=200)
#账号密码登陆
print('日志:账号密码等待接收')
entrytwotip=tk.Label(window,text='账号:',font=('微软雅黑',12),width=3,height=1)
entryonetip=tk.Label(window,text='密码:',font=('微软雅黑',12),width=3,height=1)
entrytwotip.place(x=450, y=150)
entryonetip.place(x=450, y=200)
#账号密码定位提示
print('日志:所有登陆提示已放置')
v=tk.Label(window,text='当前版本:{}'.format(adition),font=('微软雅黑',5),width=15,height=1)
v.place(x=1130, y=485)
a=0
def secret():
    if var1.get()==1:
        entryone=tk.Entry(window, show=None, font=('微软雅黑', 14))
        entryone.place(x=500, y=200)
    else:
        entryone=tk.Entry(window, show="●", font=('微软雅黑', 14))
        entryone.place(x=500, y=200)
var1=tk.IntVar()         
radiobutton=tk.Checkbutton(window, text='密码可视化', variable=var1,onvalue=1, offvalue=0, command=secret)
radiobutton.place(x=450, y=250)
designer=(tkinter.messagebox.askyesno(title='Amphetamine的开发信息',message='Amphetamine由7ÐЦΙÏ_开发！是否了解？\n"是"则开始使用,"否"则退出程序！'))
print("日志:开发信息已放置")
if designer==True:
    print("日志:开发信息结束")
    pass
else:
    print("程序结束")
    quit()
#开发信息
#hostname=socket.gethostname()
#ip=socket.gethostbyname(hostname)
def next():
    print('日志:正在跳转中')
    windowtwo=tk.Tk()
    windowtwo.title('Amphetamine')
    windowtwo.geometry('1200x500')
    window.destroy()
print("日志:跳转函数已就绪")
nextpage=tk.Button(window, text='登陆成功！下一步', font=('微软雅黑',12),width=15, height=1, command=next)
def login():
    varone=entrytwo.get()#接收账号  
    vartwo=entryone.get()#接收密码
    if varone=='':
        tkinter.messagebox.showerror(title='Amphetamine', message='账号或密码为空!')
        print("日志:登陆失败")
    elif vartwo=='':
        tkinter.messagebox.showerror(title='Amphetamine', message='账号或密码为空!')
        print("日志:登陆失败")
    elif varone=='lccontop' and vartwo=='lccontop':
        nextpage.place(x=535, y=300)
        print("日志:登陆成功")
    elif varone=='7dull_' and vartwo=='953007962':  
        nextpage.place(x=535, y=300) 
        print("日志:登陆成功")
    elif varone=='FPDADA' and vartwo=='wyf2253921':  
        nextpage.place(x=535, y=300) 
        print("日志:登陆成功")
    else: 
        tkinter.messagebox.showerror(title='Amphetamine', message='账号或密码错误!请勿采用字典破解！\n您的ip为:{}已定位，过多次的尝试可能会进行封禁处理！'.format(ip))#登陆失败
        print("日志:登陆失败")
print("日志:登陆函数已就绪")        
def fix():
    tkinter.messagebox.showinfo(title='Amphetamine', message='修复完毕！')
    print("日志:输入修复完成")
print("日志:修复函数已就绪")    
fixing=tk.Button(window, text='无法输入?点击此处修复', font=('微软雅黑',12),width=20, height=1, command=fix)
fixing.place(x=735, y=145)
#解决无法输入等问题
print("日志:修复按钮已就绪")
logining=tk.Button(window, text='登陆',font=('微软雅黑',12),width=10,height=1,command=login)
logining.place(x=550, y=250)
#登陆按钮
print("日志:登录按钮已就绪")
window.mainloop()