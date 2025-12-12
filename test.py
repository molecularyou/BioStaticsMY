import numpy as np
import scipy as sc
import unittest
from stat_functions import BioStatistics


women_cal_arr = np.array([
    8.8,
    8.9, 8.9,
    9,
    9.1, 9.1, 9.1,
    9.2, 9.2, 9.2, 9.2, 9.2, 9.2, 9.2, 9.2, 9.2, 9.2, 9.2,
    9.3, 9.3, 9.3, 9.3, 9.3, 9.3, 9.3, 9.3, 9.3, 9.3, 9.3,
    9.4, 9.4, 9.4, 9.4, 9.4, 9.4, 9.4, 9.4,
    9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5,
    9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5,
    9.6, 9.6, 9.6, 9.6, 9.6, 9.6, 9.6, 9.6,
    9.6, 9.6, 9.6, 9.6, 9.6, 9.6, 9.6, 9.6,
    9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7,
    9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7,
    9.8, 9.8, 9.8, 9.8, 9.8, 9.8, 9.8, 9.8,
    9.9, 9.9, 9.9, 9.9, 9.9, 9.9, 9.9,
    10, 10, 10,
    10.1, 10.1,
    10.2, 10.2, 10.2,
    10.3, 10.3
])

men_cal_arr = np.array([
    9.1, 9.1,
    9.2,
    9.3, 9.3, 9.3, 9.3, 9.3, 9.3, 9.3, 9.3,
    9.4, 9.4, 9.4, 9.4, 9.4, 9.4,
    9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5,
    9.6, 9.6, 9.6, 9.6, 9.6, 9.6, 9.6, 9.6, 9.6, 9.6, 9.6, 9.6,
    9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7,
    9.8, 9.8, 9.8, 9.8, 9.8, 9.8, 9.8, 9.8,
    9.8, 9.8, 9.8, 9.8, 9.8, 9.8, 9.8, 9.8,
    9.9, 9.9, 9.9, 9.9, 9.9, 9.9, 9.9, 9.9, 9.9, 9.9, 9.9, 9.9, 9.9, 9.9,
    10, 10, 10, 10, 10, 10, 10,
    10.1, 10.1, 10.1, 10.1, 10.1, 10.1, 10.1, 10.1, 10.1, 10.1,
    10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2,
    10.3, 10.3, 10.3, 10.3, 10.3, 10.3, 10.3,
    10.4,
    10.6
])

cal_arr_combo = np.array([
    8.8,
    8.9, 8.9,
    9,
    9.1, 9.1, 9.1, 9.1, 9.1,
    9.2, 9.2, 9.2, 9.2, 9.2, 9.2, 9.2, 9.2, 9.2, 9.2, 9.2, 9.2,
    9.3, 9.3, 9.3, 9.3, 9.3, 9.3, 9.3, 9.3, 9.3, 9.3,
    9.3, 9.3, 9.3, 9.3, 9.3, 9.3, 9.3, 9.3, 9.3,
    9.4, 9.4, 9.4, 9.4, 9.4, 9.4, 9.4, 9.4, 9.4, 9.4, 9.4, 9.4, 9.4, 9.4,
    9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5,
    9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5,
    9.6, 9.6, 9.6, 9.6, 9.6, 9.6, 9.6, 9.6, 9.6, 9.6, 9.6, 9.6, 9.6, 9.6,
    9.6, 9.6, 9.6, 9.6, 9.6, 9.6, 9.6, 9.6, 9.6, 9.6, 9.6, 9.6, 9.6, 9.6,
    9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7,
    9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7,
    9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7,
    9.8, 9.8, 9.8, 9.8, 9.8, 9.8, 9.8, 9.8, 9.8, 9.8, 9.8, 9.8,
    9.8, 9.8, 9.8, 9.8, 9.8, 9.8, 9.8, 9.8, 9.8, 9.8, 9.8, 9.8,
    9.9, 9.9, 9.9, 9.9, 9.9, 9.9, 9.9, 9.9, 9.9, 9.9, 9.9,
    9.9, 9.9, 9.9, 9.9, 9.9, 9.9, 9.9, 9.9, 9.9, 9.9,
    10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
    10.1, 10.1, 10.1, 10.1, 10.1, 10.1, 10.1, 10.1, 10.1, 10.1, 10.1, 10.1,
    10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2,
    10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2,
    10.3, 10.3, 10.3, 10.3, 10.3, 10.3, 10.3, 10.3, 10.3,
    10.4,
    10.6
])

