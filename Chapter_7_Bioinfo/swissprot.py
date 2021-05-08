# This code is part of the Biopython distribution and governed by its
# license.  Please see the LICENSE file that should have been included
# as part of this package.
#

"""Example of connecting with exPASy and parsing SwissProt records."""

# biopython

from Bio import ExPASy, SwissProt

# 'O23729', 'O23730', 'O23731', Chalcone synthases from Orchid

ids = ["O23729", "O23730", "O23731"]

for id in ids:
    #First, we grab the records and get back a handle to a raw text record (no HTML to mess with!)
    handle = ExPASy.get_sprot_raw(id)
    try:
        record = SwissProt.read(handle)
    except ValueError:    
        print("WARNING: Accession %s not found" % ids)
    #We can the use Bio.SwissProt.read to pull out the Swiss-Prot record, or Bio.SeqIO.read to get a SeqRecord
    print("description: %s" % record.description)
    for ref in record.references:
        print("authors: %s" % ref.authors)
        print("title: %s" % ref.title)
    
    print("classification: %s" % record.organism_classification)
    print("")
