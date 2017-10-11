# -*- coding: utf-8 -*-
import sys,os
import csv
import MySQLdb
import re
import shutil
import threading
import  datetime
import multiprocessing
conn ={}
curdor={}
def stock_I(num):
    filename = "/home/yutuo/stockdata/doc/" + str(num).zfill(6)
    if os.path.exists(filename):
        os.chdir("/home/yutuo/stockdata/doc/" + str(num).zfill(6))
        print "file exits"
        conn[num] = MySQLdb.Connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            passwd='root',
            db='stock',
            charset='utf8',
            use_unicode=True
        )
        curdor[num] = conn[num].cursor()
        conn[num].autocommit(False)
        #start = datetime.datetime.now()
        post_name = str(num).zfill(6) + "_1_post"
        reply_name = str(num).zfill(6) + "_1_reply"
        print "doing:", filename
        creat_reply = "create table if not exists %s" % reply_name + "(reply_id int unsigned auto_increment primary key,昵称 varchar(30),时间 varchar(30),内容 text,post_id int unsigned)"
        creat_post = "create table if not exists %s" % post_name + "(post_id int unsigned auto_increment primary key,访问 int(7),回复 int(5),昵称 varchar(30),时间 varchar(30),主题 varchar(50),内容 text)"
        #foreign_key = "alter table %s" % reply_name + " add foreign key(post_id) references %s" % post_name + "(post_id)"
        try:         # 创建post和reply表格
            curdor[num].execute(creat_post)
            curdor[num].execute(creat_reply)
            #curdor[num].execute(foreign_key)
            conn[num].commit()
        except Exception as e:
            #print e
            conn[num].rollback()
        os.system("cat *.txt >file_big.txt")
        filename_txt="/home/yutuo/stockdata/doc/"+str(num).zfill(6)+"/file_big.txt"
        r=0
        with open(filename_txt, 'r')as fp:
            allLines = fp.readlines()
        while r < len(allLines):       #处理 大文件
            visit_index = re.compile(r'^访问')
            line_2 = (allLines[r + 0].decode('gbk')).encode('utf-8')
            while str(re.match(visit_index, line_2)) == 'None':
                r = r + 1
                line_2 = (allLines[r + 0].decode('gbk')).encode('utf-8')
            #line_2 = allLines[num + 1].decode(encoding='gbk')
            line_2 = allLines[r + 1].decode(encoding='gbk')#回复
            if 0 == (int(line_2[3:-1]) != 0):
                sql_insert = "insert into %s" % post_name + "(访问,回复,昵称,时间,主题,内容) VALUE (%s,%s,%s,%s,%s,%s)"
                try:
                    line_1 = allLines[r + 0].decode(encoding='gbk')  # 访问
                    line_3 = allLines[r + 2].decode(encoding='gbk')  # 昵称
                    line_4 = allLines[r + 3].decode(encoding='gbk')  # 时间
                    line_5 = allLines[r + 4].decode(encoding='gbk')  # 主题
                    line_6 = allLines[r + 6].decode(encoding='gbk')  # 内容
                    curdor[num].execute(sql_insert,
                                        [line_1[3:-1], line_2[3:-1], line_3[3:-1], line_4[3:-1], line_5[3:-1],
                                         line_6[3:-1]])
                    conn[num].commit()
                except Exception as e:
                   # print e
                    #print "wroing"
                    conn[num].rollback()
                r = r + 10
            else:
                    sql_max_id = "select max(post_id) from %s" % post_name
                    sql_insert_post = "insert into %s" % post_name + "(访问,回复,昵称,时间,主题,内容) VALUE (%s,%s,%s,%s,%s,%s)"
                    sql_insert_reply = "insert into %s" % reply_name + "(昵称,时间,内容,post_id) VALUE (%s,%s,%s,%s)"
                    try:
                        line_1 = allLines[r + 0].decode(encoding='gbk')  # 访问
                        line_6 = allLines[r + 6].decode(encoding='gbk')
                        line_3 = allLines[r + 2].decode(encoding='gbk')  # 昵称
                        line_4 = allLines[r + 3].decode(encoding='gbk')  # 时间
                        line_5 = allLines[r + 4].decode(encoding='gbk')  # 主题
                        curdor[num].execute(sql_insert_post,
                                        [line_1[3:-1], line_2[3:-1], line_3[3:-1], line_4[3:-1], line_5[3:-1],
                                         line_6[3:-1]])
                        conn[num].commit()
                    except Exception as e:
                        #print e
                        #print "wroing2"
                        conn[num].rollback()
                    curdor[num].execute(sql_max_id)
                    max_id = curdor[num].fetchone()
                    try:
                        for i in range(0, int(line_2[3:-1])): #处理回复
                                w = allLines[r + 12 + i * 5].decode(encoding='gbk') # 昵称
                                y = allLines[r + 13 + i * 5].decode(encoding='gbk') # 内容
                                t = (allLines[r + 14 + i * 5].decode('gbk')).encode('utf-8') # 时间
                                time_index = re.compile(r'^时间')
                                while str(re.match(time_index, t)) == 'None':
                                    y = y + allLines[r + 14 + i * 5].decode(encoding='gbk')
                                    r = r + 1
                                    t = (allLines[r + 14 + i * 5].decode('gbk')).encode('utf-8')
                                t = allLines[r + 14 + i * 5].decode(encoding='gbk')  # shijian
                                curdor[num].execute(sql_insert_reply,
                                            [w[3:-1], t[3:-1], y[3:-1], max_id])

                        conn[num].commit()
                    except Exception as e:
                        #print e
                        #print "wroing3"
                        conn[num].rollback()
                    r = r + 12 + 5 * int(line_2[3:-1])
        end = datetime.datetime.now()
        print str(num).zfill(6), "using time:", (end - start)
        curdor[num].close()
        conn[num].close()


start = datetime.datetime.now()
if __name__ =="__main__":
    pool =multiprocessing.Pool(processes = 2)
    for i in xrange(600080,902000):
        pool.apply_async(stock_I,(i,))
    pool.close()
    pool.join()




