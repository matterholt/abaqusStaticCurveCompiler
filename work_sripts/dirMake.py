"""
script to create the next counter measure folder and the copy files to new folder
"""
import shutil
import sys
import os
import re

def main ():
    """
    when script is executed the able to use a argv to supply script name of counter measueres
    either just number for the cm with no spaces or period, First to didgites are for version 
    the rest are for the revision  (example XXXX, XX.XX.X)   
    
    copy_content_folder --> contents inside folder will be copied to working dir
    working_dir --> folder where current development of the project, model saved and ran

    copy_content_folder :
        should contain No results files.
        only file in folder should be one required to run analysis
    """


    """ need to edit the path to where working dir """
    copy_contents_folder = "..\\base_runFiles"
    working_dir =  "..\\next_CM\\"

    """ 
    Folder naming convetions -> each project folder name style are different.
    varable should be change to style
    """

    v = "Ver"  # Version number
    r = "Rev"  # Revision number
    sep = "_"  # how to break up the sections

    folder_argv = sys.argv[-1]

    def add_model_name():
        """
        Ask user for just number of the Version and Revsion folder name.
        FEA counter measure letter are OK at the end
        """
        ver_rev_name = input("Add Model Name : ")
        return ver_rev_name
    
    def check_argv (name_v_r) :
        """
        Step 1: check if argv is OK, will return folder
        check the argv
        when the  argv is the name of script then will ask user if a default
        folder name is OK, if not the will fire function to ask user for input
        """
        if name_v_r == sys.argv[0]:
            print("Folder will have default name 'XXXXX'")
            if confirm == "y" :
                folder_name = "XXXXX"
                # print("Folder create {}" .format(folder_name))
                return folder_name
            else:
                print("Add Number of Version and Revision")
                folder_name = add_model_name()
                #print("Folder created {} ".format(folder_name))
                return folder_name
        else:
            #print("Folder created {}".format(name_v_r))
            return name_v_r

    """ Step 1: """
    version_revision_name = check_argv(folder_argv)
    print("Folder create {}".format(version_revision_name))


    def check_argv_length(name_conv) :
        """
        Step 2: convert argv to fit folder naming convetions 
        convert the argv to a style of naming folder, 
        """
        list_name = name_conv.split(".")
        if len(list_name) >= 3:
            check_name_three = v + list_name[0] + sep + r + list_name[1] + sep + list_name[3]
            return check_name_three
        elif len(list_name) == 2:
            check_name_two = v + list_name[0] + sep + r + list_name[1]
            return check_name_two
        else :
            check_name = v + name_conv[:2] + sep + r + name_conv[2:]
            return check_name
    
    """ Step 2 """
    folder_name_structure = check_argv_length(version_revision_name)
    print("\nPython will create folder {} \n".format(folder_name_structure))


    def create_folder(folder_name):
        """
        Step 3: create new folder
        copy files, creates folder with the naming conventions use for project
        working dir is or where analysis file are saved and ran
        """
        new_folder_name = working_dir + folder_name
        shutil.copytree(copy_contents_folder, new_folder_name)

    """Step 3:"""
    create_folder(folder_name_structure)


    def need_update_file ():
        """
        Some mesh files need to be updated with version and revision name
        """
        need_change = input("Does mesh.inp file need name update, y to continue : ")
        if need_change == "y" or need_change == "y": # NEED TO CHECK
            dirs = os.listdir(working_dir)
            for file in dirs:
                pattern_file = r"(mesh.*)[vV]\d+[rR]\d+(.\.inp)"
                match_file = re.fullmatch(pattern_file, file)
                if match_file:
                    file_rename_to = match_file.group(1) + folder_name_structure + match_file.group(2)
                    print("Old file name --> {}".format(file))
                    print("Rename file name --> {}".format(file_rename_to))
                    os.rename(working_dir + "\\" + file, working_dir + "\\" + file_rename_to)
        else:
            break
    print("File are copied to new folder")
    print("Job Completed Buddy !! \n")

if __name__ == "__main__":
    main()

