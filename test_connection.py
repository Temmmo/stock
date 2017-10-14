# -*- coding: utf-8 -*-
import MySQLdb
import sys
import json
coon = MySQLdb.Connect(
    host='127.0.0.1',
    port = 3306,
    user ='root',
    passwd='root',
    db='test',
    charset='utf8',
    use_unicode=True
)
curdor = coon.cursor()

sql ="select * from tdb_goods"
curdor.execute(sql)
print curdor.rowcount

rs = curdor.fetchone()
print str(rs).decode(encoding='unicode_escape')  #从mysql 中直接读出中文
rs =curdor.fetchmany(3)
print str(rs).decode(encoding='unicode_escape')

rs =curdor.fetchall()
print str(rs).decode(encoding='unicode_escape')
curdor.close()
coon.close()