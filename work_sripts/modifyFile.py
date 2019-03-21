# working progress




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