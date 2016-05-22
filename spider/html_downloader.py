#coding:utf-8
import urllib2


class Html_Downloader(object):

    def download(self,url):
        '''

        :param url: 需要访问的url
        :return:  返回html
        '''
        if url is  None:
            return None
        request = urllib2.Request(url)
        request.add_header('user-agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36')
        response= urllib2.urlopen(request)
        if response.getcode()!=200:
            return None
        return response.read()


