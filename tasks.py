import subprocess
import webbrowser
import pywhatkit as kit
import getpass
import os
from error import printline
username = getpass.getuser()


def websites():
    website = str(input('Website: ')).lower()
    if 'facebook' in website or 'fb' in website:
        url = "https://www.facebook.com/"
        return webbrowser.get().open(url)
    elif 'youtube' in website or 'yt' in website:
        title = str(input('Title: '))
        if len(title) > 0:
            return kit.playonyt(title)
        else:
            print('No input found.')
    elif 'google' in website and 'google drive' not in website and 'google classroom' not in website:
        query = str(input('Search: '))
        url = "https://google.com/search?q=" + query
        return webbrowser.get().open(url)
    elif 'google drive' in website or 'gdrive' in website:
        url = 'https://drive.google.com/drive/u/0/my-drive?lfhs=2'
        webbrowser.get().open(url)
    elif 'google classroom' in website or 'classroom' in website:
        url = 'https://classroom.google.com/u/1/h'
        webbrowser.get().open(url)
    elif 'gmail' in website:
        url = "https://mail.google.com/"
        webbrowser.get().open(url)
    elif 'return' in website:
        pass
    else:
        if len(website) > 0:
            printline(f'ERROR: {website.capitalize()} not found.')
        else:
            printline('ERROR: No input found.')


def microsoft():
    application = str(input('Microsoft application: ')).lower()
    if 'word' in application:
        try:
            return subprocess.Popen(r'C:\Program Files (x86)\Microsoft Office\root\\Office16\WINWORD.EXE')
        except FileNotFoundError:
            return subprocess.Popen(r'C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE')
    elif 'powerpoint' in application or 'ppt' in application:
        try:
            return subprocess.Popen(r'C:\Program Files (x86)\Microsoft Office\root\\Office16\POWERPNT.EXE')
        except FileNotFoundError:
            return subprocess.Popen(r'C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE')
    elif 'excel' in application:
        try:
            return subprocess.Popen(r'C:\Program Files (x86)\Microsoft Office\root\Office16\EXCEL.EXE')
        except FileNotFoundError:
            return subprocess.Popen(r'C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE')
    elif 'pub' in application or 'publisher' in application:
        try:
            return subprocess.Popen(r'C:\Program Files (x86)\Microsoft Office\root\\Office16\MSPUB.EXE')
        except FileNotFoundError:
            return subprocess.Popen(r'C:\Program Files\Microsoft Office\root\Office16\MSPUB.EXE')
    elif 'outlook' in application:
        try:
            return subprocess.Popen(r'C:\Program Files (x86)\Microsoft Office\root\\Office16\OUTLOOK.EXE')
        except FileNotFoundError:
            return subprocess.Popen(r'C:\Program Files\Microsoft Office\root\Office16\OUTLOOK.EXE')
    elif 'onenote' in application:
        try:
            return subprocess.Popen(r'C:\Program Files (x86)\Microsoft Office\root\\Office16\ONENOTE.EXE')
        except FileNotFoundError:
            return subprocess.Popen(r'C:\Program Files\Microsoft Office\root\Office16\ONENOTE.EXE')
    elif 'access' in application:
        try:
            return subprocess.Popen(r'C:\Program Files (x86)\Microsoft Office\root\\Office16\MSACCESS.EXE')
        except FileNotFoundError:
            return subprocess.Popen(r'C:\Program Files\Microsoft Office\root\Office16\MSACCESS.EXE')
    elif 'return' in application:
        pass
    else:
        if len(application) > 0:
            printline(f'ERROR: {application.capitalize()} not found.')
        else:
            printline('ERROR: No input found.')


