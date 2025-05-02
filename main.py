from stat_functions import DFmaker
import pandas as pd

# Input data file with concentrations
concentration_input_file_name = 'input.csv'

# Input data file with biomarker detection limits and MYCO IDs
# detection_limit_input_file_name = 'MYBiomarkers_HQE.csv'
detection_limit_input_file_name = 'MYBiomarkers_MRM-P.csv'

# Input df for reference range calculation
df_in = pd.read_csv(concentration_input_file_name)
d = DFmaker(df_in, detection_limit_input_file_name, None, None, None, None)

df_exp = d.df_out().T
df_exp.columns = [
    'measure_id',
    'lower_range',
    'upper_range',
    'units',
    'age',
    'sex',
    'biofluid',
    'category',
    'reference',
    'exported'
]
df_exp.to_csv(r'output.csv', index=False, header=True)
