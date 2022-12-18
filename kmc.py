import numpy as np
import csv
import random



def float_(irises):
	for i in irises:
		for j in range(4):
			i[j] = float(i[j])
	
	return irises
	
	
def random_means(irises, k):
	means = random.sample(irises,k)
#	print(irises)
	return means
	
 
	 
 

def distans_ganeral(point_1, point_2):
	dis= 0
	#for i in range([])
	dis = (point_1[0] - point_2[0])**2 + (point_1[1] - point_2[1])**2 + (point_1[2] - point_2[2])**2 + (point_1[3] - point_2[3])**2 
		
	
	return dis

def distand_prive(irises, means):
	dis_0 = 0
	dis_1 = 0
	dis_2 = 0
	group_one = []
	group_two = []	
	group_three = []
	for dis in irises:
		dis_0 =  distans_ganeral(dis, means[0])
		#dis_0.append(dis_a)
		dis_1 =  distans_ganeral(dis, means[1])
		#dis_1.append(dis_b)
		dis_2 =  distans_ganeral(dis, means[2])
		#dis_2.append(dis_c)
#		print(dis_0)#, dis_1, dis_2)
		min_i = min(dis_0, dis_1, dis_2)
		if min_i == dis_0:
			group_one.append(dis)
		elif min_i == dis_1:
			group_two.append(dis)
		else:
			group_three.append(dis)
			 
	print (len(group_one))
	print (len(group_two))	
	print (len(group_three))
	
	return group_one, group_two, group_three



def center_of_mass(group_one, group_two, group_three):
	cm_arr0 =[]
	cm0	 = 0
	for i in range(4):
		for iris in group_one:
			cm0 += iris[i]/len(group_one)			 	
		cm_arr0.append(cm0)
	print(cm_arr0)
	
	cm_arr1 =[]
	cm1 = 0
	for i in range(4):
		for iris in group_two:
			cm1 += iris[i]/len(group_two)			 	
		cm_arr1.append(cm1)
	print(cm_arr1)

	cm_arr2 =[]
	cm2 = 0
	for i in range(4):
		for iris in group_three:
			cm2 += iris[i]/len(group_one)			 	
		cm_arr2.append(cm2)
	print(cm_arr2)

	return cm_arr0, cm_arr1, cm_arr2



def other_mc(irises, cm_arr0, cm_arr1, cm_arr2):
	mc_a = 0
	dis_b = 0
	dis_c = 0
	group_cm0 = []
	group_cm1 = []	
	group_cm2 = []
	for dis in irises:
		dis_a =  distans_ganeral(dis, cm_arr0[0])
		
		dis_b =  distans_ganeral(dis, cm_arr1[1])
		
		dis_c =  distans_ganeral(dis, cm_arr2[2])
		
		min_m = min(dis_a, dis_b, dis_c)
		if min_m == dis_a:
			group_cm0.append(dis)
		elif min_m == dis_b:
			group_cm1.append(dis)
		else:
			group_cm2.append(dis)
			 
	print (len(group_cm0))
	print (len(group_cn1))	
	print (len(group_cm2))
	
	return group_cm0, group_cm1, group_cm2





def main():
	with open ('/home/motialp/Downloads/iris.data') as f:
		reader = csv.reader(f)
		irises = list(reader)
	#print (means[1][:-1])
	#data_split = splite_(irises)
	irises = float_(irises)
	means = random_means(irises,3)
	group_one, group_two, group_three = distand_prive(irises, means)
	cm_arr0, cm_arr1, cm_arr2 = center_of_mass(group_one, group_two, group_three)
	group_cm0, group_cm1, group_cm2 =other_mc(irises, cm_arr0, cm_arr1, cm_arr2)
	#itar = num_random(cm_arr0, cm_arr1, cm_arr2, 10)
	#dis_0, dis_1, dis_2 = distand_prive(irises, means)
#	min_dis = find_min(irises,means,dis_0, dis_1, dis_2)
	#dis = distans_ganeral(sum(means, sum(irises)))
	
if __name__=="__main__":
	main()

















