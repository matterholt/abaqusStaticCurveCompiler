'''

copy analysis file
'''

import shutil
import sys

def main():
    """
    working folders
    should contain NO results files, 
    Only file require to complete analysis
    
    - add a check for the other args, that will copy files for the (stiff, dpds,static,)
    - add some unit test.

    """
    copy_dpds_folder = ".\\DPDS" # what ever files within
    copy_stiff_folder = ".\\Stiffness" # contains 2 .fem, or more file
    working_dir = ".\\Model\\"

    '''
    Folder Naming Style
    '''
    V = "Ver"
    R = "_Rev"

    '''
    arg inputs, 
    '''
    model_name = sys.arg[-1]
    folder_name = V + model_name[:2] + R + model_name[2:]
    """
    create folder for version and revision number
    """


    

    '''
    copy files
    '''
    new_folder_create = working_dir + folder_path_name

    shutil.copytree(copy_stiff_folder,new_folder_create )

    print("File are copied")

if __name__ == "__main__":
    main()

