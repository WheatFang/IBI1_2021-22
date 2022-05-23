#find GO terms in an XML file
#to get all the elements from the file go_obo:
from xml.dom.minidom import parse
import xml.dom.minidom
import numpy as np
import re
import matplotlib.pyplot as plt
DOMdo_obo = xml.dom.minidom.parse("go_obo.xml") # open the file
collection= DOMdo_obo.documentElement
list_term = collection.getElementsByTagName("term")
print('the total number of terms currently recorded in the Gene Ontology:', len(list_term)) # to show the total number of terms
print(list_term[1])


def getchild(term): #create a new function to obatain the childnodes for each "childnodes" of the term
    childnodes = 0
    for child in childnode_directory[term]:
        childnodes += getchild(child)
    return childnodes+1 # includes the top childnode itself
childnode_directory = {}
total_list =[] # store the number of childnodes across all terms
translation_list = [] # store the number of childnodes across all terms associated with ”translation“
for term in list_term:
    id = term.getElementsByTagName("id")[0].childNodes[0].data
    childnode_directory[id] = []
    for child in term.getElementsByTagName('is_a'):
        childnode_directory[id].append(child.childNodes[0].data)
for term in list_term:
    id = term.getElementsByTagName("id")[0].childNodes[0].data
    childnodes = getchild(term.getElementsByTagName('id')[0].childNodes[0].data)# use the function getchilds to get the number of childNodes across all terms
    total_list.append(childnodes-1) # store the total number of childNodes across all terms
    term_def = term.getElementsByTagName('def')
    def_str = term_def[0].getElementsByTagName('defstr')[0].childNodes[0].data
    if 'translation' in def_str:
        translation_list.append(childnodes)
# draw a chart describing the distribution of the number of childNodes across terms
plt.boxplot(total_list)
plt.title("The distribution of child nodes across terms")
plt.ylabel("the number of child nodes")
plt.show()

# draw a chart describing the distribution of the number of childNodes associated with ' translation'
plt.boxplot(translation_list)
plt.title("The distribution of child nodes across terms associated with translation")
plt.ylabel("the number of child nodes of all terms associated with translation")
plt.show()
#compare the average number of child codes
# the number of childnodes are stored as string in a list
m = 0
for i in range(len(list_term)):
    m = m + int(total_list[i]) # m is the all number of childnodes across all terms
average_all = m/len(list_term)
print(average_all)
n = 0
for i in range(len(translation_list)):
    n = n+ int(translation_list[i]) # m is the all number of childnodes across all terms assiociated with "translation"
average_translation = n /len(translation_list)
print(average_translation)
if average_all > average_translation:
    print("The translation terms contain, on average, have a smaller number of childnodes than the overall Gene Ontology." )
elif average_all < average_translation:
    print( "The translation terms contain, on average, have a greater number of childnodes than the overall Gene Ontology." )
else:
    print( "The translation terms contain, on average, is the same as the overall Gene Ontology." )