# -*- coding: utf-8 -*-
import MySQLdb
import sys
import json
conn = MySQLdb.Connect(
    host='127.0.0.1',
    port = 3306,
    user ='root',
    passwd='root',
    db='test',
    charset='utf8',
    use_unicode=True
)
conn.autocommit(False)

curdor = conn.cursor()

sql ="select * from tdb_goods"
curdor.execute(sql)
rs = curdor.fetchmany(3)
for row in rs:
    print str(row).decode(encoding='unicode_escape')

curdor.close()
conn.close()