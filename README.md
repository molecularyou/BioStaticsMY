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
from stat_functions import DFmaker

# Insert file here
df_in = pd.read_csv('filepath.csv')

# Input df for reference range calculation
d = DFmaker(df_in)
df_exp = d.df_out()
# Generates CSV
df_exp.to_csv (r'output.csv', index=False, header=True)
```

## Useful Classes

For more information to use other statistical features look into the `Biostatistics`
class under the `stat_functions` file
Understand the `DFmaker` class for inputting subcategories of `sex` and `age_group` follow standard database format

## Main Class

Always make sure that the biomarkers are up to date in the `MYBiomarkers.csv` file. Code will fail if any new biomarkers are not added and updated to the file first.

If more columns are needed at the exported file then simply add columns to the column extension (second last line in main)

## Documentation

`BiostatisticsMY-Documentation.pdf` has all the function details and what they are supposed to do

## Authors and acknowledgements

Tool develeped by Pranav Dhruv Tandon under the guidance of Anna Prudova, Mai Yamamoto, and Windy Wang

## Contributing

Pull requests are welcome.
Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
