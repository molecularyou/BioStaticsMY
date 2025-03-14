from stat_functions import DFmaker
import pandas as pd

# Input data file with concentrations
df_in = pd.read_csv('medcalc_input_plasma_metabolomics.csv')
# df_in = pd.read_csv('input.csv')

# Ensure biomarkers are up to date in the MYBiomarkers.csv file

# Input df for reference range calculation
d = DFmaker(df_in, None, None, None)

df_exp = d.df_out().T
df_exp.columns = [
    'measure_id',
    'range',
    'age',
    'sex',
    'biofluid',
    'category',
    'exported'
]
df_exp.to_csv(r'output.csv', index=False, header=True)
