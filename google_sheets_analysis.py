# -*- coding: utf-8 -*-
"""
Created on Wed May 27 15:05:24 2020

@author: Lauren Cooper and Alexa Guan

------------------------------------------------------------------------------
This file counts the final number of papers included in the review (marked Y),
after filtering for eligibility
"""
import pandas as pd


df=pd.read_csv('Data/Keywords_for_review.csv',encoding = "ISO-8859-1", engine='python')
print(df['Included in PRISMA?'].value_counts())
