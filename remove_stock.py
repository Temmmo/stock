import os
os.chdir("/home/yutuo/haileydata/eastmoney2/")
for i in range(4, 1000):
    filename_txt= "/home/yutuo/haileydata/eastmoney2/"+str(i).zfill(6)
    try:
        line ="rm -r "+filename_txt
        os.system(line)
    except Exception as e:
        print filename_txt,"not in"
    print line


