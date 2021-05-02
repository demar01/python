# -*- coding: utf-8 -*- 

"""
Given two strings s and t of equal length, the Hamming distance between s and t,
denoted dH(s,t), is the number of corresponding symbols that differ in s and
t. See Figure 2.
Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
Return: The Hamming distance dH(s,t).
Sample Dataset
GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT
Sample Output
7
"""

def hamming_distance(s,t):
    """Hamming distance"""
    return sum([1 if si!=ti else 0 for si,ti in zip(s,t)])

def hamm():
    s,t = open("Chapter_Rosalind/hamm/rosalind_hamm.txt").readlines()
    print (hamming_distance(s,t))


hamm()