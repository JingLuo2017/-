#!/user/bin/env python
# _*_ coding:utf-8 _*_

import sys
from pykeyboard import PyKeyboard
from pymouse import PyMouse
m = PyMouse()
k = PyKeyboard()
# 模拟点击
click = m.click(107, 518, 1, 2)
# click(x,y,button,n)
# x,y 为坐标位置
# button——1表示左键，2表示右键
# n——点击次数，默认1次，2表示双击
now_localtion = m.position()  # 获取当前坐标的位置
# movw = m.move(15,15)  #鼠标移动到(x,y)位置
# click = m.click(x,y)  #移动并且在(x,y)位置点击
print(now_localtion)
# print(movw)

# 保存截图
time.sleep(3)
from PIL import ImageGrab
import time
from datetime import datetime
save_path = 'F:/截屏/'
im = ImageGrab.grab()
dt = datetime.now()
file_name = str(dt.strftime('%Y-%m-%d %H-%M-%S'))
print(save_path + file_name+'.jpg')
im.save(save_path + file_name + '.jpg')

# 发送邮件
import smtplib
from email.mime.multipart import MIMEMultipart
import email.mime.text
from email.header import Header
from email.mime.image import MIMEImage

msg = MIMEMultipart()
msg['from'] = Header('123@qq.com', 'utf-8')
msg['to'] = Header('456@qq.com', 'utf-8')
msg['subject'] = Header('test03', 'utf-8')
content = '''
    你好，
            这是自动发送的邮件。
    致敬！！！
'''
# txt=email.mime.text.MIMEText(content,'plain','utf-8') # 纯文本
txt = email.mime.text.MIMEText(
    '<b>Some <i>HTML</i> text</b> and an image.<br><img src="cid:image1"><br>good!', 'html', 'utf-8')
msg.attach(txt)

with open(save_path + file_name+'.jpg', 'rb') as fp:
    msgImage = MIMEImage(fp.read())

msgImage.add_header('Content-ID', '<image1>')
msg.attach(msgImage)

smtp = smtplib.SMTP('smtp.qq.com', 25)
smtp.set_debuglevel(1)
smtp.starttls()  # 加密传输
smtp.login('123@qq.com', '123')

smtp.sendmail('123@qq.com', '456@qq.com', str(msg))
smtp.quit()


