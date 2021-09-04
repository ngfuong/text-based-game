class Menu:
    def __init__(self, kind, end=False, options=None):
        self.kind = kind
        self.end = end
        if options is None:
            self.options = {}
        self.options = options
        self.options["Others"] = ("Exit", exit_conversation())

    def add_option(self, option):
        pass

    def print_menu(self):
        for k, v in self.options.item():
            print("({key}) - {description}".format(key=k, description=v))

    def exit_conversation(self):
        self.end = True
        return