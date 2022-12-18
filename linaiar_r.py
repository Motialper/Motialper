import numpy as np
import matplotlib.pyplot as plt


data_array1 = np.load ('/home/motialp/Downloads/XYdata/array_1.npy')
data_array2 = np.load('/home/motialp/Downloads/XYdata/array_2.npy')
X = data_array1
Y =data_array2	


def grandient(x, y, teta_1, teta_2):
    
    sum_x = 0
    sum_y = 0
    for i in range(len(x)):
        sum_x = sum_x + (teta_1 + teta_2 * X[i] - Y[i])
        sum_y = sum_y + (teta_1 + teta_2 * X[i] - Y[i])*X[i]
    return sum_x, sum_y



def fix(teta_1,  teta_2):
    X = data_array1
    Y = data_array2
    sum_x, sum_y = grandient(X, Y, teta_1, teta_2)
    Learning_rate = 0.0001
    fix_teta_x =  teta_1 - Learning_rate * sum_x
    fix_teta_y =  teta_2 - Learning_rate * sum_y

   # print (sum_x, sum_y)
    
    return fix_teta_x, fix_teta_y


def iterations():
    iter_num =100
    teta_1 = teta_2 =1
    for i in range(iter_num):
        teta_1,teta_2 = fix(teta_1, teta_2)
        print(f'{cost_function(teta_1, teta_2 )=}')
    return  teta_1,teta_2
    


def cost_function(teta_1, teta_2 ):
    cost=0
    for i in range(len(X)):
        linex = teta_1 + teta_2 * X[i]
        cost += (linex - Y[i] )**2
        #print (cost)
    return cost

def display(X, Y, teta_1, teta_2 ):
    linex = teta_1 + teta_2 * X
    plt.scatter(X,Y)
    plt.plot(linex, X)
    plt.show()
    return 




def main():

    x = data_array1
    y = data_array2  
    print(X,Y)
    teta_1 = 1
    teta_2 = 2
    fix_teta_x, fix_teta_y = fix(x, y)
    iterations()
    cost_function(x, y )
    display (X, Y, teta_1, teta_2)

if __name__=="__main__":
    main()








 

































