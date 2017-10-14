import os
for i in xrange(0,1000):
    file_name ="/home/yutuo/PycharmProjects/stock/"+str(i).zfill(6)
    if (os.path.exists(file_name)):
        del_file = "rm -r "+file_name
        os.system(del_file)