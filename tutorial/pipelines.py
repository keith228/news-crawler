# -*- coding: utf-8 -*-

import re
import MySQLdb
from tutorial.items import NaverArticleItem, NaverCommentItem, NeteaseArticleItem
from tutorial.spiders.netease_spider import NeteaseSpider

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item

class MySQLPipeline(object):

    db_host = 'localhost'
    db_name = 'mers_zhwang'
    db_user = 'mers_zhwang'
    db_pw = 'Khhd7ALtc8XLhwVK'

    def open_spider(self, spider):
        try:
            self.conn = MySQLdb.connect(
                    host = self.db_host,
                    user = self.db_user,
                    passwd = self.db_pw,
                    charset = 'utf8'
                    )
            self.cur = self.conn.cursor()
            self.conn.select_db(self.db_name)
        except MySQLdb.Error, e:
            print 'MySQL error %d: %s' % (e.args[0], e.args[1])

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()

    def process_item(self, item, spider):
        values = []

        table_name = ''
        if isinstance(item, NaverArticleItem):
            table_name = 'articles'
        elif isinstance(item, NeteaseArticleItem):
            table_name = 'articles_163'
        elif isinstance(item, NaverCommentItem):
            # cleansing
            # ㅋㅋㅋㅋㅋㅋ/ㅎㅎㅎㅎㅎㅎ => ㅋ/ㅎ
            item['contents'] = re.sub(u'ㅋ{3,}', u'ㅋ', item['contents'], flags = re.M | re.S)
            item['contents'] = re.sub(u'ㅎ{3,}', u'ㅎ', item['contents'], flags = re.M | re.S)
            table_name = 'comments'

        sql = u'insert into ' + table_name + ' ('
        for key in item.keys():
            sql += key
            sql += ','
        sql = sql[:-1]
        sql += ') values ('
        for i in item.items():
            values.append((i[1]))
            sql += '%s,'
        sql = sql[:-1]
        sql += ')'

        self.cur.execute(sql, values)
        self.conn.commit()

        return item

