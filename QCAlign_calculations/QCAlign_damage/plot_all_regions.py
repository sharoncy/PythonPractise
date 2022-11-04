import pandas as pd
import sys
import matplotlib.pyplot as plt
import numpy as np
import glob
import math
import mod_calc_regions
import subprocess
#from mpl_toolkits.mplot3d import proj3d
import matplotlib.ticker as mtick

#The mod_calc_regions script has been imported. This script calls the calc function in mod_calc_regions and applies it to each column.

if (len(sys.argv)<3):
    print("Usage: ")
    print("python plot_all_regions.py [ input file ] [ base name ]")
    exit(1)

infile = sys.argv[1]
basename = sys.argv[2]

df = pd.read_csv(sys.argv[1], sep='\t')
columns = 0
for d in df:
    columns = len(d)-3

# assign file name. 

for i in range(0,columns-1):
    outfile = basename + "_column"+str(i+3)+".csv"
    outpng = basename + "_column"+str(i+3)+".png"
    print("Calculating column: "+str(i+3))
    mod_calc_regions.calc(infile, outfile, i+3)
 #   subprocess.call("./plot.py"),outfile + " "+outpng+" -noplot")
    subprocess.call(["python","plot.py",outfile,"-outfile="+outpng,"-noplot"])

#print(columns)




