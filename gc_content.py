dna = "ATGCGATAATAG"
gc = dna.count("G") + dna.count("C")
length = len(dna)
print("DNA sequence:", dna)
print("GC bases:", gc)
print("Length:", length)
print("GC content:", (gc/length)*100,"%")