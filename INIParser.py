import os
import re
import sys


class INIParser:
	'''
	INIParser v1.0alpha072020
	Parse, modify .ini files in python.
	'''
	def __init__(self, filename):
		self.ini = open(filename, 'r').read().split('\n')

		self.__headers = []
		self.__settings = dict()
		
		self.__remove_blanks()
		self.__get_heads()
#		print(self.ini)

	def __remove_blanks(self):
		ini_t = self.ini[:]
		self.ini.clear()
		for line in ini_t:
			if not line == '':
				self.ini.append(line)

	def __get_heads(self):
		for line in self.ini:
			if re.match(r"\[[a-zA-Z0-9\:_\-]+\]", line):
				self.__headers.append(re.sub(r"[\[]{1}|[\]]{1}", "", line))

	def __get_settings(self):
		pass

	def get_headers(self):
		return self.__headers


def run():
	ini = INIParser('app.ini')
	print(ini.get_headers())


if __name__ == "__main__":
	run()
