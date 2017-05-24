import pandas as pd
import numpy as np

def load_sav_table(filename):
    """

    Loads SAV data file into a pandas Dataframe

    INPUTS:

    filename: 
        file name

    RETURNS

    df: 
        pandas Dataframe

    """
    df = pd.read_csv(filename,sep='\t',header=0,index_col=False)
    print("df has %d entries.\n" % np.shape(df)[0])
    return df

