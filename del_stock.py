import os
for i in xrange(0,1000):
    file_name ="/home/yutuo/PycharmProjects/stock/"+str(i).zfill(6)
    if (os.path.exists(file_name)):
        del_file = "rm -r "+file_name
        os.system(del_file)
for count in xrange(1, 902):
    for i in range(1000 * (count - 1), 1000 * count):
        filename = "/home/yutuo/data/搜狐股吧/" + str(i).zfill(6) + ".rar"
        if (os.path.exists(filename)):
            unrar_filename = "unrar x " + filename
            os.system(unrar_filename)
            print "unrar: ", filename
    pool = multiprocessing.Pool(processes=4)
    for i in xrange(3, 901000):
        pool.apply_async(stock_I, (i,))
    pool.close()
    pool.join()
    for i in range(3, 901000):
        filename = "/home/yutuo/data/搜狐股吧/" + str(i).zfill(6)
        if (os.path.exists(filename)):
            del_filename = "rm -r " + filename
            os.system(del_filename)
            print "remove: ", filename
