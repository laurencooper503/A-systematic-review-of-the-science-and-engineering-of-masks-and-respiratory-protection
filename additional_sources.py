# -*- coding: utf-8 -*-
"""
Created on Fri May 22 21:20:44 2020
Updated on Wed May 27 15:05:24 2020

@author: Lauren Cooper and Alexa Guan

------------------------------------------------------------------------------
This is for 'additional records identified through other sources'

The copied citations were of the format:
Authors (year). Title. Journal. Type. Link

This code extracts the title from the string

"""
import csv
import re


#N95 decon sources
with open('N95DECON_bibliography.csv', newline='') as f:
    reader = csv.reader(f)
    titles = [row for row in reader]

#filter out the empty lists and delete everything before the (year). title. 
titles=[re.sub("^.*?\\)\\. ","",x[0]) for x in titles if x]
#delete everything after title. journal...
titles=[re.sub(r'\..*',"",x) for x in titles]

