# Python lesson about renaming image files
# also covers list comprehension

# import packages

from glob import glob # package for getting path, for navigating file directory 
import shutil # package for accessing bash commands for moving files
import os # package for windows operating system, can use os.sep (os separator) and os.rename
import pandas as pd # package for dataframes (excel in .py files)

# declare variables: identify the files

png_path = r"C:\users\sharoncy\Documents\programming\Python_club\PythonClub_Ingrid" # declare the folder (r means to ignore backslashes)
png_files = glob(png_path + "/*.png") # all the png files in the png_path # specify the png in the folder

# print out the png files in the specified directory

#print(len(png_files))
#print(png_files[0])

# To rename need to extract the file name from the path

first_file_name = png_files[0].split(os.sep)[-1] # separate the path for first png at last double backslash
#print(first_file_name)

# this is a list comprehension/ for loop
all_png_names = [i.split(os.sep)[-1] for i in png_files]
#print(all_png_names)

# alternative method for creating all_png_names

alternative_png_names = [os.path.basename(i) for i in png_files]
#print(alternative_png_names)

# compare that the names are the same
#print(list(zip(all_png_names, alternative_png_names)))

# edit file names

png_names_edited = [i.split("BDA")[1] for i in alternative_png_names]
#print(png_names_edited)

png_names_edited = ["New_name" + i for i in png_names_edited]
#print(png_names_edited)

# assign the new name to the full path
new_png_filenames = [png_path + os.sep + i for i in png_names_edited]
#print(new_png_filenames)

#print(list(zip(png_files, png_names_edited)))

for old, new in zip(png_files, png_names_edited):
    print(f'renaming{old} to :\n{new}')
    shutil.copy(old, new) # copy image at old path to new path (keep original)

df = pd.DataFrame({"oldPNGs": png_files, "newPNGs": png_names_edited})
df.to_csv("old_new_png_names.csv")
