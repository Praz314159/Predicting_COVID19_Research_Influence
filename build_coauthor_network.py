'''
This code is meant to build a coauthor network using the COVID19 paper data set provided by the CDC 
'''

import pandas as pd 
import numpy as np 
import string 
#import networkx 


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

#building dictionary 
#coauthor_list_1 = coauthor_groups[0][0] 
#print(coauthor_list_1) 

#the keys will be the authors, and the values will be coauthors --> don't need to worry about redundant edges, since networkx takes care of redundancy automatically 
author_dict = {}  

#again, inefficient, but will suffice for now --> structured for readability 
for coauthors in coauthor_groups: 
    author_names_unclean = coauthors[0].split(';')
    author_list = []
    #print(author_list)
    for author in author_names_unclean:
        #get rid of spaces at beginning and end of author name 
        author_list.append(author.strip())  

        '''
        print(author)
        print(type(author))
        print(author == author_list[0])
        print(author in author_list) 
        #author is in the author_list, so why 
        '''

        if author not in author_dict.keys():
            print("AUTHOR LIST: ", author_list)
            print("AUTHOR: ", author) 
            #coauthor_list = author_list.remove(author)
            author_dict.update({author: author_list})
        else: #we only want the coauthors that are not already in the value --> author already in dict 
            coauthor_list = author_dict.get(author) #getting existing coauthor list for author in question 
            candidate_coauthor_additions = coauthors.remove(author) 
            for candidate in candidate_coauthor_additions: 
                if candidate not in coauthor_list: 
                    coauthor_list.append(candidate)
                    author_dict.update({author: coauthor_list})
            
print(author_dict)



#Network building --> we want edges between each of the coathors of a paper 







