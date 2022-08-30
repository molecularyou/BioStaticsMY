import numpy as np
import scipy as sc
from scipy import stats
import pandas as pd


class BioStatistics:
    """
                          This class has all the statistical functions that are required. Any future to add more features work should be added on top of this
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
               Calculates the coefficient of kurtosis
            """
        shap_wilk_val = sc.stats.shapiro(self.array)
        return shap_wilk_val

    def RI(self):
        """
                   Calculates reference interval in accordance to CLSI guidelines
        """
        global low_RI, high_RI, n
        n = self.array.size
        val = round((n + 1) * .025)
        low_RI = self.array[val - 1]
        high_RI = self.array[n - val]

    def low_lim(self):
        """
                          Returns lower limit of the Reference Range
                """
        self.RI()
        return low_RI

    def high_lim(self):
        """
                                  Returns lower limit of the Reference Range
                        """
        self.RI()
        return high_RI

    def para_outlier(self):
        """
                       Removes outliers accordance to CLSI guidelines
        """
        self.RI()
        low = low_RI
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
                          Makes the DataFrame for processing by the Biostatists
                          @:param df_in is the input dataframe
                          @:param age is the age subcategory "Adult" or "Child"
                          @:param sex is the sex subcategory "Male" or "Female"
                          @:param biofluid is the type of fluid being analysed "serum" or "plasma"

            """
    def __init__(self, df_in, age=None, sex=None, biofluid=None):
        self.df_in = df_in
        self.age = age
        self.sex = sex
        self.biofluid = biofluid




    def df_out(self):
        """
        This is where the processing for the Reference Range happens
        Remember:Adding MY biomarkers to update the list add the Biomarker and ID in the MY Biomarkers file"""

        df_bioMarker = pd.read_csv('MYBiomarkers.csv')
        temp_dict = dict(zip(df_bioMarker.Biomarker, df_bioMarker.MYID))

        self.df_in = pd.DataFrame(self.df_in)

        df = self.df_in.T
        ref_df = self.df_in

        ref_df.drop(ref_df[ref_df['sex'] != self.sex].index, inplace=True)

        ref_df.drop(ref_df[ref_df['age_group'] != self.age].index, inplace=True)


        ref_df = ref_df.drop(['Test ID', 'sex', 'age_group'], axis=1)



        col_list = ref_df.columns.to_list()

        ref_dic = {}

        i = 3
        j = len(df)
        z = 0
        while i < j:
            p = BioStatistics(df.iloc[i].to_numpy())

            if col_list[z] in temp_dict.keys():
                ref_dic.update({col_list[z]: [temp_dict[col_list[z]], str(p.low_lim()) + " - " + str(p.high_lim()), self.age, self.sex, self.biofluid, "Calculated", "1"]})
            #     add column keys in the dictionary above
            i = i + 1
            z = z + 1
            if i > j + 1:
                break

        return pd.DataFrame.from_dict(ref_dic)

