from Bio import Entrez
from Bio import SeqIO

def frmt():
    Entrez.email = "maria.dermit@qmul.ac.uk"
    ids = open("Chapter_Rosalind/frmt/rosalind_frmt.txt").read().split()
    # Fetch data from GenBank server
    handle = Entrez.efetch(db="nucleotide", id=ids, rettype="fasta")
    records = list(SeqIO.parse(handle, "fasta"))
    handle.close()
    
    # Find shortest string
    shortest_rec = min(records, key=lambda rec: len(rec.seq))
    print (shortest_rec.format("fasta"))

