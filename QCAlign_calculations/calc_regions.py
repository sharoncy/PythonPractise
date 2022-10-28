import csv
from pydoc import doc
import sys
import matplotlib.pyplot as plt
import mod_calc_regions

# PROGRAM STARTS HERE

if len(sys.argv)!=4:
    print("Usage:")
    print("python plot.py [input file] [output file (csv file)] [column]")
    exit(1)


mod_calc_regions.calc(sys.argv[1], sys.argv[2], int(sys.argv[3]))


