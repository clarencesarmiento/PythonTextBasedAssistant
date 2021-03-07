import colorama
from colorama import Fore, Style

colorama.init()


def help_command():
    print(
        "\n                     Python 3 Text-Based Mini Assistant \n" + Fore.RED +
        "               [COMMANDS]                   [FUNCTIONS] \n" + Style.RESET_ALL +
        """                HELP                        > Shows this text and exit.
                CLEAR                       > Clear Terminal.
                RETURN                      > Return to Command.
                EXIT                        > Exit Program.
                FILE                        > Locate and Open file.
                WEBSITE                     > Open Websites.
                MICROSOFT                   > Open Microsoft applications. 
                APPLICATION                 > Open Applications.
                WIFI                        > Shows all names and passwords of connected wifi.
                CLOSE                       > Close Applications. 
    _________________________________________________________________________ \n""" +
        Fore.RED + "       [MICROSOFT]              [WEBSITES]                 [APPLICATIONS]\n" + Style.RESET_ALL +
        """       WORD                      FACEBOOK                   CHROME
       POWERPOINT                YOUTUBE                    DISCORD
       EXCEL                     GOOGLE                     PYCHARM
       PUBLISHER                 GOOGLE DRIVE               ADOBE PREMIERE
       OUTLOOK                   GOOGLE CLASSROOM           STEAM
       ONENOTE                   GMAIL                      AUTOCAD
       ACCESS                                               NOTEPAD \n""" +
     
        Fore.RED + "\n      [FILETYPE]\n" + Style.RESET_ALL +
        """      .DOCX
      .PPTX 
      .PDF
      .TXT
      .PNG""")


help_command()
