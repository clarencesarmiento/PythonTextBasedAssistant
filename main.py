from help import help_command
from error import printline
import tasks
import os
import filefinder


print("""Text-Based Mini Assistant [Version 1.0]
(c) January 17, 2021 / Clarence Sarmiento""")

"""A Simple Python 3 Text-Based Mini Assistant"""


def request():
    req = str(input('\nAssistant:\\Command> ')).lower()
    return req


class Assistant(object):

    def commands_to_actions(self, command):
        method = getattr(self, command, lambda: printline('ERROR: Unregistered Command. Try "help".'))
        return method()

    @staticmethod
    def help():
        return help_command()

    @staticmethod
    def file():
        filefinder.locate()

    @staticmethod
    def microsoft():
        return tasks.microsoft()

    @staticmethod
    def website():
        return tasks.websites()

    @staticmethod
    def application():
        return tasks.applications()

    @staticmethod
    def wifi():
        return tasks.wifi_password()

    @staticmethod
    def clear():
        os.system('cls')

    @staticmethod
    def close():
        tasks.close()

    @staticmethod
    def exit():
        exit()


while True:
    x = Assistant()
    x.commands_to_actions(request())
