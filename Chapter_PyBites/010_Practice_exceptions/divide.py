def positive_divide(num, denom):
    try:
        if num/denom <0:
            raise ValueError
        return num/denom
    except ZeroDivisionError:
        return 0  
    except TypeError:
        raise     


