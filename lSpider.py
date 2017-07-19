# lSpider.py
#!/user/bin/env python3
# -*- conding: utf-8 -*-

'lSpider.py'
'@author LiuChen'

import urllib.request as request
import re

import lConfig as Config
from lParser import lParser as Parser

conf = Config.parse()

def connect(url = conf['url']):
	response = request.urlopen(url)
	return str(response.read().decode('utf-8'))

def main():
	out = open('out', 'w', encoding='utf-8')
	count = int(conf['count'])
	pre = int(conf['pre'])
	movies = []
	parserRank = Parser('rankConfig')
	parserDetails = Parser('detailConfig')
	for i in range(0, count, pre):
		# one page
		url = conf['url'].replace(r'{0}', str(i))
		content = connect(url)
		movies.append(parserRank.parserXML(content))
	out.write(str(movies).replace('\'', '"'))

# main
# main()