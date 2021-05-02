# -*- coding: utf-8 -*- 

"""
http://rosalind.info/problems/splc/
"""
'''
Problem
After identifying the exons and introns of an RNA string, we only need to delete the introns and concatenate the exons to form a new string ready for translation.

Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings are given in FASTA format.

Return: A protein string resulting from transcribing and translating the exons of s. (Note: Only one solution will exist for the dataset provided.)

Sample Dataset
>Rosalind_10
ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
>Rosalind_12
ATCGGTCGAA
>Rosalind_15
ATCGGTCGAGCGTGT

Sample Output
MVYIADKQHVASREAYGHMFKVCA

'''

import sys
sys.path.append("/Users/dermit01/Documents/python/Chapter_Rosalind/")
import rosalind_utils
from Bio.Seq import Seq
from Bio import SeqIO

def splc():
    recs = rosalind_utils.read_fasta("Chapter_Rosalind/splc/rosalind_splc.txt")
    seqs = [rec[1] for rec in recs]
    exon = seqs[0]
    introns = sorted(seqs[1:], key=lambda s: len(s), reverse=True)
    for intron in introns:
        exon = exon.replace(intron, "", 1)
        prot = Seq(exon).transcribe().translate()
    return prot[:-1]