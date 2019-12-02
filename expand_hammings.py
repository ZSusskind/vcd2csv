#!/usr/bin/env python3

import os
import sys
import pandas as pd

if len(sys.argv) != 3:
	print("Format: " + sys.argv[0] + " <input CSV name> <Max Hamming expansion distance>")
	exit()

input_name = sys.argv[1]
output_name = os.path.splitext(input_name)[0] + "_expanded.csv"
distance = int(sys.argv[2])

data = pd.read_csv(input_name)
hamming_col_names = [x for x in data.columns.values.tolist() if x[0:2] == "d_"]

for hamming_col_name in hamming_col_names:
	current_col_names = data.columns.values.tolist()
	col_idx = current_col_names.index(hamming_col_name)
	distances = data[hamming_col_name].tolist()
	data = data.drop(columns=[hamming_col_name])
	for i in range(1, distance+1):
		data.insert(col_idx, "d" + str(i) + "_" + hamming_col_name[2:], distances)
		distances.insert(0, 0)
		distances = distances[:-1]
		col_idx += 1

data.to_csv(output_name, index=False)
