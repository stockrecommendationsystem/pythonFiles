#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# step5: s5_preprocess_occurrence.py
from pathlib import Path
import csv

#Get the list of pages on the first page based on tag url
rownum = 0
colnum = 0
file = "data/co-occurrence_all.txt"
with open('data/preprocessed-cooccurrence.csv', mode='w') as occurrence_file:
	ooccurrence_writer = csv.writer(occurrence_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	rows = Path(file).read_text().split("\n")
	for row in rows:
		if len(row) > 0:
			stocks = row.split("\t")
			vlstocks = []
			for stock in stocks:
				if "." not in stock:
					vlstocks.append(stock)
			if len(vlstocks) >0 :
				rownum += 1
				ooccurrence_writer.writerow(vlstocks)
				if len(vlstocks) > colnum:
					colnum = len(vlstocks)

print("Row number: " + str(rownum))
print("Colume number: " + str(colnum))