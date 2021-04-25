from Bio.SeqUtils.ProtParam import ProteinAnalysis
X = ProteinAnalysis("MAEGEITTFTALTEKFNLPPGNYKKPKLLYCSNGGHFLRILPDGTVDGT"
                    "RDRSDQHIQLQLSAESVGEVYIKSTETGQYLAMDTSGLLYGSQTPSEEC"
                    "LFLERLEENHYNTYTSKKHAEKNWFVGLKKNGSCKRGPRTHYGQKAILF"
                    "LPLPV")

print(X.count_amino_acids())
print(X.count_amino_acids()['A'])
print("%0.2f" % X.get_amino_acids_percent()['A']) #The return value is cached in self.amino_acids_percent.
print("%0.2f" % X.molecular_weight())