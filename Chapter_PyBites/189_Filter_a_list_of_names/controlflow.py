from sys import getsizeof
import re 
IGNORE_CHAR = 'b'
QUIT_CHAR = 'q'
MAX_NAMES = 5


names = ['barry', 'tim', 'amber', 'ana', 'cindy', 'sara', 'molly', 'qhenry']
# list = ['12', 'bas']

def filter_names(names):
    result = []
    for name in names:
        if name.startswith(IGNORE_CHAR) or re.match(r".*\d+.*", name):
            continue
        if QUIT_CHAR in name or len(result) >= MAX_NAMES:
            break
        result.append(name)
    
    return result

def filter_names2(names):
    count = 0
    for name in names:
        if count == MAX_NAMES or name.startswith(QUIT_CHAR):
            break
        if name.startswith(IGNORE_CHAR) or any(char.isdigit() for char in name):
            continue
        count += 1
        yield name

#[i for i in filter_names2(names)]

# getsizeof(filter_names(names)) 120
# getsizeof(filter_names2(names)) 112