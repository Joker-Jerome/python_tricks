import os
import sys

# file name
file_name = sys.argv[1]

# method
method_nam = sys.argv[2]

# datasets
real_data_list = ["Brain", "HNSC", "TCGA_LUNG", "melanoma", "Metabric"]

# stepsize 
par1_vec = [0.01, 0.1, 0.5, 1, 2]

# maxstep
par2_vec = [100, 250, 500]

with open(file_name, "w") as fo:
	for dataset in real_data_list:
		for par1 in par1_vec:
			for par2 in par2_vec:
				fo.write("module load R; Rscript --vanila " + method_nam + "_multi.R /ysm-gpfs/project/lz276/Project3/data_survival/" + dataset + " " + dataset)
				fo.write(" " + str(par1) + " " + str(par2) + "\n")
