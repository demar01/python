
import math
def round_up_or_down (transactions :list, up=True):
    return [ceil(item) if up else floor(item) for item in transactions]

def round_up_or_down (transactions :list, up=True) -> int:
    if up:
        return [math.ceil(float(x)) for x in transactions]
    else:
        return [math.floor(float(x)) for x in transactions]