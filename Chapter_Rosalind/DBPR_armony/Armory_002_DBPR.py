from Bio import ExPASy
from Bio import SwissProt

#See the docs https://biopython.org/docs/1.75/api/Bio.SwissProt.html


def getgo(id):
	handle = ExPASy.get_sprot_raw(id)
	record = SwissProt.read(handle)
	go = [r[2].split(":")[1] for r in record.cross_references if r[0] == "GO" and r[2].startswith('P')]
	print "\n".join(go)

# Test
getgo("Q65N65")


# id="Q5SLP9"
# handle = ExPASy.get_sprot_raw(id) #<_io.TextIOWrapper encoding='UTF-8'>
# record = SwissProt.read(handle) #<Bio.SwissProt.Record object at 0x109873be0>

# [r for r in record.cross_references]
# go=([r[2].split(":")[1] for r in record.cross_references if r[0] == "GO" and r[2].startswith('P')])


#https://github.com/Shivi91/Rosalind-1/blob/master/Armory_002_DBPR.py
#https://github.com/adelq/rosalind/blob/master/DBPR.py