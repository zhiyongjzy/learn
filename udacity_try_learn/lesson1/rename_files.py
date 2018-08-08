import os

def rename_files():
    # 1) get file names for a folder
    dir_path = os.getcwd() + "/prank/"
    file_list = os.listdir(dir_path);
    #print(file_list)
    # 2) for each file, rename filename.
    try:
        #print(os.name)
        for file in file_list:
            os.rename(dir_path+file, dir_path+file.strip("0123456789"))
    except OSError as e:
        print(e)

rename_files()
