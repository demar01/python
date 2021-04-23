bites={1: 'bob', 2: 'julian', 3: 'tim'}
exclude_bites={2, 3}

# for k, v in bites.items():
#     if k not in exclude_bites:
#         print({k, v}) 

def filter_dic(bites=bites, bites_done=exclude_bites):
    """return the bites dict with the exclude_bites filtered out"""
    return {k: v for k, v in bites.items() if k not in exclude_bites}
