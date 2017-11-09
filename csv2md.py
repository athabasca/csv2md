#!/usr/bin/python

"""
csv2md
======
Convert a .csv file into a markdown table.

Usage: python csv2md.py [-i infile.csv] [-o outfile.md]

If either infile or outfile are unspecified, csv2md reads from stdin or prints to stdout. csv2md assumes the first row of the .csv is a header.

TODO: add option to specify alignment of columns. Currently all columns are centred.
"""
from sys import stdin, stdout, exit
from optparse import OptionParser
import csv

parser = OptionParser()
parser.add_option("-i", dest="infile", default="stdin", help="input .csv file, default=stdin")
parser.add_option("-o", dest="outfile", default="stdout", help="output .md file, default=stdout")

(opts, args) = parser.parse_args()

if opts.infile is "stdin":
    infile = stdin
else:
    try:
        infile = open(opts.infile, 'rb')
    except Exception as e:
        exit("Could not open {}: {}".format(opts.infile, e))

if opts.outfile is "stdout":
    outfile = stdout
else:
    try:
        outfile = open(opts.outfile, 'wt')
    except Exception as e:
        infile.close()
        exit("Could not open {}: {}".format(opts.outfile, e))

reader = csv.reader(infile)
try:
    header = 0
    for row in reader:
        for cell in row[:-1]:
            outfile.write(cell + " | ")
        outfile.write(row[-1] + "\n")
        if not header:
            outfile.write(":---:|" * (len(row)-1) + ":---:\n")
            header = 1
except csv.Error as e:
    infile.close()
    outfile.close()
    exit("file {}, line {}: {}".format(opts.infile, reader.line_num, e))

infile.close()
outfile.close()
