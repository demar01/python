#https://github.com/srinivasramachandran/Anschutz_python/blob/master/Module8/Module_8_STARRseq.ipynb

# Reading the wiggle files, which have the STARR-seq read densities for every 10 bp in chromosome 3L. 
def readwig (inFile):
      wig=open(inFile, 'r' )
      val={}
      for line in wig:
            lineL = line.split()
            if "chr" in lineL[1]:
                  cj=lineL[1]
                  chrom=cj[9:]
                  print(chrom)
                  val.setdefault(chrom,{})
            elif "rack" not in line:
                  pos=int(lineL[0])
                  val[chrom][pos] = float(lineL[1])
      return(val)


w_ecd = readwig('Chapter_9_STARRSeq/3L.w_ecd.wig')
wo_ecd = readwig('Chapter_9_STARRSeq/3L.wo_ecd.wig')  

#Directly view the data. Looking in a region in Chr 3 : Eip75B, which goes from 17950953 to 18064696 on chromosome 3L.
import numpy as np
subset_w_ecd = []
for i in range(17950953,18064696):
    if i in w_ecd['3L']:
        subset_w_ecd.append(w_ecd['3L'][i])
        
ns_w_ecd = np.array(subset_w_ecd)

import matplotlib.pyplot as plt

plt.plot(ns_w_ecd)
#plt.show()

#Extracting peaks. Read density corresponds to enhancers,  which we want to identify.

import scipy
from scipy.signal import find_peaks
from numpy import pi

# Lets see how find_peaks works
x = np.linspace( 0, 6*pi, 600 )
f = np.sin(x)

# https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.find_peaks.html

peaks, _ = find_peaks(f, height=0)

plt.plot(x,f)
plt.plot(x[peaks], f[peaks], "ro")
plt.ylim(-1.1,1.1)
#plt.show()

#Now lets do peak calling on our gene
indices = np.arange(0,len(ns_w_ecd))
peaks, _ = find_peaks(ns_w_ecd) 
plt.plot(ns_w_ecd)
plt.plot(indices[peaks],ns_w_ecd[peaks], "ro")
#plt.show()

#We can call less peaks
peaks, _ = find_peaks(ns_w_ecd, height=4*ns_w_ecd.std()+ns_w_ecd.mean())
plt.plot(ns_w_ecd)
plt.plot(indices[peaks],ns_w_ecd[peaks], "ro")
#plt.show()

#We can use the Savistky Golay filter to smooth it a bit
from scipy.signal import savgol_filter
smooth_ar = savgol_filter(ns_w_ecd,9,1)
peaks, _ = find_peaks(smooth_ar, height=4*smooth_ar.std()+smooth_ar.mean(), distance=10)
plt.plot(smooth_ar,)
plt.plot(indices[peaks],smooth_ar[peaks], "ro")
#plt.show()

#Call peaks on the whole chromosome

temp_list = [] #Values
pos_list = [] #Chromosome positions

for i in sorted(w_ecd['3L'].keys()):
    temp_list.append(w_ecd['3L'][i])
    pos_list.append(i)

chrom_array = np.array(temp_list)

smooth_ar = savgol_filter(chrom_array,9,1)
peaks_ecd, _ = find_peaks(smooth_ar, height=4*smooth_ar.std()+smooth_ar.mean(), distance=10)

print(f'Length of peaks is {len(peaks_ecd)}')

#Now for the non ecdysone treated sample

temp_list = []
pos_list_wo = []

for i in sorted(wo_ecd['3L'].keys()):
    temp_list.append(wo_ecd['3L'][i])
    pos_list_wo.append(i)

chrom_array_wo = np.array(temp_list)

smooth_ar_wo = savgol_filter(chrom_array_wo,9,1)
peaks_wo_ecd, _ = find_peaks(smooth_ar_wo, height=4*smooth_ar_wo.std()+smooth_ar_wo.mean(), distance=10)

print(f'Length of ctl peaks is {len(peaks_wo_ecd)}')

rand_index = int(np.random.rand()*len(peaks_ecd)-1)
print(rand_index)
print(peaks_ecd[rand_index])
peak_val = pos_list[peaks_ecd[rand_index]]
print(peak_val)

#We will plot the STARR-seq density around this random peak and ask if it looks like a peak.

#to see an indiviaul peak 
subset_w_ecd = []
location = []
for i in range(peak_val-2000,peak_val+2000):
    if i in w_ecd['3L']:
        subset_w_ecd.append(w_ecd['3L'][i])
    else:
        subset_w_ecd.append(0)
    location.append(i-peak_val)
ns_w_ecd = np.array(subset_w_ecd)
plt.plot(location,ns_w_ecd)
#plt.show()

#to see the average profile 
import pandas as pd

peak_score_w_ecd = {}

