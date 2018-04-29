import os
import sys

# file name
file_name = sys.argv[1]

# method
method_nam = sys.argv[2]

# datasets
real_data_list = ["Brain", "HNSC", "TCGA_LUNG", "melanoma", "Metabric"]

# splitrule
par1_vec = ["logrank", "logrankscore"]

# ntree
par2_vec = [100, 200, 500]

# nodedepth
par3_vec = [3,5,7]

with open(file_name, "w") as fo:
	for dataset in real_data_list:
		for par1 in par1_vec:
			for par2 in par2_vec:
				for par3 in par3_vec:
					fo.write("module load R; Rscript --vanilla " + method_nam + "_multi.R /ysm-gpfs/project/lz276/Project3/data_survival/" + dataset + " " + dataset)
					fo.write(" " + str(par1) + " " + str(par2) + " " + str(par3) + "\n")
