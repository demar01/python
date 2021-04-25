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
    return round(sum(1 for char in sequence
                     if char.upper() in ['C', 'G'])/sum(1 for char in sequence
                                                        if char.upper() in ['A', 'C', 'G', 'T'])*100, 2)