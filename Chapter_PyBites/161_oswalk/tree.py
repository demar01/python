def count_dirs_and_files(directory='.'):
    """Count the amount of of directories and files in passed in "directory" arg.
       Return a tuple of (number_of_directories, number_of_files)
    """
    dirs, files = 0, 0
    for _, dirs_list, files_list in os.walk(directory): #root, directory, files 
        dirs += len(dirs_list)
        files += len(files_list)
    return dirs, files

# for root, dirs, files in os.walk(directory):
#     if len(root)>100:
#         for name in files:
#             print(name)
#         print(getsize(root,))
#         print(sum(getsize(join(root, name)) for name in files), end=" ")