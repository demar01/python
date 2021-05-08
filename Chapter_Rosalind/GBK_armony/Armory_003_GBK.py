
from Bio import Entrez

def genbank(genus, dtstart, dtend):
	Entrez.email = "adelq@sas.upenn.edu"
	term = '%s[Organism] AND (%s[Publication Date] : %s[Publication Date])' % (genus, dtstart, dtend) #'Drosophila[Organism] AND (2003/7/25[Publication Date] : 2005/12/27[Publication Date])' 
	handle = Entrez.esearch(db="nucleotide", term=term) #<http.client.HTTPResponse object at 0x1098c7610>
	record = Entrez.read(handle) #<class 'Bio.Entrez.Parser.DictionaryElement'>
	return record["Count"]

# Tests
print (genbank("Drosophila", "2019/12/29", "2020/12/27"))
print (genbank("Human", "2019/12/29", "2020/12/27"))