#-*- coding:utf-8 -*-
import itchat
import datetime
import time

itchat.auto_login(hotReload = True)
target = itchat.search_chatrooms(userName = '2020届高三（18）班师生群')
while 1:
    now = datetime.datetime.now()
    nowstr = now.strftime('%Y/%m/%d %H:%M:%S')[11:]
    print('\r{}'.format(nowstr), end='')
    if nowstr in ['06:30:00']:
        if itchat.send('打卡',toUserName = target) == 1:
            print('打卡1成功完成')
    if nowstr in ['14:00:00']:
        if itchat.send('打卡',toUserName = target) == 1:
            print('打卡2成功完成')
    if nowstr in ['19:00:00']:
        if itchat.send('打卡',toUserName = target) == 1:
            print('打卡3成功完成')
    time.sleep(1)

if __name__ == '__main__':
    itchat.auto_login()
    itchat.run()