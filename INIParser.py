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
		print(self.ini)

	def __remove_blanks(self):
		pass


def run():
	ini = INIParser('app.ini')


if __name__ == "__main__":
	run()
