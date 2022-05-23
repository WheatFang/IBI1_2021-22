edit_distance =  0  # set initial distance as zero
match = 0  #set the number of identical amino acids in these two sequences
not_match = 0  #set the number of unidentical amino acids in these two sequences
import pandas as pd
blosum = pd.read_excel('BLOSUM.xlsx')
blosum62 = 'ARNDCQEGHILKMFPSTWYVBZX'
human_string = []
mouse_string = []
random_string = []
import re
human = open('DLX5_human.fa','r')
human_read = human.read()
human_sequence = str(re.findall(r'MTG.+',human_read))
mouse = open("DLX5_mouse.fa",'r')
mouse_read = mouse.read()
mouse_sequence = str(re.findall(r'MTG.+',mouse_read))
random = open('RandomSeq.fa')
random_read = random.read()
random_sequence = str(re.findall(r'GDY.+',random_read))
# HUMAN SEQUENCE between MOUSE SEQUENCE
for i in range(2,len(mouse_sequence)-2):
    human_amino_acid = human_sequence[i]
    mouse_amino_acid = mouse_sequence[i]
    if mouse_sequence[i] != human_sequence[i]:
       edit_distance += 1  # add a score 1 if  amino edit are different
       not_match += 1
    else:
       match += 1
    for i in range(len(blosum62)):
        if blosum62[i] == human_amino_acid:
            human_string.append(str(i+1))
    for i in range(len(blosum62)):
        if blosum62[i] == mouse_amino_acid:
            mouse_string.append(str(i+1))
identical_percentage = match/len(human_sequence)
print("edit distance is",edit_distance,"the identical percentage between human and mouse sequence is",identical_percentage)
score = 0
for i in range(len(human_string)):
    score = score + blosum.iloc[int(human_string[i])-1,int(mouse_string[i])]
print("the BLOSUM62 score of the comparison between human and mouse sequence is",score)
# MOUSE SEQUENCE between RANDOM SEQUENCE
match = 0
for i in range(2,len(mouse_sequence)-2):
    random_amino_acid = random_sequence[i]
    mouse_amino_acid = mouse_sequence[i]
    if mouse_sequence[i] != random_sequence[i]:
       edit_distance += 1  # add a score 1 if  amino edit are different
       not_match += 1
    else:
       match += 1
    for i in range(len(blosum62)):
        if blosum62[i] == random_amino_acid:
            random_string.append(str(i+1))
    for i in range(len(blosum62)):
        if blosum62[i] == mouse_amino_acid:
            mouse_string.append(str(i+1))
identical_percentage = match/len(random_sequence)
print("edit distance is",edit_distance,"the identical percentage between random and mouse sequence is",identical_percentage)
score = 0
for i in range(len(random_string)):
    score = score + blosum.iloc[int(random_string[i])-1,int(mouse_string[i])]
print("the BLOSUM62 score of the comparison between random and mouse sequence is",score)
#RANDOM SEQUENCE and HUMAN SEQUENCE
match = 0
for i in range(2,len(human_sequence)-2):
    random_amino_acid = random_sequence[i]
    human_amino_acid = human_sequence[i]
    if human_sequence[i] != random_sequence[i]:
       edit_distance += 1  # add a score 1 if  amino edit are different
       not_match += 1
    else:
       match += 1
    for i in range(len(blosum62)):
        if blosum62[i] == random_amino_acid:
            random_string.append(str(i+1))
    for i in range(len(blosum62)):
        if blosum62[i] ==human_amino_acid:
            human_string.append(str(i+1))
identical_percentage = match/len(random_sequence)
print("edit distance is",edit_distance,"the identical percentage between random and human sequence is",identical_percentage)
score = 0
for i in range(len(random_string)):
    score = score + blosum.iloc[int(random_string[i])-1,int(human_string[i])]
print("the BLOSUM62 score of the comparison between random and human sequence is",score)












