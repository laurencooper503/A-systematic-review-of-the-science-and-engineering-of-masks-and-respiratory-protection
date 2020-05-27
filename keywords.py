# -*- coding: utf-8 -*-
"""
Created on Fri May 22 21:20:44 2020
Updated on Wed May 27 15:05:24 2020

@author: Lauren Cooper and Alexa Guan
------------------------------------------------------------------------------
Here, the csv files for all of the titles found will be analyzed and duplicates
will be removed
"""

import pandas as pd
from functools import reduce
import operator
from additional_sources import titles


#importing the unfiltered data and returning the titles
def addcsv(filename,input_list):
    #add data to dataframe
    tempdf=pd.read_csv(filename,encoding = "ISO-8859-1", engine='python')
    #only add titles to list and return the list of titles
    return input_list.append(tempdf["Title"].tolist())


#we have all of the unfiltered titles from Pubmed and Google Scholar stored in 
#csv files. add titles from each of the csv files to source_titles
source_titles=[]
addcsv('Data/PUBMED_csv-homemadema-set.csv',source_titles)
addcsv('Data/PUBMED_csv-maskfiltra-set.csv',source_titles)
addcsv('Data/PUBMED_csv-repiratorr-set.csv',source_titles)
addcsv('Data/GOOGLESCHOLAR_cyclicflowFFR.csv',source_titles)
addcsv('Data/GOOGLESCHOLAR_fomitepotentialFFR.csv',source_titles)
addcsv('Data/GOOGLESCHOLAR_survivabilityFFR.csv',source_titles)
addcsv('Data/GOOGLESCHOLAR_transferefficiencyFFR.csv',source_titles)
addcsv('Data/GOOGLESCHOLAR_uvgidecontaminationFFR.csv',source_titles)


#flatten list and count records. This only is for counting the number
#found through databases and NOT through additional sources
database_titles=reduce(operator.concat,source_titles)
information={'Records found through database searching':[len(database_titles)]}

#add references from CDC sources
addcsv('Data/CDC_references.csv',source_titles)

#flatten list and append titles from N95 decon
source_titles=reduce(operator.concat,source_titles)
source_titles.extend(titles)



""""FINAL INFORMATION: COUNTS"""
#store number of titles
information.update({'Total number':[len(source_titles)]})
#delete duplicates
source_titles=set(source_titles)
#count remaining
information.update({'Delete duplicates':[len(source_titles)]})
print(information)
