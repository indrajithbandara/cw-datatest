#-*-coding:utf-8-*-
import os

__author__ = 'huligong'

now_path = os.path.dirname(__file__)
file_root = os.path.join(os.path.dirname(now_path),'file','').replace('\\','/')

def get_folder_path(folder_name):
    return os.path.join(os.path.dirname(now_path),folder_name,'').replace('\\','/')

def get_image_folder(folder_name='image'):
    return get_folder_path(folder_name)

def get_file_folder(folder_name='file'):
    return get_folder_path(folder_name)

def get_db_folder(folder_name='db'):
    return get_folder_path(folder_name)

def main():
    print get_image_folder()
    print get_file_folder()
    print get_db_folder()

if __name__ == '__main__':
    main()