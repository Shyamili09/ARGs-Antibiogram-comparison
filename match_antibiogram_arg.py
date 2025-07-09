#!/bin/python
import os


from collections import OrderedDict
abg = open("Antibiogram_summary_filename.csv","r")
rgi = open("Merged_rgi_files.csv","r")
rgi_d={}

#readind rgi files and storing in dictionary
for lines in rgi.readlines():
	line=lines.split(",")
	#print(line)
	sample=line[0].strip(".txt")
	#print("sample",sample)
	arg_cl = [x.strip(' ') for x in line[1:]]
	arg_cl = [x.replace("'","") for x in arg_cl]
	arg_cl = [x.replace("{","") for x in arg_cl]
	arg_cl = [x.replace("}","") for x in arg_cl]
	arg_cl = [x.replace("\n","") for x in arg_cl]
	#print(arg_cl)
	sample=sample.replace("99.5_rgi_","")
	#print(sample)
	rgi_d[sample]=arg_cl
	
print("rgi_d",rgi_d)
# this is list of antibioitc names and antibiotic classes based on antibiogram to be compared
abg_hea=["GENTAMYCIN__aminoglycoside__2nd","AMIKACIN__aminoglycoside__3rd","TOBRAMYCIN__aminoglycoside__3rd","BENZYLPENCILLIN__penam__1st","AZTREONAM__monobactam__0","OXACILLIN__penam__2nd","AMPICILLIN__penam__3rd","DORIPENEM__carbapenem__0","ERTAPENEM__carbapenem__0","IMIPENEM__carbapenem__0","MEROPENEM__carbapenem__0","CEFAZOLIN__cephalosporin__1st","CEFOXITIN__cephamycin__2nd","CEFUROXIME__cephalosporin__2nd","CEFUROXIMEAXETIL__cephalosporin__2nd","CEPHOXITIN__cephalosporin__2nd","CEFOTAXIME__cephalosporin__3rd","CEFTRIAXONE__cephalosporin__3rd","CEPHOTAXIME__cephalosporin__3rd","CEFEPIME__cephalosporin__4th","CEFTAZIDIME__cephalosporin__5th","CEFOPERAZONE/SULBACTUM__penam cephalosporin__0","AMOXYCILLIN+CLAVULANICACID__penam__0","PIPERACILLIN+TAZOBACTUM__penam__0","TICARCILLIN+CLAVULANICACID__penam__0","DAPTOMYCIN__lipopeptide__0","TEICOPLANIN__Glycopeptide__0","VANCOMYCIN__Glycopeptide__0","COLISTIN__polymyxin__0","NALIDIXICACID__fluoroquinolone__1st","OFLOXACIN__fluoroquinolone__2nd","CIPROFLOXACIN__fluoroquinolone__2nd","NORFLOXACIN__fluoroquinolone__2nd","LEVOFLOXCIN__fluoroquinolone__3rd","MOXIFLOXACIN__fluoroquinolone__3rd","GATIFLOXACIN__fluoroquinolone__4th","RIFAMPICIN__rifamycin__0","CO-TRIMOXAZOLE__Sulfonamide__0","TRIMETHOPRIM/SULFOMETHOXAZOLE__Sulfonamide__0","MINOCYCLINE__tetracycline__0","TETRACYCLIN__tetracycline__0","TIGECYCLINE__glycylcycline__0","CLINDAMYCIN__Lincosamide__0","AZITHROMYCIN__macrolide__0","ERYTHROMYCIN__macrolide__0","CHLORAMPHENICOL__Phenicol__0","LINEZOLID__oxazolidinone__0","NITROFURANTOIN__nitrofuran__0","FOSFOMYCIN__phosphonic__0","MENINGITIS__MENINGITIS__0","PNEUMONIA__PNEUMONIA__0","ORAL__ORAL__0","OTHER__OTHER__0"]

