# encoding:utf-8
import re
import pymssql
import decimal

def select_data(ganhao):


    server = "192.168.1.175"
    msuser = "sa12"
    pwd = "886391**"
    db = "Erp"

    conn = pymssql.connect(host=server, user=msuser, password=pwd, database=db, charset="utf8")
    cur = conn.cursor()
    # if not cur:
    #     raise (NameError, "连接数据库失败")
    # else:
    #     print("连接数据库成功")


    cursor_2 = conn.cursor()
    cursor_2.execute('SELECT out,post,bh,mc,ys,ysmc,hk,kg FROM Cpjcd WHERE dh=%s', ganhao)

    result = cursor_2.fetchall()
    cur.close()
    conn.close()
    if len(result) == 0:
        return 99

    for row in result:
        out = row[0]
        post = row[1]
        bh = row[2]
        bj = row[3]
        sh = row[4]
        ys = row[5]
        fk = row[6]
        kj = row[7]

    if out is True and post is True:  # 提交上传都是1 已经OK
        return (1,out, post,bh, bj, sh, ys, fk, kj)

    elif out is False and post is False:  # 提交上传都是0 不OK
        return (0,out, post,bh, bj, sh, ys, fk, kj)

    elif out is True and post is False: # 提交1上传0  已提交上传不成功
        return (10,out, post,bh, bj, sh, ys, fk, kj)


def update0_data(ganhao):

    server = "192.168.1.175"
    msuser = "sa12"
    pwd = "886391**"
    db = "Erp"

    conn = pymssql.connect(host=server, user=msuser, password=pwd, database=db, charset="utf8")
    cur = conn.cursor()
    # if not cur:
    #     raise (NameError, "连接数据库失败")
    # else:
    #     print("连接数据库成功")

    cursor_3 = conn.cursor()
    cursor_3.execute('Update Cpjcd set out=0,post=0 WHERE dh=%s', ganhao)
    conn.commit()
    cur.close()
    conn.close()


def update1_data(ganhao):

    server = "192.168.1.175"
    msuser = "sa12"
    pwd = "886391**"
    db = "Erp"

    conn = pymssql.connect(host=server, user=msuser, password=pwd, database=db, charset="utf8")
    cur = conn.cursor()
    # if not cur:
    #     raise (NameError, "连接数据库失败")
    # else:
    #     print("连接数据库成功")

    cursor_3 = conn.cursor()
    cursor_3.execute('Update Cpjcd set out=1 WHERE dh=%s', ganhao)
    conn.commit()
    cur.close()
    conn.close()


def update_all():

    server = "192.168.1.175"
    msuser = "sa12"
    pwd = "886391**"
    db = "Erp"

    conn = pymssql.connect(host=server, user=msuser, password=pwd, database=db, charset="utf8")
    cur = conn.cursor()
    # if not cur:
    #     raise (NameError, "连接数据库失败")
    # else:
    #     print("连接数据库成功")

    cursor_3 = conn.cursor()
    cursor_3.execute('update cpjcd set out=1 where post=0')
    conn.commit()
    cur.close()
    conn.close()


if __name__ == '__main__':
    while True:
        print("*"*50)
        print("1.泰旺取消缸号程序V1.110----by ltiaw@126.com")
        print("2.按 回车键 退出,多个缸号用逗号分开")
        ganHao_input = input("3.请输入你要取消的缸号：")
        print("*"*50)
        ganhaos = re.split("[,.，。 ]", ganHao_input)
        ganhao_count = 0
        ganHaosOk = 0
        for ganhao in ganhaos:
            print(ganhao)
            result_select = select_data(ganhao)
            ganhao_count += 1
            if result_select == 99:
                print("*"*50)

                print("查询不到缸号:%s 的数据，请按格式输入正确的缸号,多个缸号请用逗号隔开" % ganhao)
                continue

            result, out, post, bh, bj, sh, ys, fk, kj = result_select
            print(result)
            if result == 1:
                print("*" * 50)
                # print("确认已经上传，提交=%s,上传=%s\n缸号：%s\n编号：%s\n布种：%s\n色号：%s\n颜色：%s\n幅宽：%s\n克重：%s"
                #       % (out, post, ganhao, bh, bj, sh, ys, fk, kj))
                print("确认已经上传\n缸号：%s\n编号：%s\n布种：%s\n色号：%s\n颜色：%s\n幅宽：%s\n克重：%s"
                            % (ganhao, bh, bj, sh, ys, fk, kj))
                update0_data(ganhao)
                ganHaosOk += 1
                print("取消提交成功")
                print("取消缸号: %s 成功" % ganhao)
            elif result == 0:
                print("*" * 50)
                print("还没上传\n缸号：%s\n编号：%s\n布种：%s\n色号：%s\n颜色：%s\n幅宽：%s\n克重：%s"
                      % (ganhao, bh, bj, sh, ys, fk, kj))

                print("缸号 %s 还没上传不用取消，请输入正确的缸号" % ganhao)
            elif result == 10:
                print("已经提交但还没上传\n缸号：%s\n编号：%s\n布种：%s\n色号：%s\n颜色：%s\n幅宽：%s\n克重：%s"
                      % (ganhao, bh, bj, sh, ys, fk, kj))
                update0_data(ganhao)
                ganHaosOk += 1
                print("取消缸号: %s 成功" % ganhao)
        print("本次取消操作缸号总数为 %d 成功数为 %d" % (ganhao_count, ganHaosOk))
