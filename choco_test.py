from choco_module import read_file
from choco_module import percent_to_numeric
import pandas as pd
import numpy as np

#Q4
# TEST_FUNCTION: TEST_READ_DATA

def test_read_data () :
    assert type(read_file("testfile.csv")) == pd.DataFrame
    assert all(read_file("testfile.csv").review_date.between(2006, 2021, inclusive=True))
    assert len(read_file('testfile.csv')) == 20

#-------------------------------------------------------------------------

#Q5

#TEST_CALCULATE_STATS

def test_precent_to_numeric():
    df = read_file('testfile.csv')
    df_fixed = percent_to_numeric(df, 'cocoa_percent')
    
    # type will check the type of return and compare to right operand. if this condition returns False, AssertionError is raised
    assert type(df_fixed['cocoa_percent']) == pd.Series
    # all() function will return bool, returns true if all the elements of iterable is True.
    # and between will return bool, if the series element is between the given parameter
    assert all(df_fixed['cocoa_percent'].between(0.0, 100.0, inclusive=True))
    # np.array_equal will return True if the first and second parameter is match
    assert np.array_equal(df_fixed['cocoa_percent'], df_fixed['cocoa_percent'].astype(float))

        
        
        

        
     
     
