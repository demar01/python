
def tail(filepath, n):
    """Similate Unix' tail -n, read in filepath, parse it into a list,
       strip newlines and return a list of the last n lines"""
    with open(filepath, encoding="utf-8") as f:
        return f.read().splitlines(keepends=False)[-n:]


#filepath = "/Users/dermit01/Documents/python/Chapter_PyBites/100_Tail_file_unix/readme.md"
#note that the default behavious of splitlines is keepends=False. If keepends is provided and True, line breaks are also included in items of the list.

# this will read the file
# with open(filepath, encoding="utf-8") as f:
#     print(f.read())

# this will read the file and return the output into a list
# with open(filepath, encoding="utf-8") as f:
#     print(f.read().splitlines())

# from pathlib import Path
# import os
# os.getcwd()
# #  print(Path('Chapter_PyBites/100_Tail_file_unix/readme.md').absolute())
