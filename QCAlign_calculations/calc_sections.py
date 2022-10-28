import csv
from pydoc import doc
import sys
import matplotlib.pyplot as plt

# sys.argv, list of input from the command line

# defining a function called calc that takes in two input parameters: an input file from QCAlign and the name of the output file.
# create empty arrays.
def calc(infile, outfile):
    i = 0
    x = []
    y = []
    rawData = []
    rawDataID = []
    structure = []

# define that the data is always the infile.
# assign the data to data_reader

    i = 0
    with open(infile) as data:                                                                                          
        data_reader = csv.reader(data, delimiter='\t')
        header = []
        total_total = []
        total_damaged = []
        clear_damaged = []
        clear_total = []
        count = 0

#loop through each row in the data and perform a different function depending on the row number.

        for d in data_reader:
            
            if (i==0):
                header = d
                count = len(d)
            if (i==1):
                for j in range(3,count):
                    total_total.append(float(d[j]))
            if (i==5):
                for j in range(3,count):
                    total_damaged.append(float(d[j]))

            if (i==6):
                for j in range(3,count):
                    clear_total.append(float(d[j]))
            if (i==10):
                for j in range(3,count):
                    clear_damaged.append(float(d[j]))
            i+=1

# create the output file: add values separated by tabs. 

    f = open(outfile,"w+")
    f.write("index\tid\tstructure\tvalue\n")
    count-=3
    for i in range(0,count):
        fy = 0.0
        A = total_damaged[i] - clear_damaged[i]
        B = (total_total[i] + total_damaged[i]) - (clear_total[i] + clear_damaged[i]) 
        if (B!=0):
            fy = A/B*100           

#        fy = damaged[i]/tot*100
        f.write(str(i) + "\t" + "0"+ "\t" + header[i+3]+"\t" +str(fy) + "\n")  



    f.close()


if len(sys.argv)!=3:
    print("Usage:")
    print("python plot.py [input file] [output file]")
    exit(1)

# perform calculation

calc(sys.argv[1], sys.argv[2])

