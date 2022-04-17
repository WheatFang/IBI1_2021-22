#for counting the number of fragments by enzyme
seq = 'ATGCAATCGACTACGTCAATCGAGGGCC'
n = 0
for i in range (14):#we can obtain 14 (len(seq)-4) times
    fn = seq[i:i+5]#Five Nucleotide(FN)sequences were obtained successively
    if fn == "GAATC":
        n= n+1#n reprecents the number of occurrences of a particular sequence
    else:
        n = n
print(n)
        
