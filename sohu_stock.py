# -*- coding: utf-8 -*-
import sys,os
import MySQLdb
import re
import string
import shutil
import threading
import  datetime
import multiprocessing
conn ={}
curdor={}
def stock_I(num):
    filename = "/home/yutuo/data/搜狐股吧/" + str(num).zfill(6)
    if os.path.exists(filename):
        os.chdir("/home/yutuo/data/搜狐股吧/" + str(num).zfill(6))
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
        post_name = str(num).zfill(6) + "_3_post"
        print "doing:", filename
        creat_post = "create table if not exists %s" % post_name + "(post_id int unsigned auto_increment primary key,作者 varchar(50),内容 text,点击量 int(10) null,提交时间 varchar(50));"
        try:         # 创建post和reply表格
            curdor[num].execute(creat_post)
            conn[num].commit()
        except Exception as e:
            print "create table wrong:",e
            conn[num].rollback()
        os.system("cat *.txt >file_big.txt")
        filename_txt= "/home/yutuo/data/搜狐股吧/"+str(num).zfill(6)+"/file_big.txt"
        r=0
        with open(filename_txt, 'r')as fp:
            allLines = fp.readlines()
        while r < len(allLines): #处理 大文件
            count = 0
            i = 0
            author_index = re.compile(r'^作者')
            author = (allLines[r + i].decode('gbk')).encode('utf-8')
            while str(re.match(author_index, author)) == 'None':
                i = i + 1
                author = (allLines[r + i].decode('gbk')).encode('utf-8')
            if i > count:
                count = i
            #print "author:", i

            i = 0
            body_index = re.compile(r'^内容2')
            body = (allLines[r + i].decode('gbk')).encode('utf-8')
            while str(re.match(body_index, body)) == 'None':
                i = i + 1
                body = (allLines[r + i].decode('gbk')).encode('utf-8')
            i = i + 1
            click_index = re.compile(r'^点击量')
            click = (allLines[r + i].decode('gbk')).encode('utf-8')
            while str(re.match(click_index, click)) == 'None':
                body = body + (allLines[r + i].decode('gbk')).encode('utf-8')
                i = i + 1
                click = (allLines[r + i].decode('gbk')).encode('utf-8')
            if (str(click[10:-3]) == ''):
                click = "00000000000000"
            if i > count:
                count = i

            i = 0
            time_index = re.compile(r'^提交时间')
            time = (allLines[r + i].decode('gbk')).encode('utf-8')
            while str(re.match(time_index, time)) == 'None':
                i = i + 1
                time = (allLines[r + i].decode('gbk')).encode('utf-8')
            if (time.strip() == '提交时间:v class="commtop_ft_r">'):
                time = ""
            if i > count:
                count = i
            r = r+count
            #print "body+click:", i
            sql_insert = "insert into %s" % post_name + "(作者,内容,点击量,提交时间) VALUE (%s,%s,%s,%s)"
            try:
                curdor[num].execute(sql_insert, [author[9:-1], body[8:-1].strip(), click[10:-3], time[13:-1]])
                conn[num].commit()
            except Exception as e:
                #print e
                conn[num].rollback()


        end = datetime.datetime.now()
        print str(num).zfill(6), "using time:", (end - start)
        curdor[num].close()
        conn[num].close()


start = datetime.datetime.now()
if __name__ =="__main__":
    os.chdir("/home/yutuo/data/搜狐股吧/")
    pool = multiprocessing.Pool(processes=4)
    for i in xrange(0, 901000):
        pool.apply_async(stock_I, (i,))
    pool.close()
    pool.join()
    for i in xrange(0, 901000):
        file_name = "/home/yutuo/data/搜狐股吧/" + str(i).zfill(6)
        if (os.path.exists(file_name)):
            del_file = "rm -r " + file_name
            os.system(del_file)
    for count in xrange(1,602):
        for i in range(1000*(count-1), 1000 * count):
            filename = "/home/yutuo/data/搜狐股吧/" + str(i).zfill(6) + ".rar"
            if (os.path.exists(filename)):
                unrar_filename = "unrar x " + filename
                os.system(unrar_filename)
                print "unrar: ", filename
        pool = multiprocessing.Pool(processes=4)
        for i in xrange(0, 901000):
            pool.apply_async(stock_I, (i,))
        pool.close()
        pool.join()
        for i in range(0, 901000):
            filename = "/home/yutuo/data/搜狐股吧/" + str(i).zfill(6)
            if (os.path.exists(filename)):
                del_filename = "rm -r " + filename
                os.system(del_filename)
                print "remove: ", filename


