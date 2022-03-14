import pandas as pd



#Q9 SPLIT_DATASET

def split_dataset (dataset, n = 3) :
    """
    randomly split up data
    the number of data to be return depends on n parameter
    
    """
    shuffled = dataset.sample(frac = 1, replace=False)
    result = np.array_split(shuffled, n)
    return result
    

#Q6 unique items

def calculate_unique(data, variable) :
    """
    Calculate the proportion of unique values
    returning unique values and the length of it
    with table representing it
    
    """
    num_unique = pd.unique(data[variable]).size
    num_total = len(data[variable])
    prop_unique = pd.unique(data[variable])
    return num_unique, num_total, prop_unique


#Q8 Refactoring

def calculate_common(dataset, column):
    
    """
    
    Determine the most common random number
    returning the most occuring item and the count of occurence

    """
    most_occurring_value = dataset[column].value_counts().idxmax()
    return most_occurring_value, dataset[column].value_counts().max()


    

    







    
