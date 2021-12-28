# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface


# class ZazaScrapyPipeline:
#     def process_item(self, item, spider):
#         return item

import sqlite3

class SQLitePipeline(object):

    #打开数据库
    def open_spider(self, spider):
        db_name = spider.settings.get('SQLITE_DB_NAME', 'main.db')
        print("------------------  CONNECTED ------------------")
        self.db_conn = sqlite3.connect(db_name)
        self.db_cur = self.db_conn.cursor()

    #关闭数据库
    def close_spider(self, spider):
        print("------------------  CLOSEED ------------------")
        self.db_conn.commit()
        self.db_conn.close()

    #对数据进行处理
    def process_item(self, item, spider):
        print("------------------  PROCESSING ------------------")
        self.insert_db(item)
        return item

    #插入数据
    def insert_db(self, item):
        print("------------------  INSERTING ------------------")
        values = (
            item['host'],
            item['title'],
            item['url'],
            item['author'],
            item['publish_date'],
            item['used'],
        )

        sql = 'INSERT INTO news VALUES(?,?,?,?,?,?)'
        self.db_cur.execute(sql, values)