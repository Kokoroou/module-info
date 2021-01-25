from importlib import import_module
from os import system

print("Which module do you want to know?")
mod = input()

try:
	module = import_module(mod)

	max_len = max(len(i) for i in module.__dir__())

	for i in module.__dir__():
		try:
			print(i + " "*(max_len - len(i)) + ": " + str(type(getattr(module, i))))
		except Exception:
			print(i + " "*(max_len - len(i))+": '{}' is not imported".format(i))
except ModuleNotFoundError:
	print("No module named '{}'".format(mod))

system("pause")
