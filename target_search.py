#!/usr/bin/python

# modules 
import os
from ciscoconfparse import CiscoConfParse                                

# get a string and a direction of advertsement
extcomm = raw_input("Enter a String: ")
direction = raw_input("import or export?: ")

# concatinate the input to form the query string
target = direction+' '+extcomm

# ennumerate the target configs
path = "/Users/dj/Desktop/All/"
dirs = os.listdir( path )

# rewcurse through the directory and locate the vrfs that are importing or 
# exporting the string and print the result
for file in dirs:
 parse = CiscoConfParse(path+file)          
 importers = parse.find_parents_w_child( "ip", target)
 if importers != []:
  print file
  print importers



