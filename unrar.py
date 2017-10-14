# -*- coding: utf-8 -*-
import rarfile
import os
os.chdir("/home/yutuo/downloads/teacherdata/股票贴吧数据/新浪股吧")
for num in range(1,901010):
    file_name = str(num).zfill(6)
    file_name_rar ="/home/yutuo/downloads/teacherdata/股票贴吧数据/新浪股吧/"+file_name+".rar"
    if os.path.exists(file_name_rar):
        if os.path.exists(file_name):
            print "已经存在"+file_name
            os.remove(file_name_rar)
        else:
            rar = rarfile.RarFile(file_name_rar)
            rar.extractall()
            rar.close()
            os.remove(file_name_rar)