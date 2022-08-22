from stat_functions import *
import pandas as pd


df_in = pd.read_csv(
    '/Users/pranavdhruv/Desktop/MY2022/MedCalcProject/SampleData/reference_range/medcalc_input_serum_metabolomics.csv')

d = DFmaker(df_in) #input df for reference rangecalculation
df_exp = d.df_out()
df_exp.to_csv (r'sample_ref.csv', index = False, header=True) for CSV maker


