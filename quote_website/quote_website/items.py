# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
from dataclasses import dataclass

from scrapy import item


class QuoteWebsiteItem(item.Item):
    # define the fields for your item here like:
    title = item.Field()
    author = item.Field()
    tags = item.Field()
    tag_links = item.Field()
    tag_links1 = item.Field()


class QuoteWebsiteItem1(item.Item):
    # define the fields for your item here like:
    title1 = item.Field()
    author1 = item.Field()
    tags1 = item.Field()
    tag_links1 = item.Field()
    tag_links11 = item.Field()

# @dataclass
# class QuoteWebsiteItem():
#     title: str
#     author: str
#     tags: list
#     tag_links = list
#     tag_links1 = list
