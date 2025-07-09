#!/bin/python
import os

rgi_comp=open("outputfname.csv","a")
dire="inpuyt file directory with all rgi output files"
def cal_rgi_merge(fname):
	rgi = open(str(dire)+fname,"r")
	print("FILE:\n\n")
	rgi_val=[]
	count_rgi={}
	drug_cla=[]
	for lines in rgi.readlines():
		line=lines.split("\t")
		rgi_val.append([line[1],line[14]])
		dr=(line[14].split(";"))
		drug_cla.extend(dr)
		
	print("DRUG_CLAS\n",drug_cla)
	drug_cla_n= [x.strip(' ') for x in drug_cla]
	print("\nDRUG_CLAS\n",drug_cla_n)	
	for i in set(drug_cla_n):
		#print(i)
		count_rgi[i]=str(drug_cla_n.count(i))
	print(type(count_rgi))
	
	rgi_comp.write(fname+","+str(count_rgi)+"\n")

		
				

for files in os.listdir(dire):
	cal_rgi_merge(files)				
							
			
