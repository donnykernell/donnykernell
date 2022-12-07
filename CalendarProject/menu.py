class Menu:
    def __init__(self):
        self._commands = []
        self._should_run = True


    def run(self):
        while self._should_run:
            print(" Menu\n======")

            for i, cmd in enumerate(self._commands, 1):
                print("{}. {}".format(i, cmd.description()))

            try:
                select = int(input("Select: "))-1
                if select < 0 or select >= len(self._commands):
                    print("Invalid input!")
                else:
                    self._commands[select].execute()
            except ValueError:
                print("Value error!")
                continue



    def stop(self):
        self._should_run = False


    def register(self, command):
        self._commands.append(command)


class MenuCommand:

    def execute(self):
        raise NotImplementedError("you should implement this method in subclass")


    def description(self):
        raise NotImplementedError("you should implement this method in subclass")


class ExitCommand(MenuCommand):
    def __init__(self, menu):
        self._menu = menu


    def execute(self):
        self._menu.stop()


    def description(self):
        return "Exit"