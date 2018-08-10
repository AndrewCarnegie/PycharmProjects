# _*_ coding: utf-8 _*_

"""
This module demonstrates how to manage the URL,
to distinguish which of them has been handled, or not been handled yet

"""


class LinkManager(object):

    def __init__(self):
        self.new_urls = set()  # URL set to be crawled
        self.old_urls = set()  # URL set already crawled

    def has_new_link(self):
        """check if there is new URL to be picked up"""
        return self.size_new_url() != 0

    def add_new_url(self, url):
        """ add the new URL to the data set which hasn't been crawled
        :param url: single url
        :return:
        """
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        """ add the new URLs to the data set which hasn't been crawled
        :param urls:  url set
        :return:
        """
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def get_new_url(self):
        """ get a new URL from the data set which hasn't been crawled"""
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

    def size_new_url(self):
        """ get a new URL from the data set which hasn't been crawled"""
        return len(self.new_urls)

    def size_old_url(self):
        """ get a new URL from the data set which hasn't been crawled"""
        return len(self.old_urls)
