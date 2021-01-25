#开源时去除了一些东西！
#开源时去除了一些东西！
#开源时去除了一些东西！
#开源时去除了一些东西！
#开源时去除了一些东西！
#开源时去除了一些东西！
#开源时去除了一些东西！
#开源时去除了一些东西！
#开源时去除了一些东西！
#开源时去除了一些东西！
#开源时去除了一些东西！
#开源时去除了一些东西！
#开源时去除了一些东西！
#开源时去除了一些东西！
#开源时去除了一些东西！
#开源时去除了一些东西！
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
import telnetlib#测试端口
xin=25565
cn=25575
try:
    telnetlib.Telnet('43.248.188.149', port='{}'.format(xin), timeout=20)
except:
    reportxin='关闭'
else:
    reportxin='开启'
try:
    telnetlib.Telnet('43.248.188.149', port='{}'.format(cn), timeout=20)
except:
    reportcn='关闭'
else:
    reportcn='开启'
def next():
    print('日志:正在跳转中')
    windowtwo=tk.Tk()
    windowtwo.title('Amphetamine')
    windowtwo.geometry('1200x500')
    window.destroy()
    bluebg=tk.Canvas(windowtwo, bg='#B0C4DE', height=150, width=10000)
    bluebg.place(x=-100, y=-100)
    print("日志:bluebg已放置")
    graybg=tk.Canvas(windowtwo, bg='#DCDCDC', height=10000, width=400)
    graybg.place(x=-100, y=-100)
    print("日志:graybg已放置")
    showxin=tk.Label(windowtwo,text='2B2T.XIN  {}'.format(reportxin),font=('微软雅黑',10),width=15,height=1)
    showcn=tk.Label(windowtwo,text='CN2B2T.ORG  {}'.format(reportcn),font=('微软雅黑',10),width=15,height=1)
    showxin.place(x=0, y=5)
    showcn.place(x=0,y=30)
print("日志:跳转函数已就绪")
nextpage=tk.Button(window, text='登陆成功！下一步', font=('微软雅黑',12),width=15, height=1, command=next)
#开源时去除了一些东西！
#开源时去除了一些东西！
#开源时去除了一些东西！
#开源时去除了一些东西！
#开源时去除了一些东西！
#开源时去除了一些东西！
#开源时去除了一些东西！
#开源时去除了一些东西！
#开源时去除了一些东西！
#开源时去除了一些东西！
#开源时去除了一些东西！
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