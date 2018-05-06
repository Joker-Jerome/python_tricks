import os 
import numpy as np 

# function of matching two lists
def match_list(a, b):
    """ find the indices of matching element 
    :return: The indices of elements in list a in list b 
    """
    return np.array([ b.index(x) if x in b else -1 for x in a ])

# function of getting the list
def get_list(filename):
	tmp_list = []
	with open(filename, "r") as fi:
		for item in fi:
			tmp_list.append(item.strip())
	return(tmp_list)

# function of transforming the table to the matrix
def get_matrix(input_table, predictor_list):
	output_list = []
	with open(input_table, "r") as fi:
		for line in fi:
			line_list = line.strip().split("\t")
			basic_list = line_list[:4]
			event_list = line_list[4:]
			match_idx = match_list(event_list, predictor_list)
			tmp_array = np.zeros(len(predictor_list), dtype = int)
			tmp_array[match_idx] = 1
			output_list.append(basic_list + tmp_array.astype(str).tolist())
	return(output_list)

# get the two lists
list_nam = "event_top100.txt"
list_opioid = get_list("./insulinPatients/" + list_nam)
list_insulin = get_list("./opioidPatients/" + list_nam)
list_merged = list_opioid + list_insulin

# transform the data
info_nam = "patient_dict.txt"
opioid_t = get_matrix("./opioidPatients/" + info_nam, list_merged)
insulin_t = get_matrix("./insulinPatients/" + info_nam, list_merged)

# output file
output_nam = "merged_matrix.txt"
with open(output_nam, "w") as fo:
	fo.write("\t".join(["patient_id", "age", "gender", "weight"]) + "\t" + "\t".join(list_merged) + "\t" + "label" + "\n")
	for item in opioid_t:
		fo.write("\t".join(item) + "\t" + "opioid" + "\n")
	for item in insulin_t:
		fo.write("\t".join(item) + "\t" + "insulin" + "\n")







