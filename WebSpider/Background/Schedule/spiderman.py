# _*_ coding: utf-8 _*_

"""
This module is a scheduler, to cooperate other APIs

"""

from DataStoreage.dataoutput import DataOutput
from Download.htmldownloader import HtmlDownloader
from HTMLParser.htmlparser import HtmlParser
from URLManager.linkmanager import LinkManager


class SpiderMan(object):
    def __init__(self):
        self.manager = LinkManager()
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.output = DataOutput()

    def crawl(self, root_url):
        self.manager.add_new_url(root_url)
        while(self.manager.has_new_url() and self.manager.old_url_size() < 100):
            try:
                new_url = self.manager.get_new_url()
                html = self.htmldownloader.downloader(new_url)
                new_urls, data = self.htmlparser.parser(new_url, html)
                self.manager.add_new_urls(new_urls)
                self.output.store_data(data)
                print('%s urls has been crawled'%self.manager.old_url_size)
            except IOError:
                print('crawl failed')
        self.output.output_html()

        if __name__ == '__main__':
            spider_man = SpiderMan()
            spider_man.crawl('http://baike.baidu.com/view/284853.htm')