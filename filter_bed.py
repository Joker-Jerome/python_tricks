# module
import sys

# arguments passing
args = sys.argv
chr = args[1]
start = int(args[2])
end = int(args[3])
infile = args[4]
outfile = args[5]
print("Info: Inputfile is " + infile + "\n")

# read the file and filter
fo = open(outfile, "w")
fo.write("\t".join(["chromosome", "start", "end", "score"]) + "\n")
ct = 0 
with open(infile, "r") as fi:
	for line in fi:
		ct += 1
		if ct % 5000 == 0:
			print("Info: " + str(ct) + " lines processed.\n" )
		tmp_line = line.strip().split()
		tmp_chr = tmp_line[0]
		tmp_start = int(tmp_line[1])
		tmp_end = int(tmp_line[2])
		tmp_score = tmp_line[3]
		if tmp_chr == chr and tmp_start >= start and tmp_end <= end:
			print("Info: Target found. \n" + tmp_line + "\n")
			fo.write("\t".join(tmp_line) + "\n")
fo.close()