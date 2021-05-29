def is_armstrong(n: int) -> bool:
    return n == sum(int(c) ** len(str(n)) for c in str(n))


# [int(c) ** len(str(153)) for  c in str(153)]
# sum(int(c) ** len(str(153)) for  c in str(153))