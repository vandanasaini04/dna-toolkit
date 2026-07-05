dna = "ATGCGATAATAG"
print("codons:")
for i in range(0, len(dna), 3):
  codon = dna[i:i+3]
  print(codon)