#to calculate each nucleotide content in a DNA sequence
def nu_con_cal(D):
    SEQUENCE = sequence.upper()  # Convert all letters to uppercase
    total = len(SEQUENCE)  # Count the total number of nucleotides
    A = SEQUENCE.count("A")  # Count how many of each nucleotide there are
    T = SEQUENCE.count("T")
    G = SEQUENCE.count("G")
    C = SEQUENCE.count("C")
    CA = A/total  # calculate the percenatge of nucleotidrs in the sequence
    CT = T/total
    CG = G/total
    CC = C/total
    return CA,CT,CG,CC
sequence = input("please input a DNA sequence:")
answer = nu_con_cal(sequence)
print("content of A =",answer[0],"content of T =",answer[1],"content of G =",answer[2],"content of C =",answer[3])

    
    
    
