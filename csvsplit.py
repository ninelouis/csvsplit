# Feb 2, 2016
# usage
# 1st argument (string) = input file
# 2nd argument (int)    = column to be used as splitter

#-*-coding: utf-8 -*-
import csv
import sys
import os

# Specifies input CSV file
infile = sys.argv[1]

# Specifies the column that will be a splitter
splitter_col = int(sys.argv[2])

# Specifies output folder name
output_folder = "out"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

with open(infile,'r') as fin:   
	
	# save header row for using later
	header_row = fin.readline()
	
	# DEBUG: print(headerrow)
	for row in csv.reader(fin, delimiter=','):
		
		# naming output file
		outfile = output_folder + "/" + row[splitter_col] + ".csv"
		
		# create file if it does not exist
		if not os.path.exists(outfile):
			# also drop in the header row
			with open(outfile, 'w+b') as fout:
				fout.write(header_row)

		# drop in the content, line by line
		with open(outfile, 'a+') as fout:
			csv_writer = csv.writer(fout)
			csv_writer.writerow(row)
