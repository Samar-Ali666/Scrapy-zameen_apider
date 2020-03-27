# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import mysql.connector


class ZameenScrapingPipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='helloworld12345',
            database='zameen'
        )
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS houses_tb """)
        self.curr.execute("""create table houses_tb(
            location text,
            area text,
            beds int,
            description text,
            price text
            )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute("""insert into houses_tb values (%s,%s,%s,%s,%s)""", (
            item['location'][0],
            item['area'][0],
            item['beds'][0],
            item['description'][0],
            item['price'][0]
        ))

        self.conn.commit()
