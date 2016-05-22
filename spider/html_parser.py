#coding:utf-8
from bs4 import BeautifulSoup
from db.db_helper import DB_Helper
from entity.proxy_info import proxy_infor
from spider.html_downloader import Html_Downloader

'''
html解析器
'''
class Html_Parser(object):


    def __init__(self,db_helper):
        self.db_helper = db_helper


    def parser(self,html_cont):
        '''
        :param html_cont:
        :return:
        '''
        if html_cont is None:
            return

        # 使用BeautifulSoup模块对html进行解析
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        tr_nodes = soup.find_all('tr',class_ = True)

        for tr_node in tr_nodes:
            proxy = proxy_infor()
            i = 0
            for th in tr_node.children:
                if th.string != None and len(th.string.strip()) > 0:
                    proxy.proxy[proxy.proxyName[i]] = th.string.strip()
                    print  'proxy',th.string.strip()
                    i += 1
                    if(i>1):
                        break
            self.db_helper.insert({proxy.proxyName[0]:proxy.proxy[proxy.proxyName[0]],proxy.proxyName[1]:proxy.proxy[proxy.proxyName[1]]},proxy.proxy)




