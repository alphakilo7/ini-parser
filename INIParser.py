import os
import re
import sys


class INIParser:
	def __init__(self, filename):
		self.ini = open(filename, 'r').read().split('\n')

		self.__sections = []
		self.__settings = dict()
		
		self.__remove_blanks_and_comments()
		self.__get_sects()
		self.__get_settings()
		# print(self.ini)

	def __remove_blanks_and_comments(self):
		ini_t = self.ini[:]
		self.ini.clear()
		for line in ini_t:
			if not line == '' and not line.lstrip()[0] == ";":
				self.ini.append(line)

	def __get_sects(self):
		for line in self.ini:
			if re.match(r"\[[a-zA-Z0-9\:_\-]+\]", line):
				self.__sections.append(re.sub(r"[\[]{1}|[\]]{1}", "", line))

	def __get_settings(self):
		for line in self.ini:
			if re.match(r"\[[a-zA-Z0-9\:_\-]+\]", line):
				head = re.sub(r"[\[]{1}|[\]]{1}", "", line)
				self.__settings[head] = dict()
			else:
				_key = line.split("=", 1)[0]
				_val = line.split("=", 1)[1]
				self.__settings[head][_key] = _val
				# self.__settings[head].append(line)

	def get_sections(self):
		return self.__sections

	def get_all(self):
		return self.__settings

	def get(self, section, key=None):
		if key == None:
			return self.__settings[section]
		else:
			return self.__settings[section][key]

	def test(self):
		pass


def run():
	ini = INIParser('app.ini')
	print(ini.get("host:warlax-co"))


if __name__ == "__main__":
	run()