abg_hea_LVp=["AMIKACIN__aminoglycoside__3rd","VANCOMYCIN__Glycopeptide__0","CEFUROXIME__cephalosporin__2nd","CEFAZOLIN__cephalosporin__1st","CHLORAMPHENICOL__Phenicol__0","OFLOXACIN__fluoroquinolone__2nd","CIPROFLOXACIN__fluoroquinolone__2nd","GATIFLOXACIN__fluoroquinolone__4th","MOXIFLOXACIN__fluoroquinolone__3rd","CEPHOXITIN__cephalosporin__2nd","GENTAMYCIN__aminoglycoside__2nd","CEFTAZIDIME__cephalosporin__5th","PIPERACILLIN+TAZOBACTUM__penam__0","TICARCILLIN+CLAVULANICACID__penam__0","CEFOPERAZONE/SULBACTUM__penam cephalosporin__0","CEFEPIME__cephalosporin__4th","DORIPENEM__carbapenem__0","IMIPENEM__carbapenem__0","MEROPENEM__carbapenem__0","LEVOFLOXCIN__fluoroquinolone__3rd","TOBRAMYCIN__aminoglycoside__3rd","MINOCYCLINE__tetracycline__0","COLISTIN__polymyxin__0","TIGECYCLINE__glycylcycline__0","TRIMETHOPRIM/SULFOMETHOXAZOLE__Sulfonamide__0","LINEZOLID__oxazolidinone__0","AZITHROMYCIN__macrolide__0","BENZYLPENCILLIN__penam__1st","CEFTRIAXONE__cephalosporin__3rd","ERYTHROMYCIN__macrolide__0","CLINDAMYCIN__Lincosamide__0","TETRACYCLIN__tetracycline__0","RIFAMPICIN__rifamycin__0","AZTREONAM__monobactam__0","CEFOXITIN__cephamycin__2nd","OXACILLIN__penam__2nd","DAPTOMYCIN__lipopeptide__0","TEICOPLANIN__Glycopeptide__0","NITROFURANTOIN__nitrofuran__0","AMPICILLIN__penam__3rd","CO-TRIMOXAZOLE__Sulfonamide__0","CEPHOTAXIME__cephalosporin__3rd","ERTAPENEM__carbapenem__0","AMOXYCILLIN+CLAVULANICACID__penam__0","NALIDIXICACID__fluoroquinolone__1st","CEFOTAXIME__cephalosporin__3rd","PNEUMONIA__PNEUMONIA__0","ORAL__ORAL__0","MENINGITIS__MENINGITIS__0","OTHER__OTHER__0","CEFUROXIMEAXETIL__cephalosporin__2nd","NORFLOXACIN__fluoroquinolone__2nd","FOSFOMYCIN__phosphonic__0"]

abg_cl=abg_cl_s={}

#parsing abtibiogram class in from LVPEI , Res or sensiti value, arg from rgi finder
def match_withabg(abgclas,abg_rs,arg_cl):
	print("INPUT_ARG_ABG_COMPARISON\n",abgclas,abg_rs,arg_cl)
	abgclas=abgclas.strip(" ")
	res = any(abgclas.lower() in cl.lower() for cl in arg_cl)
	res=str(res)
	abg_rs=str(abg_rs)
	abg_rs=abg_rs.strip("\n")
	abg_rs=abg_rs.strip("*")
	print("ABG_ARG_COMPARISON\n",res,abg_rs,abgclas)
	resu=""
	if (str(res) == "True" and str(abg_rs)=="R"):
		print("match_ARG_Found")
		resu="yesR"
	elif (res == "False" and abg_rs == "S"):
		print("Match_susceptible")
		resu="yesS"
	elif (res == "False" and abg_rs == "R"):
		print("mismatch_ARG_not_found_species_is_resistant")
		resu="no"
	elif (res == "True" and abg_rs =="NA"):
		print("Putative_ARG_found")
		resu="P"
	elif (res == "True" and abg_rs == "I"):
		print("ARGFound_Intermediate")
		resu="ARGi"
	elif (res == "True" and abg_rs == "SDD"):
		print("ARG_SDD")
		resu="ARG_SDD"
	elif (res == "False" and abg_rs == "NA"):
		print("NO_DETAILs")
		resu="NA"
	elif (res == "False" and abg_rs == "I"):
		resu="NoARGi"
		print("NoArg_Intermediate")
	elif (res == "True" and abg_rs == "S"):
		print("NVARG")
		resu="NVARG"
	elif (res == "FALSE" and abg_rs == "SDD"):
		print("No_ARG_SDD")
		resu="N_SDD"
	else:
		print("Error")	
	return(resu)
