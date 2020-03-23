 #-*- coding:utf-8 -*-
import requests
import itchat

KEY = '69d2f9f92399470f8cf0c79574d0b8c9'  #可以到图灵机器人官网申请一个，免费的

def get_response(msg):
    # 构造了要发送给服务器的数据
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : KEY,
        'info'   : msg,
        'userid' : 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json() # 字典的get方法在字典没有'text'值的时候会返回None而不会抛出异常
        return r.get('text')                        # 为了防止服务器没有正常响应导致程序异常退出，这里用try-except捕获了异常
    except:                                        # 如果服务器没能正常交互（返回非json或无法连接），那么就会进入下面的return
        return                                    # 将会返回一个None

#注册获取别人发来的信息方法
@itchat.msg_register(['Text','Map', 'Card', 'Note', 'Sharing', 'Picture'])
def tuling_reply(msg):
    print(msg.User["Nickname"])
    # print(msg.User['NickName'] +":"+ msg['Text'])
    reply = get_response(msg['Text'])         #调取图灵机器人获取回复
    print(reply+"\n")       #打印机器人回复的消息
    return reply

@itchat.msg_register([itchat.content.TEXT], isGroupChat=True)    #群消息的处理
def print_content(msg):
    if msg.User["NickName"] == '🈲不能说的㊙️密' or msg.User["NickName"] == '测试玩玩':
        #这里可以在后面加更多的or msg.User["NickName"]=='你希望自动回复群的名字'
        print(msg.User['NickName'] +":"+ msg['Text'])     #打印哪个群给你发了什么消息
        print(get_response(msg['Text'])+"\n")           #打印机器人回复的消息
        return get_response(msg['Text'])
    else:                                         #其他群聊直接忽略
        pass

itchat.auto_login(hotReload=True)
itchat.run()