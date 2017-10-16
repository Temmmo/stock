import os
num =4
os.chdir("/home/yutuo/haileydata/eastmoney2/" + str(num).zfill(6))
print "/home/yutuo/haileydata/eastmoney2/" + str(num).zfill(6)
os.system("cat *.txt >file_big.txt")
filename_txt= "/home/yutuo/haileydata/eastmoney2/"+str(num).zfill(6)+"/file_big.txt"
r=0
with open(filename_txt, 'r')as fp:
    allLines = fp.readlines()
    print "file lines count:",len(allLines)