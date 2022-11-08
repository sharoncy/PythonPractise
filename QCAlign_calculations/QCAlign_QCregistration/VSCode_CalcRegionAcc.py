import pandas as pd
import pydoc as doc
import matplotlib.pyplot as plt
from pathlib import Path

def CalcRegionAcc(infile, outfile):
    
    df =pd.read_csv(infile, sep="\t")
    region_id = list(df.iloc[::5,0])
    region_name = list(df.iloc[::5,1])
    region_accuracy = list(df.iloc[1::5,3])
    region_inaccuracy = list(df.iloc[2::5,3])
    combined_list = list(zip(region_id,region_name,region_accuracy,region_inaccuracy))
    new_combined_list = [(a, b, c, d) for a, b, c, d in combined_list if c != 0]

    new_region_name = []
    new_region_id = []
    accuracy_score = []

    for a,b,c,d in new_combined_list:
        new_region_id.append(a)
        new_region_name.append(b)
        accuracy_score.append(c / (c + d))

    dict = {'Region ID': new_region_id, 'Region': new_region_name, 'Perc accuracy': accuracy_score}  
    df = pd.DataFrame(dict) 
    df.to_csv(outfile, index=False)

CalcRegionAcc("AJ_QControl_Thionine_stats_SY.txt", "AJ_SY_accuracy_score_final.csv")