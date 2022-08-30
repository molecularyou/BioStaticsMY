from stat_functions import *
import pandas as pd


df_in = pd.read_csv(
    '/Users/pranavdhruv/Desktop/MY2022/MedCalcProject/SampleData/reference_range/medcalc_input_serum_metabolomics.csv')


#always make sure that the biomarkers are up to date in the MYBiomarkers.csv file

d = DFmaker(df_in,None,None, None) #input df for reference range calculation

df_exp = d.df_out().T
df_exp.columns = ['measure_id', 'range', 'age', 'sex','biofluid','category', 'exported' ] #add more columns for future and update 
# in the dictionary inside DFmaker
df_exp.to_csv (r'sample_ref.csv', index = False, header=True) # for CSV maker
