import csv
from pydoc import doc
import sys
import matplotlib.pyplot as plt

# sys.argv, list of input from the command line

# defining a function called calc that takes in three input parameters: a QCAlign file; the output file name; the column to analyse .
# create empty arrays.
def calc(infile, outfile, column):
    i = 0
    j = 0
    x = []
    y = []
    rawData = []
    rawDataID = []
    structure = []

#- read in the QCAlign file. Iterate through the rows...

    i = 0
    total_total = 0
    total_damaged = 0
    clear_total = 0
    clear_damaged = 0
    with open(infile) as data:                                                                                          
        data_reader = csv.reader(data, delimiter='\t')

        for d in data_reader:
            if (i==1):
                if d[column]!='':
                    total_total = int(d[column])                

            if (i==5):
                if d[column]!='':
                    total_damaged = int(d[column])                

            if (i==6):
                if d[column]!='':
                    clear_total = int(d[column])                

            if (i==10):
                if d[column]!='':
                    clear_damaged = int(d[column])                


            exists = 0
            if ((i>0 and i<6) or (i>10)):
                if d[column]!='':                
                    rawData.append(int(d[column]))
                    exists = 1
                else:
  #                  rawData.append(0)
                    exists = 0

                if d[0]!='' and exists==1:
                    rawDataID.append(int(d[0]))
#                else:
 #                   rawDataID.append(-1)
            i+=1
            if (i%5==0 and i!=10 and exists==1):
                structure.append(d[1])

 

# assign length of the rawData array divided by 5 to the "count" variable
    count = int(len(rawData)/5)

# define 3 empty arrays
# the len() function counts the no. of items in an object: a string, a tuple, a dictionary, list, sets, array, etc.
# for i in range 0 to length of custom hierarchy (what is counted here?)
# append 0 to the acc, inacc and uncert arrays, and assign no. to the x array (keep count?)
# for i in range 0 to 1/5th of length
# position = no. that goes up by 5
# id = ID in the rawDataID array located at every 5th position
# for j in range 0 to length of cust, if the ID in the j position of the custom hierarchy
# 

    total = []
    acc = []
    inacc = []
    uncert = []
    damaged = []

    for i in range(0,count):
        acc.append(0)
        inacc.append(0)
        uncert.append(0)
        total.append(0)
        damaged.append(0)
        x.append(i)
    
    for i in range(0,count):
        pos = i*5
        #id[i] = rawDataID[pos]
        total[i]=rawData[pos]
        acc[i]=rawData[pos+1]
        inacc[i]=rawData[pos+2]
        uncert[i]=rawData[pos+3]
        damaged[i]=rawData[pos+4]
        #print(rawData[pos+5])




    for i in range(0,count):
        A = damaged[i]
        tot = A+total[i] + acc[i] + inacc[i] + uncert[i]
        fy = 0.0
        if (tot!=0):
            fy = A/(tot)*100

        y.append(fy)
        # number of decimal points
#        print(structure[i] + " " + "{:.3f}".format(fy)+"%")


#    print(clear_damaged)

#    Special case: 

    A = total_damaged-clear_damaged
    B = (total_total + total_damaged) - (clear_total + clear_damaged)

    fy = 0.0
    if (B!=0):
        fy = A/B
    y[0] = fy*100.0

#    print(fy)

    # special case for total:
    

    # write file

    f = open(outfile,"w+")
    f.write("index\tid\tstructure\tvalue\n")
    for i in range(0,count):
        f.write(str(i) + "\t" + str(rawDataID[i])+ "\t" + structure[i]+"\t" +str(y[i]) + "\n")  






    f.close()

