import os
import getpass
from error import printline

username = getpass.getuser()
path = 'C:\\Users\\{}\\'.format(username)
global name, directory, file_root


def word(filename):
    file_list = []
    global file_root, directory, name
    for root, directories, files in os.walk(path, topdown=False):
        for name in files:
            # for specific file type
            if name.endswith('.docx'):
                if filename in name.lower():
                    file_list.append(name)
                    print('\n'f'Found in: {root}')
                    print((len(file_list)), ')', name)
                    file_root = root
    if len(file_list) > 1:
        print(f'[SUCCESS]: {len(file_list)} files found for {filename}.')
        choice = int(input('Choice|return[0]: '))
        for file in file_list:
            try:
                if choice == file_list.index(file) + 1:
                    directory = (os.path.join(file_root, file))
                    return os.startfile(directory)
                elif 0 == choice:
                    break
            except FileNotFoundError:
                printline('[ERROR|docx]: File unavailable.')
    elif len(file_list) == 1:
        print(f'[SUCCESS]: {len(file_list)} file found for {filename}.')
        choice = int(input('Choice|return[0]: '))
        for file in file_list:
            try:
                if choice == file_list.index(file) + 1:
                    directory = (os.path.join(file_root, file))
                    return os.startfile(directory)
                elif 0 == choice:
                    break
            except FileNotFoundError:
                printline('[ERROR|docx]: File unavailable.')
    else:
        printline('[ERROR|docx]: 0 file found.')


def powerpoint(filename):
    file_list = []
    global file_root, directory, name
    for root, directories, files in os.walk(path, topdown=False):
        for name in files:
            # for specific file type
            if name.endswith('.pptx'):
                if filename in name.lower():
                    file_list.append(name)
                    print('\n'f'Found in: {root}')
                    print((len(file_list)), ')', name)
                    file_root = root
    if len(file_list) > 1:
        print(f'[SUCCESS]: {len(file_list)} files found for {filename}.')
        choice = int(input('Choice|return[0]: '))
        for file in file_list:
            try:
                if choice == file_list.index(file) + 1:
                    directory = (os.path.join(file_root, file))
                    return os.startfile(directory)
                elif 0 == choice:
                    break
            except FileNotFoundError:
                printline('[ERROR|pptx]: File unavailable.')
    elif len(file_list) == 1:
        print(f'[SUCCESS]: {len(file_list)} file found for {filename}.')
        choice = int(input('Choice|return[0]: '))
        for file in file_list:
            try:
                if choice == file_list.index(file) + 1:
                    directory = (os.path.join(file_root, file))
                    return os.startfile(directory)
                elif 0 == choice:
                    break
            except FileNotFoundError:
                printline('[ERROR|pptx]: File unavailable.')
    else:
        printline('[ERROR|pptx]: 0 file found.')


def portable_document_format(filename):
    file_list = []
    global file_root, directory, name
    for root, directories, files in os.walk(path, topdown=False):
        for name in files:
            # for specific file type
            if name.endswith('.pdf'):
                if filename in name.lower():
                    file_list.append(name)
                    print('\n'f'Found in: {root}')
                    print((len(file_list)), ')', name)
                    file_root = root
    if len(file_list) > 1:
        print('\n'f'[SUCCESS]: {len(file_list)} files found for {filename}.')
        choice = int(input('Choice|return[0]: '))
        for file in file_list:
            try:
                if choice == file_list.index(file) + 1:
                    directory = (os.path.join(file_root, file))
                    return os.startfile(directory)
                elif 0 == choice:
                    break
            except FileNotFoundError:
                printline('[ERROR|pdf]: File unavailable.')
    elif len(file_list) == 1:
        print(f'[SUCCESS]: {len(file_list)} file found for {filename}.')
        choice = int(input('Choice|return[0]: '))
        for file in file_list:
            try:
                if choice == file_list.index(file) + 1:
                    directory = (os.path.join(file_root, file))
                    return os.startfile(directory)
                elif 0 == choice:
                    break
            except FileNotFoundError:
                printline('[ERROR|pdf]: File unavailable.')
    else:
        printline('[ERROR|pdf]: 0 file found.')


def portable_network_graphics(filename):
    file_list = []
    global file_root, directory, name
    for root, directories, files in os.walk(path, topdown=False):
        for name in files:
            # for specific file type
            if name.endswith('.PNG'):
                if filename in name.lower():
                    file_list.append(name)
                    print('\n'f'Found in: {root}')
                    print((len(file_list)), ')', name)
                    file_root = root
    if len(file_list) > 1:
        print('\n'f'[SUCCESS]: {len(file_list)} files found for {filename}.')
        choice = int(input('Choice|return[0]: '))
        for file in file_list:
            try:
                if choice == file_list.index(file) + 1:
                    directory = (os.path.join(file_root, file))
                    return os.startfile(directory)
                elif 0 == choice:
                    break
            except FileNotFoundError:
                printline('[ERROR|PNG]: File unavailable.\n')
    elif len(file_list) == 1:
        print(f'[SUCCESS]: {len(file_list)} file found for {filename}.')
        choice = int(input('Choice|return[0]: '))
        for file in file_list:
            try:
                if choice == file_list.index(file) + 1:
                    directory = (os.path.join(file_root, file))
                    return os.startfile(directory)
                elif 0 == choice:
                    break
            except FileNotFoundError:
                printline('[ERROR|PNG]: File unavailable.')
    else:
        printline('[ERROR|PNG]: 0 file found.')


def text(filename):
    file_list = []
    global file_root, directory, name
    for root, directories, files in os.walk(path, topdown=False):
        for name in files:
            # for specific file type
            if name.endswith('.txt'):
                if filename in name.lower():
                    file_list.append(name)
                    print('\n'f'Found in: {root}')
                    print((len(file_list)), ')', name)
                    file_root = root
    if len(file_list) > 1:
        print('\n'f'[SUCCESS]: {len(file_list)} files found for {filename}.')
        choice = int(input('Choice|return[0]: '))
        for file in file_list:
            try:
                if choice == file_list.index(file) + 1:
                    directory = (os.path.join(file_root, file))
                    return os.startfile(directory)
                elif 0 == choice:
                    break
            except FileNotFoundError:
                printline('[ERROR|txt]: File unavailable.\n')
    elif len(file_list) == 1:
        print(f'[SUCCESS]: {len(file_list)} file found for {filename}.')
        choice = int(input('Choice|return[0]: '))
        for file in file_list:
            try:
                if choice == file_list.index(file) + 1:
                    directory = (os.path.join(file_root, file))
                    return os.startfile(directory)
                elif 0 == choice:
                    break
            except FileNotFoundError:
                printline('[ERROR|txt]: File unavailable.')
    else:
        printline('[ERROR|txt]: 0 file found.')


def locate():
    filetype = str(input('Filetype: ')).lower()
    if '.docx' in filetype:
        filename = str(input('Filename: ')).lower()
        word(filename)
    elif '.pptx' in filetype:
        filename = str(input('Filename: ')).lower()
        powerpoint(filename)
    elif '.pdf' in filetype:
        filename = str(input('Filename: ')).lower()
        portable_document_format(filename)
    elif '.png' in filetype:
        filename = str(input('Filename: ')).lower()
        portable_network_graphics(filename)
    elif '.txt' in filetype:
        filename = str(input('Filename: ')).lower()
        text(filename)
    elif 'return' in filetype:
        pass
    else:
        printline('[ERROR]: Filetype unavailable. Type "help" for more information '
                  'or try adding "." at the beginning of the filetype.')
