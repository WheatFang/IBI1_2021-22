# the user input a filenme as the new fasts fila to be written to
import re
import os
data = open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", 'r')
data_read = data.read()  # read the file
ls_genenames = []  # list to obtain all the gene names
ls_sequences = []  # list to obtain all the gene sequences
number_of_gene = [] # store position of sequences taht can be cut
number_of_cut = [] # store the number of fragments of DNA cut
genenames = re.findall(r'gene:(.+?\s)', data_read)  # obtain all the gene names
data_new = data_read.replace("\n","") # make sequence in a single line
data_1 = data_new.split(">")  # make the information about genes separated
for i in range(len(data_1)):
    sequence = re.findall(r'[ATCG]{10,}',data_1[i])
    ls_sequences.append(sequence) # get the sequences for all genes
for i in range(len(ls_sequences)):
    c = re.findall('GAATTC',str(ls_sequences[i])) # find " GAATTC" in the whole sequence
    if len(c) != 0:
        number_of_gene.append(str(i)) # number_of_gene stores the number of genes that can be cleaved by the enzyme
        number_of_cut.append(str(len(c)+1))
# create a new list to store all the information about genes that can be cut by the anzyme
final_list = []
for i in range(len(number_of_gene)):
    position = int(number_of_gene[i])
    final_list.append(genenames[position]) # stores the name of genes
    sequence_string1 = str(ls_sequences[position]) # list only appends string
    sequence_string2 = sequence_string1[2:len(sequence_string1)-4]
    final_list.append(number_of_cut[i]) # store the legth of genes
    final_list.append("\n")
    final_list.append(sequence_string2) # store the sequence
    final_list.append(" ")
    final_list.append("\n")
with open("C:/cygwin64/home/Wheat‘s Computer/IBI1_2021-22/Practical8/Fragments.fa","w") as newfile:
    newfile.writelines(final_list) # put the information into the new fa file
with open("C:/cygwin64/home/Wheat‘s Computer/IBI1_2021-22/Practical8/Fragments.fa","r") as newfile:
    newfile_read = newfile.read() # read file
    print(newfile_read)