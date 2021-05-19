from typing import List
from string import whitespace


def split_once(text: str, separators: str = None) -> List[str]:
    result = [text]
    seps = list(separators or whitespace)

    while seps:
        # result[-1] #this removes the parenthesis 
        # list(result[-1].find(sep) for sep in seps )
        # print(result[-1].find(x) for sep in seps )
        # min(result[-1].find(sep) for sep in seps )  
        sep = min(seps, key=lambda x: result[-1].find(x))
        result[-1:] = result[-1].split(sep, 1)
        seps.remove(sep)
    return result

