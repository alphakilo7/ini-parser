import os
import re
import sys
import json


class SectionNotFoundError(Exception):
	pass


class KeyNotFoundError(Exception):
	pass


class SectionExistsError(Exception):
	pass


class INIParser:
	def __init__(self, filename):
		self.__file = filename
		self.ini = open(self.__file, 'r').read().split('\n')

		self.__sections = []
		self.__settings = {}
		
		self.__remove_blanks_and_comments()
		self.__get_sects()
		self.__get_settings()

	# PRIVATE FUNCTIONAL METHODS
	def __remove_blanks_and_comments(self):
		ini_t = self.ini[:]
		self.ini.clear()
		for line in ini_t:
			if not line == '' and not line.lstrip()[0] == ";" and not line.lstrip()[0] == "#":
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

	# GETTER METHODS
	def get_sections(self):
		return self.__sections

	def get_all(self):
		return self.__settings

	def get(self, section, key=None):
		if key == None:
			return self.__settings[section]
		else:
			return self.__settings[section][key]

	# SETTER METHOD
	def set(self, section, key=None, value=None):
		if key == None and value == None and not section in self.__sections:
			self.__settings[section] = dict()
		elif key == None and value == None and section in self.__sections:
			raise SectionExistsError(f"The {section} already exists! Provide key and value pair to set.")
		else:
			try:
				self.__settings[section][key] = value
			except KeyError:
				self.__settings[section] = dict()
				self.__settings[section][key] = value

	# DELETE METHOD
	def delete(self, section, key=None):
		if key == None and not section in self.__sections:
			raise SectionNotFoundError(f"The {section} does not exist! Operation failed!")
		elif key == None and section in self.__sections:
			del self.__settings[section]
		else:
			try:
				del self.__settings[section][key]
			except KeyError:
				raise KeyNotFoundError(f"The key {key} in section {section} does not exist! Operation failed!")

	# COMMIT METHOD
	def commit(self):
		write_file = open("up_" + self.__file, "a+")
		write_file.truncate(0)
		for sect in self.__settings.keys():
			write_file.write("[" + sect + "]\n")
			for k, v in self.__settings[sect].items():
				write_file.write(k + "=" + v + "\n")
			write_file.write("\n")


def run():
	ini = INIParser('app.ini')
	print(ini.get("host:warlax-co", "logger"))
	ini.set("host:groots-in", "username", "grootsadmin")
	ini.set("host:groots-in", "password", "groots@123")
	ini.set("host:groots-in", "website", "www.groots.in")
	ini.delete("baseconfig", "port")
	print(ini.get_all())
	ini.commit()


if __name__ == "__main__":
	run()