fh = open("py_peaks_w_ecd.bed","w")
ave_vals = {}
location = []
for p in peaks_ecd:
    peak_pos = pos_list[p]
    temp_str = "chr3L\t" + str(peak_pos-250) + "\t" + str(peak_pos+250) + "\t" + str(p) + "\n"
    fh.write(temp_str)
    for i in range(peak_pos-2000,peak_pos+2000):
        if i in w_ecd['3L']:
            ave_vals.setdefault('val',{})
            if i-peak_val in ave_vals:
                ave_vals['val'][i-peak_pos] += w_ecd['3L'][i]
            else:
                ave_vals['val'][i-peak_pos] = w_ecd['3L'][i]
    score=0
    key="chr3L:" + str(peak_pos-250) + "-" + str(peak_pos+250)
    for i in range(peak_pos-100,peak_pos+100):
        if i in w_ecd['3L']:
            score+=w_ecd['3L'][i]
        peak_score_w_ecd[key] = score/20

fh.close()
df_ave_vals = pd.DataFrame(ave_vals)
print(df_ave_vals)
df_ave_vals['val'] /= len(peaks_ecd)
#df_ave_vals.head()
plt.plot(df_ave_vals)
#plt.show()

#and for the control 

fh = open("py_peaks_wo_ecd.bed","w")
ave_vals_wo = {}
location_wo = []
for p in peaks_wo_ecd:
    peak_pos = pos_list_wo[p]
    temp_str = "chr3L\t" + str(peak_pos-250) + "\t" + str(peak_pos+250) + "\t" + str(p) + "\n"
    fh.write(temp_str)
    for i in range(peak_pos-2000,peak_pos+2000):
        if i in wo_ecd['3L']:
            ave_vals_wo.setdefault('val',{})
            if i-peak_val in ave_vals_wo:
                ave_vals_wo['val'][i-peak_pos] += wo_ecd['3L'][i]
            else:
                ave_vals_wo['val'][i-peak_pos]  = wo_ecd['3L'][i]

fh.close()
df_ave_vals = pd.DataFrame(ave_vals_wo)
df_ave_vals['val'] /= len(peaks_wo_ecd)
plt.plot(df_ave_vals)
#plt.show()

#What Transcription Factor motifs underlie enhancer peaks?

#We will first extract the sequences underlying the enhancers that are activated in the presence of ecdysone. We will use bedtools to
#Identify enhancers unique to ecdysone response
#Extract sequences of the enhancers that respond to ecdysone and control enhancers that don't.

import pybedtools 

enhancers_w_ecd = pybedtools.BedTool('py_peaks_w_ecd.bed')
enhancers_wo_ecd = pybedtools.BedTool('py_peaks_wo_ecd.bed')

#Enhancers unique to Ecdysone treatment:
activated_enhancers = enhancers_w_ecd - enhancers_wo_ecd 

print(activated_enhancers.count())


g = activated_enhancers.sequence(fi='Chapter_9_STARRSeq/3L.fa')

#g.seqfn

fo = open('w_ecd_peaks.fa', 'w')
fo.write(open(g.seqfn).read())

g = enhancers_wo_ecd.sequence(fi='Chapter_9_STARRSeq/3L.fa')

fo = open('wo_ecd_peaks.fa', 'w')
fo.write(open(g.seqfn).read())



w_ecd_motifs = pd.read_csv('Chapter_9_STARRSeq/fimo_w_ecd.txt',sep='\t')
w_ecd_motifs.head()

wo_ecd_motifs = pd.read_csv('Chapter_9_STARRSeq/fimo_wo_ecd.txt',sep='\t')
wo_ecd_motifs.head()


norm_w_ecd = (w_ecd_motifs.groupby('motif_alt_id').count()/len(w_ecd_motifs)).iloc[:,0:1]
norm_wo_ecd = (wo_ecd_motifs.groupby('motif_alt_id').count()/len(wo_ecd_motifs)).iloc[:,0:1]
print(norm_w_ecd.head())
print(norm_wo_ecd.head())
mergeddf = pd.merge(norm_w_ecd, norm_wo_ecd, how = 'left', on = 'motif_alt_id')
mergeddf.head()


ratio_w  = mergeddf['# motif_id_x']
ratio_wo = mergeddf['# motif_id_y']

Enrichment = (ratio_w / ratio_wo)
#print(Enrichment)

#Now add these values as a new column
newdf = mergeddf.assign(Enrichment = Enrichment)
print(newdf.sort_values(by='Enrichment',ascending=False).head(10))

peak_score_w_ecd[w_ecd_motifs.iloc[0]['sequence_name']]
print(peak_score_w_ecd)

with_score = pd.DataFrame()
for i in newdf.sort_values(by='Enrichment',ascending=False).head(5).index.values:
    new_df = w_ecd_motifs.query("motif_alt_id == '{0}'".format(i)).iloc[:,1:3]
    #print(new_df.head(1))
    score_col = []
    for index, row in new_df.iterrows():
        score_col.append(peak_score_w_ecd[row['sequence_name']])
    new_df = new_df.assign(score_col = score_col)
    with_score = with_score.append(new_df)
with_score.head()


import seaborn as sns
sns.boxplot(data = with_score, x = 'motif_alt_id', y = 'score_col')
plt.show()