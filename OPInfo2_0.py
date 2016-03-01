#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import requests
from Tkinter import *
import datetime
import tkMessageBox
import threading
from Queue import Queue


def working():
    url = var.get()
    is_right_url = re.match(r'https://one-piece.com/assets/uploads/pagetop/comics', url)
    if not is_right_url:
        q.put((tkMessageBox.showinfo, ('Message', u'链接错误，请检查！'), {}))
        return
    t.insert(1.0, url+'\n')
    t.update()
    try:
        while True:
            req = requests.get(url, timeout=10)
            now = datetime.datetime.now()
            now = now.strftime("%Y-%m-%d %H:%M:%S")
            if req.status_code != 200:
                temp1 = u'访问网址出错！\nstatus_code:%s' % req.status_code
                q.put((tkMessageBox.showinfo, ('Message', temp1), {}))
            else:
                t.insert(END, 'working，%s\n' % now)
                t.update()
            html = req.content
            info = re.findall(r'/assets/images/common/notfound.png', html)
            if not info:
                temp2 = u'海贼王出情报啦！\n%s' % now
                q.put((tkMessageBox.showinfo, ('Message', temp2), {}))
                break
            time.sleep(30)
    except Exception, e:
        t.insert(END, e)
        t.insert(END, u'\n程序停止！')
        t.update()


def new_thread():
    global flag
    if flag:
        flag = False
        thread_ob = threading.Thread(target=working, name='working_func')
        thread_ob.setDaemon(True)
        thread_ob.start()


def my_tkloop():
    try:
        while True:
            msg_info, a, k = q.get_nowait()
            print msg_info, a, k
            msg_info(*a, **k)

    except Exception:
        pass

    window.after(100, my_tkloop)


q = Queue()

# thread flag
flag = True

window = Tk()
window.title(u'Window')

frame = Frame(window)
frame.pack()

Label(frame, text=u'输入网址：').pack(side=LEFT)

var = StringVar()
Entry(frame, width=50, textvariable=var).pack(side=LEFT)

Button(frame, text=u'运行', width=5, command=new_thread).pack(side=LEFT)
Button(frame, text=u'退出', command=window.quit).pack(side=RIGHT)

scroll = Scrollbar(window, orient=VERTICAL)
scroll.pack(side=RIGHT, fill=Y)
t = Text(window, width=78, yscrollcommand=scroll.set)
scroll['command'] = t.yview()
t.pack()

my_tkloop()
window.mainloop()