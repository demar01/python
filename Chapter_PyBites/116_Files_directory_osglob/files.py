#https://realpython.com/working-with-files-in-python/#filename-pattern-matching
#Another useful module for pattern matching is glob.

#created in the test 
# dirname='/tmp/tmpczm7lx4t'

import os
import glob

ONE_KB = 1024

def get_files(dirname, size_in_kb):
    """Return files in dirname that are >= size_in_kb"""
    for file in glob.glob(f"{dirname}/*"):
        if os.path.getsize(file) / ONE_KB >= size_in_kb:
            yield file



# with tempfile.TemporaryDirectory() as tmpdir:
#     print('Created temporary directory ', tmpdir)
#     os.path.exists(tmpdir)

# Created temporary directory  /var/folders/dl/wr0bjtw5793f5t0k2mw6dj31pgl01f/T/tmpz79lmn7j
# True
#tmpdir
#'/var/folders/dl/wr0bjtw5793f5t0k2mw6dj31pgl01f/T/tmpz79lmn7j'
# os.path.exists(tmpdir)
# False

# After the context manager goes out of context, the temporary directory is deleted and a call to os.path.exists(tmpdir) returns False



