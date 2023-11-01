'''
File sorter sorts files in folders named by the file extensions
'''
import os


def create_folder(path: str, extension: str) -> str:
    '''
    Creates a folder named after the extension fo the file passed in
    '''
    folder_name: str = extension[1:]  # get name after .
    folder_path: str = os.path.join(path, folder_name)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    return folder_path
