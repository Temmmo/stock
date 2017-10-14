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
curdor = conn.cursor()
conn.autocommit(False)
sql_insert = "insert into tdb_goods_brands(brandid,brand_name) VALUE (10,'蘑菇')"
sql_update = "update tdb_goods_brands set brand_name ='猪' "
sql_delete = "delete from tdb_goods_brands where brand_id<3"
try:
    curdor.execute(sql_insert)
    print curdor.rowcount
    curdor.execute(sql_update)
    print curdor.rowcount
    curdor.execute(sql_delete)
    print curdor.rowcount
    conn.commit()
except Exception as e:
    print e
    conn.rollback()
curdor.close()
conn.close()