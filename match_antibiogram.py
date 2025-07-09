#!/bin/python
import os
'''arg= open("ARG_subclasscounts_b2.csv","r")
abg=open("antibiogram_b2.csv","r")
abg_class=open("antibiogram_classes.txt","r")
arg_dict={}
arg_val={}
subc=[]
subclass_list=arg.readlines()[0]
for su in subclass_list.split(",")[1:]:
	#print(su)
	subc.append(su.strip("\n"))
#subc=(subc[2:])
#print(subc)
#print(subclass_list)
arg.close()
arg= open("ARG_subclasscounts_b2.csv","r")
#for su in 
for lines in arg.readlines()[1:]:
	line=lines.split(",")
	#sample=line[1]
	sample=line[0]
	#print(sample)
	#print(line)
	for su, val  in zip(subc,line[1:]):
		arg_val[su]=val.strip("\n")
	#print(arg_val)
	arg_dict[sample]=arg_val
	arg_val={}
	
#print(arg_dict)

abg_dict={}
abg_val={}
subc_abg=[]
subclass_list_abg=abg.readlines()[0]
for su in subclass_list_abg.split(","):
	#print(su)
	subc_abg.append(su.strip("\n"))
#subc=(subc[2:])
subc_abg=subc_abg[6:]
#print(subc_abg)
#print(subclass_list)
abg.close()
abg= open("antibiogram_b2.csv","r")
#for su in 
for lines in abg.readlines()[1:]:
	line=lines.split(",")
	#print(line)
	#sample=line[1]
	#sample=line[0]
	sample=tuple(line[:6])
	#print(sample)
	#print(line[6:])
	for su, val  in zip(subc_abg,line[6:]):
		abg_val[su]=val.strip("\n")
	#print(abg_val)
	abg_dict[sample]=dict(abg_val)
	abg_val={}
	
#print(abg_dict)


#for keyb,val in (abg_dict).items():
	#print(keyb)
	#print(arg_dict.keys())
	#if str(list(keyb)[0]) in arg_dict.keys():
		#print("match\n")
		#print(abg_dict[keyb])
		#print("\n")
		#print(arg_dict[str(list(keyb)[0])])	'''

rgi_comp=open("batch8_12_rgi_compile_99.5perc.csv","a")
dire="/home/ccmb/LV_data/abg_arg_comp_b8_b12/99.5_rgi_files/"
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

#for i in rgi_val:
#	print(i)


'''for keyb in abg_dict:
		if (keyb[5]) == "TRUE" and  str(keyb[0]) == str(keyr):
			print(keyb[0],keyr)
			print("matched\n",keyr,keyb,arg_dict[keyr],abg_dict[keyb])'''
				
				

for files in os.listdir(dire):
	cal_rgi_merge(files)				
							
			
