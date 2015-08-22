import os


def rename_files():
    # get file names from a folder
    file_list = os.listdir('/home/aniket/github/python-code/prank')
    print file_list

    saved_path = os.getcwd()
    print 'The current working dir is', saved_path
    os.chdir('/home/aniket/github/python-code/prank')

    # for each file rename file name
    for file_name in file_list:
        print 'Old Name of file:', file_name
        print 'New name of file:', file_name.translate(None, '0123456789')
        os.rename(file_name, file_name.translate(None, '0123456789'))
    os.chdir(saved_path)

if __name__ == '__main__':
    rename_files()
