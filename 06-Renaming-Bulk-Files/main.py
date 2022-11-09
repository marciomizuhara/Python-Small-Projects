import os

# PROMPT THE USER FOR THE DIRECTORY PATH
folder_path = str(input('Enter the directory name of the files you want to rename: ')) + '/'
folder_path.replace("\\", "/")

# PROMPT THE USER FOR THE EXTENSION/FILE TYPE OF THE FILES THEY WANT TO RENAME
extension = str(input('Enter the extension (without the dot) of the files you want to rename: '))

# PROMPT THE USER FOR THE NEW FILENAME PREFIX THEY WANT TO SET FOR FILES
prefix = str(input('Enter the new filename prefix you want to set for files: '))


def main():
    counter = 0
    for filename in os.listdir(folder_path):
        if filename.split('.')[-1] == extension:
            new_filename = prefix + str(counter) + '.' + extension
            source = folder_path + filename
            new_filename = folder_path + new_filename
            os.rename(source, new_filename)
            print(f'{filename} renamed to {new_filename}')
        else:
            continue
        counter += 1


if __name__ == '__main__':
    main()
