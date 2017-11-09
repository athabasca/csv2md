# csv2md

Convert a .csv file into a markdown table.

Usage: python csv2md.py [-i infile.csv] [-o outfile.md]

If either infile or outfile are unspecified, csv2md reads from stdin or prints to stdout. csv2md assumes the first row of the .csv is a header.

TODO: add option to specify alignment of columns. Currently all columns are centred.

