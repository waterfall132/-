# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


def get_cookies_dict():
    #将cookie进行一个拆分，拆分后的内容存到键值对当中并进行返回
    cookies_str='dest_area=country_id%3D9000%26province_id%3D111%26city_id%3D0%26district_id%3D0%26town_id%3D0; __permanent_id=20221002205417272172101575772512927; ddscreen=2; search_passback=07b8352315f3cac400bc4b63fc0100000e006600fdbb4b63; __visit_id=20221016155745173286807672858659662; __out_refer=; __trace_id=20221016160835217175646357779900117; pos_0_start=1665907715261; pos_0_end=1665907716236; pos_9_end=1665907716155; ad_ids=3554379%2C3554365%7C%233%2C3; __rpm=s_112100...1665907630663%7Clogin_page...1665907710683; sessionID=pc_ed2b226b07224e5a7e5271e4c267507593fcd821a98e3f4c860e83d86c2f771d; USERNUM=pmk2syLMYp8uwbyjeNkJZg==; login.dangdang.com=.ASPXAUTH=LhHLc/9FOPyVAUCNfri4OvDV/wgmU78OJlxgprdmxn0kyRW+d/ildw==; dangdang.com=email=MTUwNTM4MDM5NzE0NDgzMkBkZG1vYmlscGhvbmVfX3VzZXIuY29t&nickname=&display_id=2846550643805&customerid=aXyeCBXIeKlMHds4uA8qvA==&viptype=cI9HxdJlKxg=&show_name=150****3971; LOGIN_TIME=1665907715213'
    cookie_dict = {}  # 字典
    for item in cookies_str.split(";"):
        key,value=item.split('=',maxsplit=1)
        cookie_dict[key]=value
    return cookie_dict

COOKIES_DICT2=get_cookies_dict()

class DangdangbookSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class DangdangbookDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        request.cookies = COOKIES_DICT2
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
