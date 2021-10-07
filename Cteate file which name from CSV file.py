# -*- coding: utf-8 -*-
# -------------------------------------------------------------------
# Open and read .csv file data
# Create file and file name from .csv file data
# Created on: 2021-08-27 15:53:05
# -------------------------------------------------------------------

# Import modules.
import csv
import os

# Read CSV file. 
with open('D:\\ArcMap test\\TestReadSV.csv', newline='') as csvfile:
    line = csv.reader(csvfile)

    # Set name from CSV file and check.
    for row in line:
        outfile = str(row)
        print(eval(outfile.strip('[]')))

        # Create file on specify path.
        os.mkdir('D:\\ArcMap test\\' + eval(outfile.strip('[]')))

print('Create File Finish!')
