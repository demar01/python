import sys
sys.path.append("/Users/dermit01/Documents/python/Chapter_Rosalind/")
import rosalind_utils

def subs():
    s, t = open("Chapter_Rosalind/dna_motif/rosalind_subs.txt").readlines()
    t = t.strip()
    idx = -1
    while True:
        try:
            idx = s.index(t, idx+1)
            print (idx+1)
        except:
            break
    print ('')

subs()