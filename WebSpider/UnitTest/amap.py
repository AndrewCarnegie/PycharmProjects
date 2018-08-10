import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    target_url = 'http://report.amap.com/detail.do?city=110000'
    headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 6.1;WOW64;Trident / 7.0;rv: 11.0)(like Gecko)',
        'Host': 'report.amap.com',
        'Cookie': 'BIDUPSID = 54FB9D873E724F7145419D61D08CADD3;PSTM = 1464682109;BAIDUID = 6F6F449348975D76C07FEA6BC4C936FD: FG = 1;H_PS_PSSID =;BDORZ = B490B5EBF6F3CD402E515D22BCDA1598;BD_UPN = 1126314351;ispeed_lsm = 2;H_PS_645EC = 9b0dAa5koumjG5wq0N % 2B5aXNMUvcERsSREhJopAdOZ % 2F441Q2KeVeL1zzOXbLZtBHMbBDvyCOO;BDSVRTM = 0'
    }

    req = requests.get(url=target_url, headers=headers)
    print(req.text)
