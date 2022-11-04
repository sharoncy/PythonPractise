import pandas as pd
import sys
import matplotlib.pyplot as plt
import numpy as np
import glob
import math
#from mpl_toolkits.mplot3d import proj3d
import matplotlib.ticker as mtick


# python3 plot_reference_atlas_regions.py [ nutil_output_dir ] [type]”
# where type = 0 is regular bars, type=1 is pie chart

if len(sys.argv)<2:
	print("Usage: python plot.py [ input file ] [ optional parameters ]")
	print(" Options:")
	print(" -noplot: only out png, don't open plot window")
	print(" -outfile=myfile.png")
	print(" -yaxis=\"y axis custom label\"")
	print(" -default_color=(1,0,0) sets default colour to red")
	exit(1)


atlas_files = glob.glob("*.label", recursive = True)


doplot = True
outfile = 'plot.png'

typ = 0
#if (len(sys.argv)>=3):
#	typ = int(sys.argv[2])


xaxis = "Index"
yaxis = "Value"

default_color = [0,0,0]
isRainbow = 0

if (len(sys.argv)>2):
	for i in range(2,len(sys.argv)):
		org = sys.argv[i]
		s = sys.argv[i].lower()
		if (s=="-noplot"):
			doplot = False
		if ("-outfile=" in s):
			outfile = s.replace("-outfile=","")
		if ("-xaxis=" in s):
			xaxis = s.replace("-xaxis=","")
		if ("-yaxis=" in s):
			yaxis = org.replace("-yaxis=","")
		if ("-default_color=" in s):
			col = org.replace("-default_color=","")
			c = col.replace("(","").replace(")","")
			cols = c.split(",")
			default_color = [float(cols[0]),float(cols[1]),float(cols[2])]

		if ("-rainbow" in s):
			isRainbow = 1


color_map = {}

def load_labels(file):
	with open(file,'r') as f:
		line = f.readline()
		while line:
			line = f.readline().strip()
			if (not line.startswith("#")):
				line = line.replace("\"","").lower().split(",")[0]
				lst = line.split('\t')
				if len(lst)==8:
#					print(lst[7])
					color_map[lst[7]] = [float(lst[1])/256.0,float(lst[2])/256.0,float(lst[3])/256.0]


#if len(report_files)==0:
#	print("Could not find any reports to plot ")
#	exit(1)

if len(atlas_files)==0:
	print("Could not find any atlas files ")
	exit(1)


load_labels(atlas_files[0])


print("Loading...")
df = pd.read_csv(sys.argv[1], sep='\t')




dmap = {}
dmapCnt = {}
#for df in all_data:
#	od = df['Region area']
#od = df[3]

for i in range(0,len(df)):
#	print(df['structure'][i])
#	print(df[0])
	key = df['structure'][i].lower().split(",")[0]
#	print(key)
	if (df['value'][i]>=0):
#	if (df['value'][i]!=0):
		if (key not in dmap):
			dmap[key] = []
			dmapCnt[key] = 0

			dmap[key].append(df['value'][i])

xx = 0
fig, ax = plt.subplots()
xticks = []
xp = []
if (typ==0):
	fig.set_figwidth(10)
	fig.set_figheight(5)
if (typ==1):
	fig.set_figwidth(8)
	fig.set_figheight(8)

xp_colors = []
td = []
explode = []
#print(color_map.keys())
curCol = 0.0
for key in dmap:

	d=[]
	x=[]
	sx = xx
	sz = 0

	if (key in color_map):
		c = color_map[key]
	else:
		c = default_color



#	if (isRainbow):
#		xp_colors.append((curCol,0,0))
#			#print("here")
#			curCol+=0.01


	for val in dmap[key]:
		d.append(val)
		td.append(val)
		x.append(xx)
		xx = xx + 1
		sz = sz + 1
		expl = 0
		if ("visual" in key):
			expl = 0.3

		expl = val
		explode.append(expl)

		if (typ==1):
			if (isRainbow==0):
				xticks.append(key)
				xp_colors.append((c[0],c[1],c[2]))


#	print(len(dmap[key]))

	if sz>=0 and typ==0:
		if (key not in xticks):
			xticks.append(key)
			xp.append(sx + (sz)/2.0)
			xp_colors.append((c[0],c[1],c[2]))

# this is a bar chart

	if (typ==0):
		ax.bar(x,d, color=(c[0],c[1],c[2]))
		ax.set_ylabel(yaxis)
	#ax.bar_label(p1, label_type='center')

	


ticks = plt.xticks(xp, xticks,rotation = 45, fontsize=6)


for label in ax.get_xmajorticklabels():
	label.set_horizontalalignment("right")


fmt = '%.2f%%' # Format you want the ticks, e.g. '40%'
yticks = mtick.FormatStrFormatter(fmt)
ax.yaxis.set_major_formatter(yticks)

ax.xaxis.set_ticks_position('bottom') 
[t.set_color(i) for (i,t) in
	zip(xp_colors,ax.xaxis.get_ticklabels())]






avg = sum(td)/len(td)
sigma = 0.0
for i in td:
	sigma = sigma + (avg-i)*(avg-i)/(len(td)-1)


sigma = math.sqrt(sigma)
#print(str(avg) + " ," +str(sigma))
#plt.ylim((avg+sigma*3),0)

#for ticklabel, tickcolor in zip(plt.gca().get_xticklabels(), xp_colors):
#   ticklabel.set_color(tickcolor)

if typ==0:
	plt.tight_layout()
        
plt.savefig(outfile,dpi=180)
if doplot:
	plt.show()
	plt.draw()
