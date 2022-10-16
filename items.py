# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DangdangbookItem(scrapy.Item):
    #标题
    title = scrapy.Field()
    #价格
    price = scrapy.Field()
    #封面图片链接
    image_url = scrapy.Field()