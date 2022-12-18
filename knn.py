import numpy as np
import matplotlib.pyplot as plt
#from sklearn.model_selection import train_test_split
import random
from math import sqrt
import csv
#def array_of_arrays(irises):
 #   all_arrays[]
  #  for i in range(len(irises)):
        


def randum_train_test(irises):
    random.shuffle(irises)
   # print(irises)
    train = irises[:120]
    test = irises[120:]
   # print (train, test)
    return train, test
 
#def splite_data(irises ):
 #   x = []
  #  y = []
   #    x = irises[:4]
    #    y = irises[4:]

        # x = irises[i].split(',')[:4]
        #y = irises[i].split(',')[4:]
        
     #   print(x,y)
   # return x,y


def distans(flower_train, flower_test):
    dis =0.0
    for i in range(len(flower_train)-1):
        dis += (float(flower_train[i]) - float( flower_test[i]))**2
    bis = sqrt(dis)
    print(dis)
    return dis
    






def main():
    with open ('/home/motialp/Downloads/iris.data.npy') as f:
        reader = csv.reader(f)
        irises = list(reader)
        print(irises)

    flower_train, flower_test = randum_train_test(irises )
    neighbors =[]   
    for i in range(len(flower_test )-1):
        test_nighb = []
        for j in range(len(flower_train)):
            dist =  distans(flower_train[j], flower_test[i])
            test_nighb.append(dist)
        neighbors.append(test_nighb)
    print(np.sort(neighbors))

    #print(neighbors)    
     
 
 # splite_data(irises)

if __name__=="__main__":
    main()












































