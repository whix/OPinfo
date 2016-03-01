#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from Tkinter import *
import time
import datetime

url = 'https://one-piece.com/assets/uploads/pagetop/comics/231/0226.png'
while True:
    req = requests.get(url)
    print req.status_code, datetime.datetime.today()
    html = req.content
    info = re.findall(r'/assets/images/common/notfound.png', html)
    if not info:
        break
    time.sleep(30)
t = datetime.datetime.today()
print t
window = Tk()
window.title(u'海贼王出情报啦')
window.mainloop()


