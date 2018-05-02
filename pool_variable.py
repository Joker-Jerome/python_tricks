import os
import numpy as np
import collections
import operator

event_count = collections.defaultdict(int)
with open("pateint_dict.txt", "r") as fi:
	for tmpline in fi:
		tmp_list = tmpline.strip().split("\t")[4:]
		for event in tmp_list:
			event_count[event] += 1

sorted_count = sorted(event_count.items(), key=operator.itemgetter(1), reverse=True)

with open("event_count.txt", "w") as fo:
	for item in sorted_count:
		fo.write("\t".join([item[0],str(item[1])]) + "\n")


