import os
import shutil
from os.path import exists

filenames = []
folder_path = str(input('Enter the directory name you want to organize: '))
folder_path.replace("\\", "/")


def get_folder_name(filename):
    """
    'Test.txt' --> 't'
    '010.txt' --> 'misc'
    'zebra.txt' --> 'z'
    'Alpha@@.txt' --> 'a'
    '!@#.txt' --> 'misc'
    """
    if filename[0].isalpha():
        return filename[0].lower()
    else:
        return 'misc'


def read_directory():
    """
    read the filename in the current directory and append them to a list
    """
    global filenames
    global folder_path
    for file in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, file)):
            filenames.append(file)
    if 'main.py' in filenames:
        filenames.remove('main.py')  # Make sure you remove the script main file from the list if current directory is chosen


#  GET THE FIRST LETTERS OF THE FILE AND CREATE A FILE IN THE CURRENT DIRECTORY
def create_folder():
    """
    create folders
    """
    global filenames
    global folder_path
    for f in filenames:
        if os.path.isdir(f'{folder_path}/{get_folder_name(f)}'):
            print(f'folder {get_folder_name(f)} already created.')
        else:
            os.mkdir(f'{folder_path}/{get_folder_name(f)}')
            print(f'creating folder {get_folder_name(f)}')


#  MOVE THE FILE INTO THE PROPER FOLDER
def move_to_folder():
    """
    move_to_folder('zebra.py','z)
    'zebra.py' moved to 'z' folder
    """
    global filenames
    for i in filenames:
        filename = i
        file = get_folder_name(i)
        source = os.path.join(folder_path, filename)
        destination = os.path.join(folder_path, file)
        if exists(f'{folder_path}/{get_folder_name(filename)}/{file}'):
            print(f'File {folder_path}/{get_folder_name(filename)} already exists')
        else:
            shutil.move(source, destination)
            print(f'File {folder_path}/{get_folder_name(filename)} moved to {destination}')


if __name__ == '__main__':
    read_directory()
    create_folder()
    move_to_folder()


