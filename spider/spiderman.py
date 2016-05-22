#coding:utf-8
from db.db_helper import DB_Helper
from detect.detect_proxy import Detect_Proxy
from spider.html_downloader import Html_Downloader
from spider.html_parser import Html_Parser


class SpiderMan(object):

    start_url = 'http://www.xicidaili.com/nn/'

    def __init__(self):
        self.db_helper = DB_Helper()
        self.downloader = Html_Downloader()
        self.parser = Html_Parser(self.db_helper)
        self.detecter = Detect_Proxy(self.db_helper)

    def crawl(self,page_start,page_end):
        '''

        :param page_start: 开始页
        :param page_end: 终止页
        :return:
        '''
        for page in range(page_start,page_end+1):
            url = self.start_url+str(page)
            self.parser.parser(self.downloader.download(url))













    pass
