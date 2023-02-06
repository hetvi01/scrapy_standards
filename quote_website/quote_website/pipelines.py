# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import logging
import os
import sqlite3

import psycopg2
from dotenv import load_dotenv, find_dotenv
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.utils import spider

logger = logging.getLogger(__name__)
load_dotenv(find_dotenv())


class QuoteWebsitePipeline:
    def __init__(self):
        self.create_connection_postgresql()
        self.create_table()

    # prerequisites
    def create_connection_sqlite(self):
        logger.info("Start Establishing connection")
        self.connection = sqlite3.connect("quotes_db")
        self.cursor = self.connection.cursor()
        logger.info("Established connection")

    def create_connection_postgresql(self):
        logger.info("Start Establishing connection")
        self.connection = psycopg2.connect(host=os.getenv('DB_HOST'), user=os.getenv('DB_USER'),
                                           password=os.getenv('DB_PASSWORD'), dbname=os.getenv('DB_NAME'))
        self.cursor = self.connection.cursor()
        logger.info("Established connection")

    def create_table(self):
        logger.info('Start Creating Tables')
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS quotes (
                                                title text,
                                                author text,
                                                tags text,
                                                tag_links text,
                                                tag_links1 text
                                            )
                    """)
        logger.info("Tables Created")

    def store_db(self, item):
        logger.info("Storing data to row of table")
        title = item['title'][0]
        with self.connection:
            with self.connection.cursor() as cur:
                cur.execute("""SELECT exists(SELECT * FROM quotes WHERE title=%s)""", (item['title'][0],))
                result = cur.fetchone()
        if not result[0]:
            self.cursor.execute("""INSERT INTO quotes VALUES (%s,%s,%s,%s,%s)""",
                                (
                                    title,
                                    item['author'][0],
                                    str(item['tags']),
                                    str(item['tag_links']),
                                    item['tag_links1']
                                )
                                )
            logger.info("Stored data to row of table")
        else:
            logger.info(f"Item Storing skipped, Item with title:{title} is already exist in db")

    def process_item(self, item, spider):
        self.store_db(item)
        self.connection.commit()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.connection.close()
        logger.info("Connection closed successfully!!")
