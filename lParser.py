# lParaser.py
#!/user/bin/env python3
# -*- conding: utf-8 -*-

'lParser.py'
'@author LiuChen'

import re

import lConfig as config

class lParser():
	def __init__(self, confPath):
		self.conf = config.parse(confPath)

	def parserXML(self, content):
		content = self.parseContent(content)
		props = self.parseProp(content)
		return props

	def preHandle(self, line):
		line = line.replace(' ', '')
		line = line.replace('\n', '')
		return line

	def parseContent(self, content):
		startParser = False
		index = 0
		con = ''
		content = content.split('\n')
		for line in content:
			line = self.preHandle(line)
			# don't parse if need filter
			if not self.needFilter(line):
				if re.match(self.conf['start_tag'], line):
					startParser = True
				if re.match(self.conf['end_tag'], line):
					startParser = False
				if startParser:
					con += line
		return con

	def parseProp(self, content):
		def parseNameAndReg(s):
			tmp = s.split(':')
			return tmp[0], re.compile(tmp[1])

		def removeTag(line):
			regs = self.conf['remove_tag'].split(',')
			for reg in regs:
				pattern = re.compile(reg)
				line = pattern.sub('', line)
			return line

		props = []
		needTag = list(map(parseNameAndReg, self.conf['need_tag'].split(',')))
		content = re.compile(self.conf['target_tag']).findall(content)
		for m in content:
			prop = {}
			for name, pattern in needTag:
				prop[name] = list(map(removeTag, pattern.findall(m)[:]))
			props.append(prop)

		return props

	def needFilter(self, line):
		filters = self.conf['filters'].split(',')
		for s in filters:
			if line == '' or not re.match('<', line) or re.match('<' + s, line) or re.match('</' + s, line):
				return True
		return False