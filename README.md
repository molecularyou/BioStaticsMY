# Biostatistics

Biostatistics is a software tool for calculating reference ranges in accordance to the Clinical & Laboratory Standards Institute (CLSI) guidelines 

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the following libraries 

```bash
pip install numpy
pip install scipy
pip install pandas
```

## Usage

```python
from stat_functions import *

#insert file here
df_in = pd.read_csv(
    'filepath.csv')

#input df for reference range calculation
d = DFmaker(df_in) 
df_exp = d.df_out()
#generates csv
df_exp.to_csv (r'sample_ref.csv', index = False, header=True)
```

## Useful Classes
For more information to use other statistical features look into the ```Biostatistics```
class under the ```stat_functions``` file


## Authors and acknowledgements
Tool develeped by Pranav Dhruv Tandon under the guidance of Anna Prudova, Mai Yamamoto, and Windy Wang

## Contributing
Pull requests are welcome. 
Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
