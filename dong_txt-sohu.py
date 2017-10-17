# -*- coding: utf-8 -*-
import os
import string
import re
num = 12
i = 0
filename_txt = "/home/yutuo/data/搜狐股吧/" + str(num).zfill(6) + "/" + str(i) + ".txt"
with open(filename_txt, 'r')as fp:
    allLines = fp.readlines()
r = 0
count = 0


i = 0
author_index = re.compile(r'^作者')
author = (allLines[r + i].decode('gbk')).encode('utf-8')
while str(re.match(author_index, author)) == 'None':
    i = i+1
    author = (allLines[r + i].decode('gbk')).encode('utf-8')
if i>count:
    count =i


i = 0
body_index = re.compile(r'^内容2')
body = (allLines[r + i].decode('gbk')).encode('utf-8')
while str(re.match(body_index, body)) == 'None':
    i = i + 1
    body = (allLines[r + i].decode('gbk')).encode('utf-8')
i = i+1
click_index = re.compile(r'^点击量')
click = (allLines[r + i].decode('gbk')).encode('utf-8')
while str(re.match(click_index, click)) == 'None':
    body = body +(allLines[r + i].decode('gbk')).encode('utf-8').strip()
    i = i + 1
    click = (allLines[r + i].decode('gbk')).encode('utf-8')
if(str(click[10:-3])==''):
    print "------"
    click="00000000000000"
if i>count:
    count =i


i = 0
time_index = re.compile(r'^提交时间')
time = (allLines[r + i].decode('gbk')).encode('utf-8')
while str(re.match(time_index, time)) == 'None':
    i = i + 1
    time = (allLines[r + i].decode('gbk')).encode('utf-8')
if (time.strip()=='提交时间:v class="commtop_ft_r">'):
    time =""
if i>count:
    count =i
print "time:",i


print author[9:-1]
print body[8:-1]
print time[13:-1]
print (click[10:-3])
print "\xe6\x8f\x90\xe4\xba\xa4\xe6\x97\xb6\xe9\x97\xb4"
print "\xe7\x82\xb9\xe5\x87\xbb\xe9\x87\x8f"



