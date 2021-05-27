CM_IN_RATIO = 2.54


def convert(value: float, fmt: str) -> float:
    """Converts the value to the designated format.
    :param value: The value to be converted must be numeric or raise a TypeError
    :param fmt: String indicating format to convert to
    :return: Float rounded to 4 decimal places after conversion
    """
    if not isinstance(value, (int, float)):
        raise TypeError

    if fmt.lower() not in ("cm", "in"):
        raise ValueError

    return round(value * CM_IN_RATIO if fmt.lower() == "cm"
                 else value / CM_IN_RATIO, 4)


#two if for checking and raising errors cuz they are independent entries. Had they been part of a list, check and raise error using a loop (see pybite 241)
# interesting see test_ for testing raising errors
