# -*- coding: utf-8 -*-
import multiprocessing
import time
import re
import re
print("The number of CPU is:" + str(multiprocessing.cpu_count()))
create table if not exists yutuo (reply_id int unsigned auto_increment primary key,昵称 varchar(30),时间 varchar(30),内容 text,post_id int unsigned)type=MyISAM