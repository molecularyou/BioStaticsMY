import numpy as np
import scipy as sc
import pandas as pd

DEFAULT_AGE = 'Adult'
DEFAULT_SEX = 'Both'
DEFAULT_BIOFLUID = 'plasma'
DEFAULT_UNITS = 'fmol/μL'
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

    def log_transform(self):
        """
        Log transformation of the data
        """
        lg_transform = np.log(self.array.astype(float))
        return lg_transform

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

    def RI(self):
        """
        Calculates reference interval in accordance to CLSI guidelines
        """
        n = self.array.size
        val = round((n + 1) * .025)
        low_RI = self.array[val - 1]
        high_RI = self.array[n - val]
        return low_RI, high_RI

    def para_outlier(self):
        """
        Removes outliers accordance to CLSI guidelines
        """
        self.RI()
        high = high_RI
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

    def df_out(self):
        """
        This is where the processing for the Reference Range happens
        Remember: To add MY biomarkers to update the list
        Add the Biomarker and ID in the MY Biomarkers file
        """

        df_biomarkers = pd.read_csv('MYBiomarkers.csv')
        biomarker_name_id_dict = dict(
            zip(df_biomarkers.Biomarker, df_biomarkers.MYID)
        )

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

            if col_list[z] in biomarker_name_id_dict.keys():
                lower_range, upper_range = p.RI()
                ref_dic.update({
                    col_list[z]: [
                        biomarker_name_id_dict[col_list[z]],
                        lower_range,
                        upper_range,
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