def applications():
    application = str(input('Application: ')).lower()
    if 'chrome' in application or 'google' in application:
        try:
            return subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe')
        except FileNotFoundError:
            return subprocess.Popen(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
    elif 'discord' in application:
        return subprocess.Popen(r'C:\Users\{}\AppData\Local\Discord\app-0.0.308\Discord.exe'.format(username))
    elif 'windows explorer' in application or 'explorer' in application:
        return subprocess.Popen(r'C:\Windows\explorer.exe')
    elif 'premiere' in application or 'adobe premiere' in application:
        try:
            return subprocess.Popen(r'C:\Program Files\Adobe\Adobe Premiere Pro 2020\Adobe Premiere Pro.exe')
        except FileNotFoundError:
            return subprocess.Popen(r'C:\Program Files (x86)\Adobe Premiere Pro 2020\Adobe Premiere Pro.exe')
    elif 'pycharm' in application:
        try:
            return subprocess.Popen(r'C:\Program Files\JetBrains\PyCharm Community Edition 2020.2.1\bin\pycharm64.exe')
        except FileNotFoundError:
            return subprocess.Popen(r'C:\Program Files (x86)\JetBrains\PyCharm Community Edition '
                                    r'2020.2.1\bin\pycharm64.exe')
    elif 'steam' in application:
        try:
            return subprocess.Popen(r'C:\Program Files\Steam\steam.exe')
        except FileNotFoundError:
            return subprocess.Popen(r'C:\Program Files (x86)\Steam\steam.exe')
    elif 'cad' in application or 'autocad' in application:
        try:
            return subprocess.Popen(r'C:\Program Files\Autodesk\AutoCAD 2019\acad.exe')
        except FileNotFoundError:
            return subprocess.Popen(r'C:\Program Files (x86)\Autodesk\AutoCAD 2019\acad.exe')
    elif 'notepad' in application or 'note' in application:
        subprocess.Popen('notepad.exe')
    elif 'return' in application:
        pass
    else:
        if len(application) > 0:
            printline(f'ERROR: {application.capitalize()} not found.')
        else:
            printline('ERROR: No input found.')


def close():
    application = str(input('Application: '))
    if 'word' in application:
        return os.system('taskkill/f /im WINWORD.EXE')
    elif 'ppt' in application or 'powerpoint' in application:
        return os.system('taskkill/f /im POWERPNT.EXE')
    elif 'excel' in application:
        return os.system('taskkill/f /im EXCEL.EXE')
    elif 'pub' in application or 'publisher' in application:
        return os.system('taskkill/f /im MSPUB.EXE')
    elif 'outlook' in application:
        return os.system('taskkill/f /im OUTLOOK.EXE')
    elif 'onenote' in application:
        return os.system('taskkill/f /im ONENOTE.EXE')
    elif 'access' in application:
        return os.system('taskkill/f /im MSACCESS.EXE')
    elif 'browser' in application:
        return os.system('taskkill/f /im chrome.exe')
    elif 'notepad' in application:
        return os.system('taskkill/f /im notepad.exe')
    elif 'discord' in application:
        return os.system('taskkill/f /im Discord.exe')
    elif 'groove' in application:
        return os.system('taskkill/f /im Music.UI.exe')
    elif 'adobe' in application:
        return os.system('taskkill/f /im AcroRd32.exe')
    elif 'explorer' in application or 'windows explorer' in application:
        return os.system('taskkill/f /im explorer.exe & start explorer')
    elif 'return' in application:
        pass
    else:
        if len(application) > 0:
            printline(f'ERROR: {application.capitalize()} not available.')
        else:
            printline('ERROR: No input found.')


def wifi_password():
    connected_wifi = []
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
    for line in data:
        if 'All User Profile' in line:
            wifi = line.split(':')[1][1:-1]
            connected_wifi.append(wifi)
    for wifi in connected_wifi:
        result = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', wifi,
                                          'key=clear']).decode('utf-8').split('\n')
        for lines in result:
            if 'Key Content' in lines:
                password = lines.split(':')[1][1:-1]
                try:
                    print(f'Name: {wifi}  \nPassword: {password}')
                except IndexError:
                    print(f'Name: {wifi}  \n[Password not stored!]')
