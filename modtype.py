import <module_name> as module

"""
Print type of any unstrongly-private-object in a module
Change <module_name> to any module you want to know
"""
print(module.__dir__(), "\n")

max_len = max(len(i) for i in module.__dir__())

for i in module.__dir__():
	try:
		print(i + " "*(max_len - len(i)) + ": " + str(type(getattr(module, i))))
	except Exception as e:
		print(i + " "*(max_len - len(i))+": '{}' is not imported".format(i))