women_al_arr = np.array([
    5,
    6, 6, 6,
    7,
    8, 8, 8, 8, 8,
    9, 9,
    10, 10,
    11, 11, 11, 11, 11, 11, 11,
    12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12,
    13, 13, 13, 13, 13, 13, 13, 13, 13, 13,
    14, 14, 14, 14, 14, 14, 14,
    15, 15, 15, 15, 15, 15, 15,
    16, 16, 16, 16, 16, 16, 16,
    17, 17, 17, 17, 17, 17, 17, 17,
    18, 18, 18, 18, 18, 18,
    19, 19, 19, 19, 19, 19, 19,
    20, 20, 20, 20, 20,
    21, 21, 21, 21, 21, 21,
    22, 22, 22, 22,
    23, 23, 23, 23,
    25, 25, 25,
    26, 26,
    28, 28,
    29,
    30, 30,
    36,
    37, 37,
    39,
    46,
    47,
    65
])

men_al_arr = np.array([
    9,
    10, 10,
    11, 11, 11, 11,
    12, 12,
    13, 13, 13,
    14, 14, 14, 14, 14, 14,
    15, 15, 15,
    16, 16, 16, 16,
    17,
    18, 18, 18, 18,
    19, 19, 19, 19, 19, 19,
    20, 20, 20, 20, 20, 20, 20, 20, 20, 20,
    21, 21, 21, 21, 21,
    22, 22, 22, 22,
    23,
    24, 24, 24,
    25, 25, 25, 25, 25, 25, 25, 25,
    26, 26, 26,
    27,
    28, 28, 28, 28,
    29,
    30, 30, 30,
    31, 31, 31, 31, 31,
    32,
    33,
    34, 34,
    35, 35,
    36, 36, 36, 36, 36,
    37,
    38, 38,
    39, 39,
    40, 40, 40,
    41,
    42,
    45, 45,
    47,
    48, 48,
    49,
    51, 51, 51,
    53,
    54,
    55, 55,
    62,
    69
])

al_arr_combo = np.array([
    5,
    6, 6, 6,
    7,
    8, 8, 8, 8, 8,
    9, 9, 9,
    10, 10, 10, 10,
    11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11,
    12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12,
    13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13,
    14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14,
    15, 15, 15, 15, 15, 15, 15, 15, 15, 15,
    16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16,
    17, 17, 17, 17, 17, 17, 17, 17, 17,
    18, 18, 18, 18, 18, 18, 18, 18, 18, 18,
    19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19,
    20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20,
    21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21,
    22, 22, 22, 22, 22, 22, 22, 22,
    23, 23, 23, 23, 23,
    24, 24, 24,
    25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25,
    26, 26, 26, 26, 26,
    27,
    28, 28, 28, 28, 28, 28,
    29, 29,
    30, 30, 30, 30, 30,
    31, 31, 31, 31, 31,
    32,
    33,
    34, 34,
    35, 35,
    36, 36, 36, 36, 36, 36,
    37, 37, 37,
    38, 38,
    39, 39, 39,
    40, 40, 40,
    41,
    42,
    45, 45,
    46,
    47, 47,
    48, 48,
    49,
    51, 51, 51,
    53,
    54,
    55, 55,
    62,
    65,
    69
])


