import json
import os 
import numpy as np
import pickle

# init
patient_info = {}

# open json filename and import the data
def open_json(filename):
	print("INFO: Processing " + filename)
	tmp_data = json.load(open(filename))
	extract_field = ["patientonsetage", "patientsex", "patientweight"]
	info_list = []
	if len(tmp_data) != 0:
		for record in tmp_data:
			tmp_dict = {}
			for field in extract_field:
				try:
					if record[field] is None:
						tmp_dict[field] = "NA"
					elif field == "patientonsetage" and "patientonsetageunit" in record.keys():
						tmp_age = str(convert_age(record["patientonsetage"], record["patientonsetageunit"]))
						tmp_dict[field] = tmp_age
					else:
						tmp_dict[field] = record[field]						
				except (KeyError, TypeError):
					tmp_dict[field] = "NA"
			reaction_list = []
			for reaction_dict in record["reaction"]:
				reaction_list.append(reaction_dict["reactionmeddrapt"])
			tmp_dict["reaction"] = reaction_list
			info_list.append(tmp_dict)
	return(info_list)


# extract the info in one dir
def extract_json(dir):
	file_list = []
	# get the json file list
	for tmp_file in os.listdir(dir):
		if tmp_file.endswith(".json"):
			file_list.append(tmp_file)
	count = 0		
	for json_nam in file_list:
		json_file = dir + "/" + json_nam
		tmp_list = open_json(json_file)
		for i in range(len(tmp_list)):
			count += 1
			patient_id = dir + "_" + str(count)
			patient_info[patient_id] = tmp_list[i]
# run
def run():
	for directory in os.listdir():
		if os.path.isdir(directory):
			extract_json(directory)

# age handling
def convert_age(value, code):
	if code == "800" or float(value) < 15:
		return(float(value)*10)
	elif code == "801" or (float(value) > 20 and float(value) < 150):
		return(float(value))
	elif code == "802":
		return(float(value)/12)
	elif code == "803":
		return(float(value)/52)
	elif code == "804" or (float(value) > 7500 and float(value) < 54750):
		return(float(value)/365)
	elif code == "805" or float(value) > 100000 :
		return(float(value)/(365*24))

#  run the main
run()
with open("patient_dict.txt",'w') as fo:
	for patient_id in patient_info.keys():
		p_dict = patient_info[patient_id]  
		fixed_column = ["patientonsetage", "patientsex", "patientweight"]
		fo.write(patient_id + "\t")
		#print(p_dict[fixed_column[0]])
		fo.write("\t".join([ p_dict[x] for x in fixed_column]))
		fo.write("\t".join([ x for x in p_dict["reaction"]]))
		fo.write("\n") 




