from stat_functions import *
import pandas as pd


df_in = pd.read_csv(
    'filepath.csv')

d = DFmaker(df_in) #input df for reference rangecalculation
df_exp = d.df_out()
df_exp.to_csv (r'sample_ref.csv', index = False, header=True) for CSV maker