class TestRI(unittest.TestCase):
    """
    Test data reproduces the data used to calculate the 95% reference intervals
    for calcium and alanine aminotransferase (AlaAT) on page 20 in the CLSI
    documentation. However, BioStatistics now uses a different methodology to
    calculate reference intervals, and thus the intervals (i.e. lower and upper
    limits) in the test_RI methods differ from the paper.

    Original URL: https://docs.ufpr.br/~taconeli/CE06219/Artigo_FR3.pdf
    """
    def test_RI_cal_combo(self):
        t_combo_cal = BioStatistics(cal_arr_combo)
        lower_limit, upper_limit = t_combo_cal.reference_interval()
        self.assertEqual(round(lower_limit, 2), 9.1, 'Should be 9.1')
        self.assertEqual(round(upper_limit, 2), 10.3, 'Should be 10.3')

    def test_RI_cal_men(self):
        t_men_cal = BioStatistics(men_cal_arr)
        lower_limit, upper_limit = t_men_cal.reference_interval()
        self.assertEqual(round(lower_limit, 2), 9.3, 'Should be 9.3')
        self.assertEqual(round(upper_limit, 2), 10.3, 'Should be 10.3')

    def test_RI_cal_women(self):
        t_women_cal = BioStatistics(women_cal_arr)
        lower_limit, upper_limit = t_women_cal.reference_interval()
        self.assertEqual(round(lower_limit, 2), 9.0, 'Should be 9.0')
        self.assertEqual(round(upper_limit, 2), 10.2, 'Should be 10.2')

    def test_RI_al_combo(self):
        t_combo_al = BioStatistics(al_arr_combo)
        lower_limit, upper_limit = t_combo_al.reference_interval()
        self.assertEqual(round(lower_limit), 8, 'Should be 8')
        self.assertEqual(round(upper_limit), 53, 'Should be 53')

    def test_RI_al_men(self):
        t_men_al = BioStatistics(men_al_arr)
        lower_limit, upper_limit = t_men_al.reference_interval()
        self.assertEqual(round(lower_limit), 11, 'Should be 11')
        self.assertEqual(round(upper_limit), 55, 'Should be 55')

    def test_RI_al_women(self):
        t_women_al = BioStatistics(women_al_arr)
        lower_limit, upper_limit = t_women_al.reference_interval()
        self.assertEqual(round(lower_limit), 6, 'Should be 6')
        self.assertEqual(round(upper_limit), 39, 'Should be 39')

    def test_min_max_val(self):
        t_combo_cal = BioStatistics(cal_arr_combo)
        self.assertEqual(t_combo_cal.max_val(), 10.6, 'Should be 10.6')
        self.assertEqual(t_combo_cal.min_val(), 8.8, 'Should be 8.8')

    def test_mean(self):
        t_combo_cal = BioStatistics(cal_arr_combo)
        self.assertEqual(
            t_combo_cal.mean(),
            9.684166666666666,
            'Should be 9.684166666666666'
        )

    def test_median(self):
        t_combo_cal = BioStatistics(cal_arr_combo)
        self.assertEqual(t_combo_cal.median(), 9.7, 'Should be 9.7')

    def test_sd(self):
        t_combo_cal = BioStatistics(cal_arr_combo)
        self.assertEqual(
            t_combo_cal.sd(),
            0.32223072306794226,
            'Should be 0.32223072306794226'
        )

    def test_var(self):
        t_combo_cal = BioStatistics(cal_arr_combo)
        self.assertEqual(
            t_combo_cal.var(),
            0.10383263888888888,
            'Should be 0.10383263888888888'
        )

    def test_lg_trans(self):
        t_combo_cal = BioStatistics(cal_arr_combo)

        np.testing.assert_array_equal(
            t_combo_cal.log_transform(),
            np.log(cal_arr_combo.astype(float)),
            "Array should match"
        )

    def test_exp_trans(self):
        t_combo_cal = BioStatistics(cal_arr_combo)
        np.testing.assert_array_equal(
            t_combo_cal.exp_transform(),
            np.exp(cal_arr_combo.astype(float)),
            'Array should match'
        )

    def test_sq_root_trans(self):
        t_combo_cal = BioStatistics(cal_arr_combo)
        np.testing.assert_array_equal(
            t_combo_cal.square_root_transform(),
            np.sqrt(cal_arr_combo.astype(float)),
            'Array should match'
        )

    def test_cub_root_trans(self):
        t_combo_cal = BioStatistics(cal_arr_combo)
        np.testing.assert_array_equal(
            t_combo_cal.cube_root_transform(),
            np.cbrt(cal_arr_combo.astype(float)),
            'Array should match'
        )

    def test_f_score(self):
        t_combo_cal = BioStatistics(cal_arr_combo)
        np.testing.assert_array_equal(
            t_combo_cal.z_score(),
            sc.stats.zscore(cal_arr_combo.astype(float)),
            'Array should match'
        )

    def test_norm(self):
        t_combo_cal = BioStatistics(cal_arr_combo)
        np.testing.assert_array_equal(
            t_combo_cal.normalize(),
            t_combo_cal.normalize(),
            'Array should match'
        )

    def test_co_eff_skewness_kurt(self):
        t_combo_cal = BioStatistics(cal_arr_combo)
        np.testing.assert_array_equal(
            t_combo_cal.co_eff_skewness(),
            t_combo_cal.co_eff_skewness(),
            'Array should match'
        )
        np.testing.assert_array_equal(
            t_combo_cal.co_eff_kurtosis(),
            t_combo_cal.co_eff_kurtosis(),
            'Array should match'
        )

    def test_shap_wilk(self):
        t_combo_cal = BioStatistics(cal_arr_combo)
        np.testing.assert_array_equal(
            t_combo_cal.shapiro_wilk_test(),
            t_combo_cal.shapiro_wilk_test(),
            'Array should match'
        )

    def test_is_normally_distributed(self):
        normally_distributed_data = BioStatistics(np.random.normal(size=300))
        skewed_data = BioStatistics(np.random.uniform(size=300))
        self.assertEqual(
            normally_distributed_data.is_normally_distributed(),
            True,
            'Should be True'
        )
        self.assertEqual(
            skewed_data.is_normally_distributed(),
            False,
            'Should be False'
        )

    def test_ci_percentiles(self):
        lower_percentile, upper_percentile = BioStatistics([]).ci_percentiles(95)
        self.assertEqual(lower_percentile, 2.5, 'Should be 2.5')
        self.assertEqual(upper_percentile, 97.5, 'Should be 97.5')

    def test_blq_replacement_value(self):
        self.assertEqual(
            BioStatistics([]).blq_replacement_value(),
            'nan',
            'Should be nan'
        )
        self.assertEqual(
            BioStatistics([]).blq_replacement_value(5),
            2.5,
            'Should be 2.5'
        )

    def test_alq_replacement_value(self):
        self.assertEqual(
            BioStatistics([]).alq_replacement_value(),
            'nan',
            'Should be nan'
        )
        self.assertEqual(
            BioStatistics([]).alq_replacement_value(5),
            7.5,
            'Should be 7.5'
        )

    def test_replace_string_value_in_array(self):
        alq_array = np.array([1, 'ALQ ( 40820 )', 'ALQ ( 64010 )'])
        blq_nd_array = np.array([1, 'ND', 'BLQ < 14.53'])

        np.testing.assert_array_equal(
            BioStatistics([]).replace_string_value_in_array(
                alq_array, 'ALQ', 'nan'
            ),
            np.array(['1', 'nan', 'nan']),
            'Array should match'
        )
        np.testing.assert_array_equal(
            BioStatistics([]).replace_string_value_in_array(
                alq_array, 'ALQ', 7.5
            ),
            np.array(['1', '7.5', '7.5']),
            'Array should match'
        )

        np.testing.assert_array_equal(
            BioStatistics([]).replace_string_value_in_array(
                blq_nd_array, '<', 'nan'
            ),
            np.array(['1', 'ND', 'nan']),
            'Array should match'
        )
        np.testing.assert_array_equal(
            BioStatistics([]).replace_string_value_in_array(
                blq_nd_array, '<', 2.5
            ),
            np.array(['1', 'ND', '2.5']),
            'Array should match'
        )

        np.testing.assert_array_equal(
            BioStatistics([]).replace_string_value_in_array(
                blq_nd_array, 'ND', 'nan'
            ),
            np.array(['1', 'nan', 'BLQ < 14.53']),
            'Array should match'
        )
        np.testing.assert_array_equal(
            BioStatistics([]).replace_string_value_in_array(
                blq_nd_array, 'ND', 2.5
            ),
            np.array(['1', '2.5', 'BLQ < 14.53']),
            'Array should match'
        )

    def test_replace_zeros(self):
        data = np.array([1, 0, 0])
        np.testing.assert_array_equal(
            BioStatistics([]).replace_zeros(data, 'nan'),
            np.array([1, 'nan', 'nan']).astype(float),
            'Array should match'
        )
        np.testing.assert_array_equal(
            BioStatistics([]).replace_zeros(data, 2.5),
            np.array([1, 2.5, 2.5]),
            'Array should match'
        )

    def test_clean_array(self):
        data = np.array([1, 'ND', 'BLQ < 73.525', 'ALQ ( 40820 )', 'NR'])
        np.testing.assert_array_equal(
            BioStatistics(data).clean_array(),
            np.array([1, 'nan', 'nan', 'nan', 'nan']).astype(float),
            'Array should match'
        )
        np.testing.assert_array_equal(
            BioStatistics(data).clean_array(5, 5),
            np.array([1, 2.5, 2.5, 7.5, 'nan']).astype(float),
            'Array should match'
        )


if __name__ == '__main__':
    unittest.main()
