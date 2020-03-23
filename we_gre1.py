# encoding:utf-8
import re
import pyto_mssql175
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

yyr = ("y", "Y", "1", "2", "3", "4", "5", "6", "7")
def get_response(msg):
    """获取图灵机器人

    :param msg: 信息
    :return: 返回结果
    """
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key': KEY,
        'info': msg,
        'userid': 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return "我要睡觉了"

#@itchat.msg_register(['Text','Map', 'Card', 'Note', 'Sharing', 'Picture', ])
# def tuling_reply(msg):
#     """个人机器回复
#
#     :param msg: 信息
#     :return:
#     """
#     print("个人消息回复")
#     print(g['NickName'] + ":" + msg['Text'])
#     if g["NickName"] not in ("piano", "3哥", "没有如果的如果"):
#         print(g['NickName'] +": "+ msg['Text'])
#         reply = get_response(msg['Text'])
#         print(reply+"\n")
#         return reply


@itchat.msg_register([itchat.content.TEXT], isGroupChat=True)
def text_reply(msg):
    """群回复

    :param msg:
    :return:
    """
    # 机器聊天
    print("11111111111111111111*****************************")
    print(msg)

    # 消息群ID
    print(msg['FromUserName'])
    from_group = msg['FromUserName']
    word_text1111 = msg['Content'][8:]
    print("11111111111111111111*****************************")
    # 查找群名
    group = itchat.get_chatrooms(update=True)
    for g in group:
        print(g)
        if g['UserName'] == from_group:
            print(g['NickName'])
            if g["NickName"] == '🈲不能说的㊙️密' or g["NickName"] == '测试3':
                print("机器聊天群有信息")
                print(msg["isAt"])
                if msg["Content"][:8] == "@A😘0001👊" or msg["isAt"]:
                    print("进入外群机器回复")
                    print(g['NickName'] + ":" + msg['Text'])
                    print(word_text1111)
                    return get_response(word_text1111)

        # 转发
        # elif g["NickName"] == '永盛系统沟通群':
        #     if msg["Content"][:8] == "@A😘0001👊" or msg["Content"][:1] == "y" \
        #             or msg["Content"][:1] == "Y" or msg["Content"][:4] == "麻烦提交":
        #         print('现在时间：', datetime.today())
        #         print("进入转发")
        #         group = itchat.get_chatrooms(update=True)
        #         for g in group:
        #             if g['NickName'] == '永盛系统沟通群':
        #                 from_group = g['UserName']
        #                 itchat.send("[OK]", from_group)

                    # if g['NickName'] == '文员＆组长*网管':
                    #     to_group = g['UserName']
                    #     print(to_group)
                    #     itchat.send('美女们上传一下，谢谢:%s' % msg['Content'], to_group)
                    #     print("转发【 %s 】成功" % msg["Content"])

        # 群SQL
            elif g["NickName"] == '测试2' or g["NickName"] == '测试':
                if msg["Content"][:8] == "@A😘0001👊" or msg["isAt"]:
                    print("*" * 50)
                    print("进入群1测试回复")
                    print("【群名】：" + g['NickName'] + "【用户】：" + msg['ActualNickName'] + ":" + "【内容】：" + msg['Text'])
                    groupName = g['NickName']             # 群名
                    word_ganhao = msg['Content'][13:]       # 缸号
                    word_Action = msg['Content'][9:11]     # 动作
                    print("消息内容为：%s " % msg['Content'])
                    print("动作：%s " % word_Action)
                    print("缸号：%s " % word_ganhao)
                    print("群名：%s" % groupName)
                    print("发言用户：%s" % msg['ActualNickName'])
                    print("是否@我？：%s" % msg["isAt"])

                    print("*" * 50)

                    # group = itchat.get_chatrooms(update=True)
                    # for g in group:
                    #     if g['NickName'] == groupName:
                    #         from_group = g['UserName']

                    # 如果后面空格返回提示
                    if word_Action in ("取消", "提交") and word_ganhao[0].isspace():
                        print("缸号前空格")
                        print("注意【缸号Y之间不要空格】\n请@我并按格式输入\n多个缸号请用逗号隔开\n例1:取消缸号Y180701251,Y18170126\n例2:提交缸号Y180701251,Y18170126")
                        # itchat.send("注意【缸号前不要空格】\n请@我并按格式输入\n多个缸号请用逗号隔开\n例1:取消缸号Y180701251,Y18170126\n例2:提交缸号Y180701251,Y18170126", from_group)
                        return "注意【取消缸号后面不要跟空格】\n请@我并按格式输入\n多个缸号请用逗号隔开\n例1:取消缸号Y180701251,Y18170126\n例2:提交缸号Y180701251,Y18170126"


                    elif word_Action in ("取消", "提交") and word_ganhao[0] not in yyr:
                        print("取消缸号后没跟正确的缸号")
                        return "请输入取消提交后直接跟缸号"

                    #  取消提交
                    elif word_Action == "取消" and word_ganhao[0:1] in yyr:
                        print('现在时间：', datetime.today())
                        ganhao_count = 0
                        ganHaoOK = 0
                        notOK_list = []
                        ganhaos = re.split("[,.，。 ]", word_ganhao)
                        for ganhao in ganhaos:
                            print(ganhao)
                            result_select = pyto_mssql175.select_data(ganhao)
                            ganhao_count += 1
                            if result_select == 99:
                                print("%s查询不到数据，请按格式输入正确的缸号" % ganhao)
                                itchat.send("查询不到缸号:%s 的数据，请按格式输入正确的缸号,多个缸号请用逗号隔开" % ganhao, from_group)
                                notOK_list.append(ganhao)
                                continue

                            result, out, post, bh, bj, sh, ys, fk, kj = result_select
                            print(result)
                            if result == 1:
                                print("确认已经上传，提交=%s,上传=%s\n缸号：%s\n编号：%s\n布种：%s\n色号：%s\n颜色：%s\n幅宽：%s\n克重：%s"
                                      % (out, post, ganhao, bh, bj, sh, ys, fk, kj))
                                itchat.send("确认已经上传\n缸号：%s\n编号：%s\n布种：%s\n色号：%s\n颜色：%s\n幅宽：%s\n克重：%s"
                                            % (ganhao, bh, bj, sh, ys, fk, kj),
                                            from_group)
                                pyto_mssql175.update0_data(ganhao)
                                ganHaoOK += 1
                                print("取消提交成功")
                                itchat.send("取消缸号: %s 成功" % ganhao, from_group)
                            elif result == 0:
                                print("还没上传\n缸号：%s\n编号：%s\n布种：%s\n色号：%s\n颜色：%s\n幅宽：%s\n克重：%s"
                                      % (ganhao, bh, bj, sh, ys, fk, kj))
                                itchat.send(
                                    "还没上传\n缸号：%s\n编号：%s\n布种：%s\n色号：%s\n颜色：%s\n幅宽：%s\n克重：%s"
                                    % (ganhao, bh, bj, sh, ys, fk, kj),
                                    from_group)
                                itchat.send("缸号 %s 还没上传不用取消，请输入正确的缸号" % ganhao, from_group)
                            elif result == 10:
                                print("已经提交但还没上传\n缸号：%s\n编号：%s\n布种：%s\n色号：%s\n颜色：%s\n幅宽：%s\n克重：%s"
                                      % (ganhao, bh, bj, sh, ys, fk, kj))
                                itchat.send(
                                    "已经提交但还没上传\n缸号：%s\n编号：%s\n布种：%s\n色号：%s\n颜色：%s\n幅宽：%s\n克重：%s"
                                    % (ganhao, bh, bj, sh, ys, fk, kj),
                                    from_group)
                                pyto_mssql175.update0_data(ganhao)
                                ganHaoOK += 1
                                print("取消提交成功")
                                itchat.send("取消缸号: %s 成功" % ganhao, from_group)
                        print("本次取消操作缸号总数为 %d 成功个数为 %d" % (ganhao_count, ganHaoOK))
                        itchat.send("本次取消操作缸号总数为 %d\n成功个数为 %d" % (ganhao_count, ganHaoOK), from_group)
                        break

                    # 申请提交
                    elif word_Action == "提交" and word_ganhao[0:1] in yyr:
                        print('现在时间：', datetime.today())
                        ganhao_count = 0
                        ganhaos = re.split("[,.，。 ]", word_ganhao)
                        for ganhao in ganhaos:
                            print(ganhao)
                            ganhao_count += 1
                            result_select = pyto_mssql175.select_data(ganhao)
                            if result_select == 99:
                                print("%s查询不到数据，请按格式输入正确的缸号" % ganhao)
                                itchat.send("查询不到缸号:%s 的数据，请按格式输入正确的缸号,多个缸号请用逗号隔开" % ganhao, from_group)
                                continue

                            result, out, post, bh, bj, sh, ys, fk, kj = pyto_mssql175.select_data(ganhao)
                            print(result)
                            if result == 1:
                                print("已经上传\n缸号：%s\n编号：%s\n布种：%s\n色号：%s\n颜色：%s\n幅宽：%s\n克重：%s"
                                      % (ganhao, bh, bj, sh, ys, fk, kj))
                                itchat.send("确认已经提交了，请检查一下\n缸号：%s\n编号：%s\n布种：%s\n色号：%s\n颜色：%s\n幅宽：%s\n克重：%s"
                                            % (ganhao, bh, bj, sh, ys, fk, kj), from_group)
                            elif result == 10:
                                print("已经提交但还没上传\n缸号：%s\n编号：%s\n布种：%s\n色号：%s\n颜色：%s\n幅宽：%s\n克重：%s"
                                      % (ganhao, bh, bj, sh, ys, fk, kj))
                                itchat.send("已经提交但还没上传，请检查一下\n缸号：%s\n编号：%s\n布种：%s\n色号：%s\n颜色：%s\n幅宽：%s\n克重：%s"
                                            % (ganhao, bh, bj, sh, ys, fk, kj), from_group)

                            elif result == 0:
                                print("还没上传\n缸号：%s\n编号：%s\n布种：%s\n色号：%s\n颜色：%s\n幅宽：%s\n克重：%s"
                                      % (ganhao, bh, bj, sh, ys, fk, kj))
                                itchat.send("确认还没上传 信息如下:\n缸号：%s\n编号：%s\n布种：%s\n色号：%s\n颜色：%s\n幅宽：%s\n克重：%s"
                                            % (ganhao, bh, bj, sh, ys, fk, kj), from_group)
                                pyto_mssql175.update1_data(ganhao)
                                itchat.send("提交缸号 %s 成功" % ganhao, from_group)
                        print("本次提交操作缸号总数为 %d" % ganhao_count)
                        itchat.send("本次提交操作缸号总数为：%d" % ganhao_count, from_group)

                    # 上传所有
                    elif word_Action == "鑫肸":
                        print("进入这步")
                        pyto_mssql175.update_all()
                        itchat.send("提交所有缸号成功", from_group)

                    # 群机器回复
                    else:
                        print("进入机器回复")
                        print(g['NickName'] + ":" + msg['Text'])
                        print(word_text1111)
                        return get_response(word_text1111)

def send_order_info():
    """定时发送

    """
    while True:
        print("现在的时间是 %d" % datetime.today().hour)
        if datetime.today().hour >= 0 and datetime.today().hour <= 24:
            print('现在时间：', datetime.today())
            chatroom = itchat.get_chatrooms()
            for c in chatroom:
                print(c['UserName'], c['NickName'])
                if c['NickName'] in ['测试2', '测试3']:
                    to_group = c["UserName"]
                    print("进入群发")
                    itchat.send_msg("程序正在运行中.........\n每小时提醒一次,没提醒则程序睡觉中", to_group)
                    print("群发成功")
        else:
            pass
        print("等1小时后再次群发")
        time.sleep(3600)


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
