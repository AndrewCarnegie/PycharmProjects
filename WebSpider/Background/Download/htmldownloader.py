# _*_ coding: utf-8 _*_

"""
This module aims to download the html content,


"""

import requests


class HtmlDownloader(object):
    def download(self, url):
        """
        :param url: the one which isn't crawled
        :return: the html content of url
        """
        if url is None:
            return None
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0'
        headers={'User-Agent': user_agent}
        req = requests.get(url, headers=headers)
        if req.status_code == 200:
            req.encoding = 'utf-8'
            return req.text
        return None
