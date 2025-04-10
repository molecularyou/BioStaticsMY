import csv
import numpy as np
import scipy as sc
import pandas as pd

DEFAULT_CI = 95
DEFAULT_AGE = 'Adult'
DEFAULT_SEX = 'Both'
DEFAULT_BIOFLUID = 'plasma'
DEFAULT_UNITS = 'nM'
DEFAULT_CATEGORY = 'Calculated'
DEFAULT_REFERENCE = 'BioStatistics'
DEFAULT_EXPORTED = '1'


class BioStatistics:
    """
    This class has all the statistical functions that are required.
    New features should be added on top of this
    and then be manipulated inside the DFmaker class
    """

    def __init__(self, array):
        self.array = array
        self.array.sort()

    def max_val(self):
        """
        Calculates the max of an array/vector
        """
        arr = np.array(self.array)
        result = np.max(arr)
        return result

    def min_val(self):
        """
        Calculates the min of an array/vector
        """
        arr = np.array(self.array)
        result = np.min(arr)
        return result

    def mean(self):
        """
        Calculates the mean of an array/vector
        """
        arr = np.array(self.array)
        result = np.mean(arr)
        return result

    def sd(self):
        """
        Calculates the standard deviation of an array/vector
        """
        arr = np.array(self.array)
        result = np.std(arr)
        return result

    def median(self):
        """
        Calculates the median of an array/vector
        """
        arr = np.array(self.array)
        result = np.median(arr)
        return result

    def var(self):
        """
        Calculates the variance of an array/vector
        """
        result = np.var(self.array)
        return result

    def iqr(self):
        """
        Calculates the inter-quartile range of an array/vector
        """
        arr = np.array(self.array)
        result = np.percentile(arr, 75) - np.percentile(arr, 25)
        return result

    def log_transform(self, lloq=None):
        """
        Log transformation of the data

        Converts all zeroes to the biomarker LLOQ / 2 if present,
        otherwise converts zeroes to nan
        """
        float_array = self.array.astype(float)

        if self.contains_zeroes():
            if not lloq:
                replacement_value = 'nan'
            else:
                replacement_value = float(lloq) / 2

            float_array[float_array == 0] = replacement_value

        return np.log(float_array)

    def exp_transform(self):
        """
        Exponential transformation of the data
        """
        ex_transform = np.exp(self.array.astype(float))
        return ex_transform

    def square_root_transform(self):
        """
        Square Root Transformation of the data
        remember to square data after processing
        """
        sq_transform = np.sqrt(self.array)
        return sq_transform

    def cube_root_transform(self):
        """
        Cube Root Transformation of the data
        """
        cb_transform = np.cbrt(self.array)
        return cb_transform

    def z_score(self):
        """
        Calculates the z score
        """
        score = sc.stats.zscore(self.array)
        return score

    def normalize(self):
        """
        Normalizes the array
        """
        data = self.array
        data_norm = (data - data.min()) / (data.max() - data.min())
        return data_norm

    def co_eff_skewness(self):
        """
        Calculates the coefficient of skewness
        """
        skewed_val = sc.stats.skew(self.array)
        return skewed_val

    def co_eff_kurtosis(self):
        """
        Calculates the coefficient of kurtosis
        """
        kurt_val = sc.stats.kurtosis(self.array)
        return kurt_val

    def shapiro_wilk_test(self):
        """
        Calculates whether a data set is normally distributed
        """
        shap_wilk_val = sc.stats.shapiro(self.array)
        return shap_wilk_val

    def is_normally_distributed(self):
        return True if self.shapiro_wilk_test().pvalue > 0.05 else False

    def contains_zeroes(self):
        return False if np.all(self.array) else True

    def ci_percentiles(self, confidence_interval):
        """
        Calculates lower and upper percentiles given a confidence interval
        e.g. For 95% CI, lower percentile = (100 - 95) / 2 = 2.5
        e.g. For 95% CI, upper percentile = 100 - 2.5 = 97.5
        """
        lower_percentile = (100 - confidence_interval) / 2
        upper_percentile = 100 - lower_percentile
        return lower_percentile, upper_percentile

    def reference_interval(self):
        """
        Calculates reference interval in accordance to CLSI guidelines
        """
        lower_percentile, upper_percentile = self.ci_percentiles(DEFAULT_CI)

        n = self.array.size
        val = round((n + 1) * .025)
        low_RI = self.array[val - 1]
        high_RI = self.array[n - val]
        return low_RI, high_RI

    def para_outlier(self):
        """
        Removes outliers accordance to CLSI guidelines
        """
        n = self.array.size
        _lower_limit, upper_limit = self.reference_interval()

        high = upper_limit
        i = 0
        while i < n - 2:
            current_val = self.array[i]
            next_val = self.array[i + 1]
            try:
                test_val = (next_val - current_val) / (high - current_val)
            except ZeroDivisionError:
                test_val = 0
            if test_val > 1 / 3:
                current_val = -100
            i += 1

        return self.array


class DFmaker:
    """
    Makes the DataFrame for processing by the Biostatistics

    @:param df_in is the input dataframe
    @:param age is "Adult" or "Child"
    @:param sex is "Male", "Female", or "Both"
    @:param biofluid is the type of fluid being analyzed "serum" or "plasma"
    @:param units is the concentration units
    """
    def __init__(self, df_in, age=None, sex=None, biofluid=None, units=None):
        self.df_in = df_in
        self.age = age or DEFAULT_AGE
        self.sex = sex or DEFAULT_SEX
        self.biofluid = biofluid or DEFAULT_BIOFLUID
        self.units = units or DEFAULT_UNITS

    def biomarker_dict(self):
        """
        Creates a dictionary of biomarker names mapped to IDs and LLOQs
        using data stored in MYBiomarkers.csv

        e.g. { 'Alanine': { 'id': 'M00000036', 'lloq': 1.093290116 } }
        """

        biomarker_dict = {}

        with open('MYBiomarkers.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                lloq = None if not row['LLOQ'] else float(row['LLOQ'])

                biomarker_dict[row['Biomarker']] = {
                    "id": row['MYID'],
                    "lloq": lloq
                }

        return biomarker_dict

    def df_out(self):
        """
        This is where the processing for the Reference Range happens
        """
        biomarker_dict = self.biomarker_dict()

        df = self.df_in.T
        ref_df = self.df_in

        ref_df.drop(ref_df[ref_df['sex'] != self.sex].index, inplace=True)

        ref_df.drop(
            ref_df[ref_df['age_group'] != self.age].index,
            inplace=True
        )

        ref_df = ref_df.drop(['Test ID', 'sex', 'age_group'], axis=1)

        col_list = ref_df.columns.to_list()

        ref_dic = {}

        i = 3
        j = len(df)
        z = 0
        while i < j:
            p = BioStatistics(df.iloc[i].to_numpy())

            if col_list[z] in biomarker_dict.keys():
                lower_limit, upper_limit = p.reference_interval()
                ref_dic.update({
                    col_list[z]: [
                        biomarker_dict[col_list[z]]['id'],
                        lower_limit,
                        upper_limit,
                        self.units,
                        self.age,
                        self.sex,
                        self.biofluid,
                        DEFAULT_CATEGORY,
                        DEFAULT_REFERENCE,
                        DEFAULT_EXPORTED
                    ]
                })

            # Add column keys in the dictionary above
            i = i + 1
            z = z + 1
            if i > j + 1:
                break

        return pd.DataFrame.from_dict(ref_dic)
