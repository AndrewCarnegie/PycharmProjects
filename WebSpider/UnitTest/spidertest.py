# import requests
# from bs4 import BeautifulSoup
#
# if __name__ == '__main__':
#     targets = 'http://www.biqukan.com/1_1094/5403177.html'
#     headers = {
#            'User-Agent': 'Mozilla / 5.0(Windows NT 6.1;WOW64;Trident / 7.0;rv: 11.0)(like Gecko)'
#            # 'Host': 'www.biqukan.com',
#            # 'Cookie': 'CNZZDATA1260938422=1775061477-1533044231-%7C1533082804; bcolor=; font=; size=; fontcolor=; width=; UM_distinctid=164f0dcb0c8fd-0f3035b1309efd-3a064d5a-100200-164f0dcb0c965b'
#
#     }
#     proxy = {'http': 'http://127.0.0.1:8080/', 'https': 'https://127.0.0.1:8080/'}
#     sesson = requests.Session()
#     req = sesson.get(url='http://www.biqukan.com//1_1094//5403177.html', headers= headers, proxies=proxy,)
#     print(req.text)

    # html_ = req.text
    # bs_ = BeautifulSoup(html_, 'html.parser')
    # texts = bs_.find_all('div', class_='showtxt')
    # print(texts)


import requests

target_url = 'http://www.biqukan.com/1_1094/5403177.html'
req = requests.get(url=target_url)
print(req.text)
