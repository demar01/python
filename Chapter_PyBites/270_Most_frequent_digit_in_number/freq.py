
from collections import Counter


def freq_digit(num: int) -> int:
    return int(Counter([int(d) for d in str(a)]).most_common(1)[0][0])