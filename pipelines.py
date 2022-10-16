# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import openpyxl
from itemadapter import ItemAdapter


class DangdangbookPipeline:
    def __init__(self):
        self.gongzuobu=openpyxl.Workbook()#创建工作簿对象
        self.worksheet=self.gongzuobu.active#拿到创建工作簿后默认的那一张表
        self.worksheet.title='当当图书'
        self.worksheet.append(('标题','价格','封面图片链接'))#表的表头

    def close_spider( self,spider ):#一旦爬虫结束时就应该保存数据到excel表格中
        self.gongzuobu.save('当当图书.xlsx')#为什么init函数里变量都要加上self：
        # 都是些局部变量，这样close_spider()拿不到init里的工作簿对象，这样加上self与管道进行一个绑定，
        # init函数里的变量就都变成了管道的属性，就可以穿透函数间的限制被调用（同一个类下局部变量穿刺技术）



    def process_item(self, item, spider):
        title=item.get('title','')
        price = item.get ( 'price', '')
        image_url = item.get('image_url', '')#这里意思是如果没有数据就用一个空字符串作为默认值
        # intro = item.get('intro','')
        self.worksheet.append((title,price,image_url))
        # self.worksheet.append ((item['name'],item['rank'],item['discription'],item['duration'],item['intro']))
        return item