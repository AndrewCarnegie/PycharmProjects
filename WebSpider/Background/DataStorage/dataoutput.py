# _*_ coding: utf-8 _*_

"""
This module aims to store the parsed data into cache
and output the data into html format



"""
import codecs


class DataOutput(object):
    def __init__(self):
        self.datas=[]

    def store_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_data(self):
        fout=codecs.open('baiki.html','w',encoding='utf-8')
        fout.write('<html>')
        fout.write('<body>')
        fout.write('<table>')
        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td>%s</td>'%data['url'])
            fout.write('<td>%s</td>'%data['title'])
            fout.wrtie('<td>%s</td>'%data['summary'])
            fout.write('/tr')
            self.datas.remove(data)
            fout.write('</table>')
            fout.write('</body>')
            fout.write('</html>')
            fout.close()
