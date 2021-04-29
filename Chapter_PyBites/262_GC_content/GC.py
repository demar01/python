from collections import Counter

sequence="ACGTAAAA"
def calculate_gc_content(sequence):
    """
    Receives a DNA sequence (A, G, C, or T)
    Returns the percentage of GC content (rounded to the last two digits)
    """
    sequence.count('C|G')/sequence.count('C|G|A|T')

def calculate_gc_content(sequence):
    """
    Receives a DNA sequence (A, G, C, or T)
    Returns the percentage of GC content (rounded to the last two digits)
    """
    c = Counter(sequence.upper())
    res = (c["G"] + c["C"]) / (c["A"] + c["G"] + c["C"] + c["T"]) * 100
    return round(res, 2)