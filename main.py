'''
File sorter sorts files in folders named by the file extensions
'''
import os
import shutil


def create_folder(path: str, extension: str) -> str:
    '''
    Creates a folder named after the extension fo the file passed in
    '''
    folder_name: str = extension[1:]  # get name after .
    folder_path: str = os.path.join(path, folder_name)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    return folder_path


def sort_files(source_path: str):
    '''
    Sorts the files based on a given path
    '''

    # go through all the folders and files of the source_path
    for root_dir, sub_dir, filenames in os.walk(source_path):
        for filename in filenames:
            file_path: str = os.path.join(root_dir, filename)
            # split extension of file or return empty string
            extension: str = os.path.splitext(filename)[1]

            if extension:
                target_folder: str = create_folder(source_path, extension)
                target_path: str = os.path.join(target_folder, filename)

                shutil .move(file_path, target_path)