#reading abg summary file
for lines in abg.readlines()[1:]:
	line=lines.split(",")
	sampl=line[0]
	print(sampl)
	print(line)
	abg_cll=line[9:]
	abg_cl={}
	#print("antibiogram cll",(abg_cll),len(abg_hea_LVp))
	for i in range(len(abg_cll)):
		abg_cl[abg_hea_LVp[i]]=abg_cll[i]
	print("eacsample",sampl,abg_cl)
	(abg_cl_s[sampl])=abg_cl
	abg_cl={}	
	
print("\nabg_cl_s",abg_cl_s)
#dict containing each sample the abg results
#{'P.aeruginosa_b5_r1': {'GENTAMYCIN__Aminoglycoside__2nd': 'S', 'AMIKACIN__Aminoglycoside__3rd': 'NA', 'TOBRAMYCIN__Aminoglycoside__3rd': 'NA', 'BENZYLPENCILLIN__Beta-lactam__1st': 'NA', 'AZTREONAM__Beta-lactam/monobactam__0': 'NA', 'OXACILLIN__Beta-lactam/penam__2nd': 'NA', 'AMPICILLIN__Beta-lactam/penam__3rd': 'S', 'DORIPENEM__Carbapenem__0': 'NA', 'ERTAPENEM__Carbapenem__0': 'NA', 'IMIPENEM__Carbapenem__0': 'NA', 'MEROPENEM__Carbapenem__0': 'S', 'CEFAZOLIN__Cephalosporin__1st': 'NA', 'CEFUROXIME__Cephalosporin__2nd': 'SDD', 'CEFUROXIMEAXETIL__Cephalosporin__2nd': 'NA', 'CEPHOXITIN__Cephalosporin__2nd': 'S', 'CEFOTAXIME__Cephalosporin__3rd
#rgi_dictionar keys :  S.aureus_b5_r1 ['peptide antibiotic: 1', 'fluoroquinolone antibiotic: 3', 'tetracycline antibiotic: 2', 'penam: 1', 'disinfecting agents and antiseptics: 3', 'cephalosporin: 1', 'glycylcycline: 1', 'Drug Class: 1}\n']
abg_abu=open("abg_arg_abundance_RGI_b8_b12.csv","w")
abg_abu.write("Sample"+","+",".join(x for x in abg_hea)+"\n")
def rgiabu(sam):
	print("Abundance",sam,rgi_d[sam])
	abu=OrderedDict()
	for i in range(len(abg_hea)):
		abu[abg_hea[i]]=0
		for cl in filter(None, rgi_d[sam]):
			abg_clas=abg_hea[i].split("__")[1]
			clabulis=(cl.split(":")[0]).lower()
			print("Clabulis",clabulis,abg_clas.lower())
			clabulis=clabulis.replace("antibiotic","")
			clabulis=clabulis.replace("acid","")
			clabulis=clabulis.strip("\n")
			clabulis=clabulis.strip("}")
			clabulis=clabulis.strip("{")
			if str(clabulis).strip(" ") in abg_clas.lower():
				print("Found",cl,abg_hea[i].split("__")[1])
				clab=cl.split(":")[1]
				clab=clab.strip("\n")
				clab=clab.strip("}")
				clab=clab.strip("{")
				abu[abg_hea[i]]=clab.strip(" ")	
	#print(sam,abu)
	abg_abu.write(sam+","+",".join(str(x) for x in list(abu.values()))+"\n")
		

print("abg_cl_s",abg_cl_s)
comp=""
comp_l=[]
fw=open("Comparing_abg_arg_rep_99.5perc_ed_tryabu_b8_b12.csv","w")	
fw.write("sampl"+","+",".join(x for x in abg_hea_LVp)+"\n")		
for sampl,val  in (abg_cl_s.items()) :
	print("samples",sampl,val)
	if sampl in rgi_d.keys():
		rgiabun=rgiabu(sampl)
		#print("Sample_match",sampl)
		comp_l=[]
		for abg_keys,abg in val.items():
			#print("all_details\n",sampl,rgi_d[sampl],abg_keys,abg)
			#print(str(abg_keys).split("__")[1],abg)
			abg_cl_1=str(abg_keys).split("__")[1]
			comp=match_withabg(abg_cl_1,abg,rgi_d[sampl])
			comp_l.append(comp)
		#print("Writing lines\n",sampl+","+",".join(x for x in comp_l)+"\n")
		fw.write(sampl+","+",".join(x for x in comp_l)+"\n")
	else:
		print("NOT FOUND",sampl)
			
					

