# config.py
#!/user/bin/env python3
# -*- conding: utf-8 -*-

'config.py'
'@author LiuChen'

import re

pattern = re.compile(r'\w+=\S+')
conf={}
def parse(path = 'config') :
	try :
		file = open(path)
		for line in file.readlines() :
			if not re.match(r'#', line) :
				# start with # is a note line
				if pattern.findall(line) :
					# right formate
					s = line.replace('\n', '').split('=', 1)
					conf[s[0]] = s[1]
		return conf
	except Exception as err :
		print('something wrong happen: ', err)

	finally :
		print('Parse complete.')