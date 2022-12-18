import numpy as np
import matplotlib.pyplot as plt
import csv




def all_poisonous(mushrooms):
	count_p = 0 
	arr_p = []
	for i in mushrooms:		
		if  i [0] == 'p':
			arr_p.append(i)
			count_p += 1
	#print (arr_p)	
	#print (count_p)	
	return arr_p

def arr_of_attributes(arr_p):
	 
	all_attributes = []
	for list_att in range(len(arr_p[1])):
		all_attributes_i = []
		for i in arr_p:
			if i[list_att] not in all_attributes_i:
				all_attributes_i.append(i[list_att])
				#print(all_attributes_i)
		all_attributes.append(all_attributes_i)

	#print(all_attributes_i)		
	print(all_attributes)
	return all_attributes, all_attributes_i


def sum_Xi(arr_p, all_attributes, all_attributes_i ):
	arr_pois = 3912
	arr_list =[]
	for pers_i in all_attributes:
		for pers_j in all_attributes_i: 
			count = 0
			for find in arr_p:
			#print (find)
				if find[pers_j] == pers_j :
					count +=1
				persent = count/arr_pois*100,'%'
			#print( pers, '=', persent)
		arr_list.append(persent)

		for i in arr_list:
			dic = {}
			dic [pers_j] = i  	
		print (count, dic)		
	return count, arr_list



#def creat_dic(arr_p):
	#list_att = []
	#for i in range(1,23):
	#	list_att.append(arr_of_attributes(arr_p))
	#print(list_att)		
	#return 	list_att	




def main():
	with open ('/home/motialp/Downloads/mushrooms.data') as f:
		reader = csv.reader(f)
		mushrooms = list(reader)
	

	arr_p = all_poisonous(mushrooms)
	all_attributes, all_attributes_i = arr_of_attributes(arr_p)
	count, arr_list = sum_Xi(arr_p, all_attributes, all_attributes_i)
#	list_att = creat_dic(arr_p)
	#print(count, arr_list)
	#print (f"blabla")
	
	
	#dic = {}
	#dic["moshe"] = 5263784
	#print (dic)
	#print (dic["moshe"])



if __name__=="__main__":
	main()



























