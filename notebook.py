# Q1 IMPORTS 

import pandas as pd
import numpy as np
import random
import my_experiment as exp
#---------------------------------------------------------------------------------------
# PART 1 NUMPY

# Q2 arrays

my_array = np.array([[1,2,3],[4,5,6],[7,8,0]])

#---------------------------------------------------------------------------------------

# Q3 row_sums

def row_sums(np_array) :
    sum = []
    for item in np_array :
        sum.append(np.sum(item))
    
    return sum
#---------------------------------------------------------------------------------------

# Q4 array_min

def array_min(np_array) :
    min_val = np.amin(np_array) # "amin" is an np method for getting the minimum number inside np array
    out = np.where(min_val == np_array)
    return out
 
#---------------------------------------------------------------------------------------

# PART 2 PANDAS

#Q5 data

df = pd.read_csv('data/random_guess.csv')

#---------------------------------------------------------------------------------------

#Q7 debugging

def select_sample(dataset, n) :
    out = dataset.sample(n, random_state=1, replace=False)
    return out
    
    

    

    







    