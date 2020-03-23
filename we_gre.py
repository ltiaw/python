
import itchat,time
from itchat.content import *
import json
import requests
import re
from  urllib.request import urlretrieve
from datetime import datetime
import threading
import os


# import requests
# import itchat
# import time
# import datetime
# import json

from time import sleep

KEY = 'b2bcef8b8314458d94abffce64d9ab4c'


def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : KEY,
        'info'   : msg,
        'userid' : 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return



@itchat.msg_register(['Text','Map', 'Card', 'Note', 'Sharing', 'Picture', ])
def tuling_reply(msg):
    sleep(30)
    print("个人消息回复")
    if msg.User["NickName"] != "piano":
        print(msg.User['NickName'] +": "+ msg['Text'])
        reply = get_response(msg['Text'])
        print(reply+"\n")
        return reply



@itchat.msg_register([itchat.content.TEXT], isGroupChat=True)
def text_reply(msg):
    if msg.User["NickName"] == '🈲不能说的㊙️密' or msg.User["NickName"] == '测试2' or msg.User["NickName"] == "永盛系统沟通群":
        if msg['isAt']:
            print("进入群机器回复")
            print(msg.User['NickName'] + ":" + msg['Text'])
            print(get_response(msg['Text'])+"\n")
            word_text = msg['Content'][4:]
            print(word_text)
            print(get_response(word_text))
            return get_response(word_text)
    elif msg.User["NickName"] == '测试' and msg["Text"][0:3] =="@精彩":
        print("进入转发")
        group = itchat.get_chatrooms(update=True)
        from_user = ''
        for g in group:
            if g['NickName'] == '测试':
                from_group = g['UserName']
                itchat.send("[OK]", from_group)

            if g['NickName'] == '测试2':
                to_group = g['UserName']

        if msg['FromUserName'] == from_group:
            itchat.send('美女们上传一下:%s' % msg['Content'], to_group)
            print("转发【 %s 】成功" % msg["Content"])




def send_order_info():
    while True:
        print(datetime.today().hour)
        if datetime.today().hour > 8 and datetime.today().hour < 23:
            print('现在时间：', datetime.today())
            chatroom = itchat.get_chatrooms()
            for c in chatroom:
                print(c['UserName'], c['NickName'])
                if c['NickName'] in ['测试', '测试2']:
                    to_group = c["UserName"]
                    print("进入群发")
                    itchat.send_msg("大家好，我是聊天机器人，请@我聊天", to_group)
                    print("群发成功")
        else:
            pass
        print("等1小时")
        time.sleep(3600)



# itchat.auto_login(hotReload=True)
# itchat.run()
#
#

if __name__ == '__main__':
    # 登录
    itchat.auto_login(hotReload=True)
    # 创建一个线程用于侦听微信的消息
    t_reply = threading.Thread(target=itchat.run)
    # 创建一个线程用于定时发送消息
    # 启动线程
    t_send = threading.Thread(target=send_order_info)
    t_reply.start()
    t_send.start()
    t_reply.join()
    t_send.join()
