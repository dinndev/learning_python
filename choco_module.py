import pandas as pd
#Q1 --------------------------------------------------------------------------------------------
# READ_DATA
def read_file(file, start_year=2006, end_year=2021):
    """
    read file and filter result depending on start_year to end_year
    
    """
    test_df = pd.read_csv(file)
    #filter  all the result from review_date column depending on start_year (minimum) and end_year (maximum)
    filter = test_df[(test_df.review_date >= start_year) & (test_df.review_date <= end_year)]
    # return only the this column from data frame
    s = filter[['review_date','cocoa_percent','specific_bean_origin_or_bar_name','rating']]
    return s
    

 #Q2 --------------------------------------------------------------------------------------------
# PERCENT_TO_NUMERIC
def percent_to_numeric(df,col_name) :
    """
    convert the percent to float
    
    """
    # It’s safer to create a new DataFrame out of original and leave the original alone
    # convert all the percent to float
    # rstrip = remove all the trailing char if it is percent 
    # astype = set the type of every value to float and divide to 100
    df[col_name] = df[col_name].str.rstrip("%").astype("float") / 100.0
    return df

