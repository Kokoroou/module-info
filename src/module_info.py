from importlib import import_module


class ModuleInfo(object):
    def __init__(self, module_name):
        self.module = None
        self.object_names = None
        try:
            self.module = import_module(module_name)
            self.object_names = self.module.__dir__()
        except ModuleNotFoundError:
            print(f"No module named '{module_name}'")

    def print_object_info(self):
        if self.module:
            print(f"Objects in module '{self.module.__name__}':")

            # Length of the longest name of objects in module
            max_length = max(len(object_name) for object_name in self.object_names)

            for object_name in self.object_names:
                print(object_name.ljust(max_length) + ":", type(getattr(self.module, object_name)))
            print()

    def print_variable_info(self, function_name):
        """
        | Print all variables in a function and their types
        :param function_name: String
            Name of the function need to get information
        :return: None
        """
        if self.module:
            function = getattr(self.module, function_name)
            variable_names = function.__dir__()

            print(f"Objects in function '{function.__name__}':")
            # Length of the longest name of variables in function
            max_length = max(len(variable_name) for variable_name in variable_names)

            for variable_name in variable_names:
                print(variable_name.ljust(max_length) + ":", type(getattr(function, variable_name)))
            print()


if __name__ == "__main__":
    stop = False

    while not stop:
        module_name = input("Which module do you want to know? ")

        info = ModuleInfo(module_name)
        # info.print_object_info()
        info.print_variable_info("popen")

        while not stop:
            a = input("\nContinue?(Y/N) ")
            if a in "Nn":
                stop = True
                break
            elif a in "Yy":
                break
        print()


