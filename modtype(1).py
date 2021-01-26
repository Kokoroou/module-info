from importlib import import_module
from os import system
# import regex

class modtype:
	def __init__(self, name, hiden="False", obj_type=None):
		self.name = name
		self.hiden = hiden
		self.type = obj_type
		self.objects = []

		module = import_module(mod)
		# if self.hiden == "False"
	# def __str__(self):
