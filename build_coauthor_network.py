'''
This code is meant to build a coauthor network using the COVID19 paper data set provided by the CDC 
'''

import pandas as pd 
import numpy as np 
import string 
import networkx as nx
import matplotlib.pyplot as plt 

#first thing's first --> we want to read in the excel file and isolate the authors column 
data = pd.read_excel(r'COVID19_Sample_Dataset_1.xlsx')
df = pd.DataFrame(data, columns = ['Author'])

#data cleaning --> should we clean as we go? Build author dictionary --> [[P1author_1, P1author_2][P2author_1, ...][ ]]
coauthor_groups = df.values.tolist() 

#let's do some data cleaning, then, since each list member is a string, we can parse using semicolon delimeter 
#Once we have individual authors stored by paper, we can create a dictionary of unique authors, nodes for each, then build edges between unique nodes based on coauthorship 

#print(coauthor_groups)

#inefficient, but will work for now --> maybe use lambda later 
for coauthors in coauthor_groups:
    if isinstance(coauthors[0], str) != True: 
        coauthor_groups.remove(coauthors) 
    else: 
        for char in coauthors: 
            if char not in string.printable: 
                coauthor_groups.remove(coauthors) 

#the keys will be the authors, and the values will be coauthors --> don't need to worry about redundant edges, since networkx takes care of redundancy automatically 
author_dict = {}  

#again, inefficient, but will suffice for now --> structured for readability
#traversing list of coauthor_groups for each paper 
i = 0 
for coauthor_group in coauthor_groups:
    #for each coauthor group (1 coauthor goru <--> 1 paper), convert group to list of names   
    coauthor_names_unclean = coauthor_group[0].split(';')
    #for scrubbed names   
    coauthor_group_members = []

    for coauthor in coauthor_names_unclean:
        #adding each scrupped coauthor name to the coauthor_group_members list 
        coauthor_group_members.append(coauthor.strip())
    
    #print("\n\nGROUP MEMBERS: ", coauthor_group_members)
 
    coauthor_dict = {}
    for author in coauthor_group_members:
        coauthor_dict.update({author: {}})

    #The problem here is that only cliques will be retained. The logic is more subtle. If an author isn't yet a key, 
    #then we want to add it to the dictionary. If it is already a key, then we just want to update it's dictionary with the 
    #neighbors it doesn't already have in its dictionary. 
    for main_author in coauthor_group_members:
        if main_author not in author_dict.keys(): 
            author_dict.update({main_author: coauthor_dict})
        else: 
            #if the author is already a key in the author_dict that means that it presumably already has a coauthor dictionary as 
            #its value. More specifically, it is already a part of a clique. Here is where we build edges between cliques
            print("CONNECTOR FOUND: ", main_author)
            for coauthor in coauthor_group_members:
                author_dict.get(main_author).update({coauthor: {}}) #getting the existing coauthor_dict and adding edges to authors in current coauthor list 

    
    #print(author_dict)
    i += 1 
    if i == 200: 
        break

coauthor_network = nx.from_dict_of_dicts(author_dict)
nx.draw(coauthor_network, with_labels = True, node_size = 50)
plt.show() 
#Note that we still have to fix semicolon delimiters
#motherfucker, can only build nx graphs from dictionary of dictionaries 
