import MySQLdb
conn = MySQLdb.Connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            passwd='root',
            db='stock',
            charset='utf8',
            use_unicode=True
        )
curdor = conn.cursor()
conn.autocommit(False)
for num in range (400,700):
    post_name = str(num).zfill(6) + "_1_post"
    try:
   # reply_name = str(num).zfill(6) + "_1_reply"
        #print post_name
        drop ="drop table %s"% post_name
        curdor.execute(drop)
        conn.commit()
    except Exception as e:
        conn.rollback()



curdor.close()
conn.close()