#for counting the number of fragments by enzyme
import re
seq = 'ATGCAATCGACTACGTCAATCGAGGGCC'
n = re.findall('GAATTC',seq) # obtain the cut ’GAATTC‘ and store them in a set
print(len(n)+1) # the length of the set pus 1 is the number of fragments that can be cut by the enzyme
        
