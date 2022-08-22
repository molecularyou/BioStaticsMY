from stat_functions import *
import unittest

women_cal_arr = np.array(
    [8.8, 8.9, 8.9, 9, 9.1, 9.1, 9.1, 9.2, 9.2, 9.2, 9.2, 9.2, 9.2, 9.2, 9.2, 9.2, 9.2, 9.2, 9.3, 9.3,
     9.3, 9.3, 9.3, 9.3, 9.3, 9.3, 9.3, 9.3, 9.3, 9.4, 9.4, 9.4, 9.4, 9.4, 9.4, 9.4, 9.4, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5,
     9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5,
     9.6, 9.6, 9.6, 9.6, 9.6, 9.6, 9.6, 9.6, 9.6, 9.6, 9.6, 9.6, 9.6, 9.6, 9.6, 9.6, 9.7,
     9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7,
     9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.8, 9.8, 9.8, 9.8, 9.8, 9.8, 9.8, 9.8, 9.9, 9.9, 9.9, 9.9, 9.9,
     9.9, 9.9, 10, 10, 10, 10.1, 10.1, 10.2, 10.2, 10.2, 10.3, 10.3])

men_cal_arr = np.array([9.1, 9.1, 9.2, 9.3, 9.3, 9.3, 9.3, 9.3, 9.3, 9.3, 9.3, 9.4, 9.4, 9.4, 9.4, 9.4, 9.4, 9.5, 9.5,
                        9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.6, 9.6, 9.6, 9.6, 9.6, 9.6, 9.6, 9.6,
                        9.6, 9.6, 9.6, 9.6, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.8, 9.8,
                        9.8, 9.8, 9.8, 9.8, 9.8, 9.8, 9.8, 9.8, 9.8, 9.8, 9.8, 9.8, 9.8, 9.8, 9.9, 9.9, 9.9, 9.9, 9.9,
                        9.9,
                        9.9, 9.9, 9.9, 9.9, 9.9, 9.9, 9.9, 9.9, 10, 10, 10, 10, 10, 10, 10, 10.1, 10.1, 10.1, 10.1,
                        10.1, 10.1,
                        10.1, 10.1, 10.1, 10.1, 10.2, 10.2,
                        10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2,
                        10.2, 10.3, 10.3, 10.3, 10.3, 10.3, 10.3, 10.3, 10.4, 10.6])

cal_arr_combo = np.array(
    [8.8, 8.9, 8.9, 9, 9.1, 9.1, 9.1, 9.1, 9.1, 9.2, 9.2, 9.2, 9.2, 9.2, 9.2, 9.2, 9.2, 9.2, 9.2, 9.2, 9.2, 9.3, 9.3,
     9.3, 9.3, 9.3, 9.3, 9.3,
     9.3, 9.3, 9.3, 9.3, 9.3, 9.3, 9.3, 9.3, 9.3, 9.3, 9.3, 9.3, 9.4, 9.4, 9.4, 9.4, 9.4, 9.4, 9.4, 9.4, 9.4, 9.4, 9.4,
     9.4, 9.4, 9.4, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5,
     9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.6, 9.6, 9.6, 9.6, 9.6, 9.6, 9.6, 9.6, 9.6, 9.6, 9.6,
     9.6, 9.6, 9.6, 9.6, 9.6,
     9.6, 9.6, 9.6, 9.6, 9.6, 9.6, 9.6, 9.6, 9.6, 9.6, 9.6, 9.6, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7,
     9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7,
     9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.7, 9.8, 9.8, 9.8, 9.8,
     9.8, 9.8, 9.8, 9.8, 9.8, 9.8, 9.8, 9.8, 9.8, 9.8, 9.8, 9.8, 9.8, 9.8, 9.8, 9.8, 9.8, 9.8, 9.8, 9.8, 9.9, 9.9, 9.9,
     9.9, 9.9, 9.9, 9.9, 9.9, 9.9, 9.9, 9.9, 9.9, 9.9, 9.9, 9.9, 9.9, 9.9,
     9.9, 9.9, 9.9, 9.9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10.1, 10.1, 10.1, 10.1, 10.1, 10.1, 10.1,
     10.1, 10.1, 10.1, 10.1, 10.1, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2,
     10.3, 10.3, 10.3, 10.3, 10.3, 10.3, 10.3, 10.3, 10.3, 10.4, 10.6])

women_al_arr = np.array(
    [5, 6, 6, 6, 7, 8, 8, 8, 8, 8, 9, 9, 10, 10, 11, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12,
     13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 14, 14, 14, 14, 14, 14, 14, 15, 15,
     15, 15, 15, 15, 15, 16, 16, 16, 16, 16, 16, 16, 17, 17, 17, 17, 17, 17,
     17, 17, 18, 18, 18, 18, 18, 18, 19, 19, 19, 19, 19, 19, 19, 20, 20, 20, 20, 20, 21, 21, 21, 21, 21, 21, 22, 22, 22,
     22, 23, 23, 23, 23, 25, 25, 25,
     26, 26, 28, 28, 29, 30, 30, 36, 37, 37, 39, 46, 47, 65])

men_al_arr = np.array(
    [9, 10, 10, 11, 11, 11, 11, 12, 12, 13, 13, 13, 14, 14, 14, 14, 14, 14, 15, 15, 15, 16, 16, 16, 16, 17, 18, 18, 18,
     18, 19, 19, 19, 19, 19, 19, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 21, 21, 21, 21, 21, 22, 22, 22, 22, 23, 24, 24,
     24, 25, 25, 25,
     25, 25, 25, 25, 25, 26, 26, 26, 27, 28, 28, 28, 28, 29, 30, 30, 30, 31, 31, 31, 31, 31, 32, 33, 34, 34, 35, 35, 36,
     36, 36, 36, 36, 37, 38, 38, 39, 39, 40, 40, 40, 41, 42, 45, 45, 47, 48, 48, 49,
     51, 51, 51, 53, 54, 55, 55, 62, 69])

al_arr_combo = np.array(
    [5, 6, 6, 6, 7, 8, 8, 8, 8, 8, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12,
     12, 12, 12, 12, 12, 12, 12, 12, 12, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 14, 14, 14, 14, 14, 14, 14,
     14, 14, 14, 14, 14, 14, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 17, 17,
     17, 17, 17, 17, 17, 17, 17, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19,
     19, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 22, 22,
     22, 22, 22, 22, 22, 22, 23, 23,
     23, 23, 23, 24, 24, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 26, 26, 26, 26, 26, 27, 28, 28, 28, 28, 28, 28,
     29, 29, 30, 30, 30, 30, 30, 31, 31, 31, 31, 31, 32, 33, 34, 34, 35, 35, 36, 36, 36, 36, 36, 36, 37, 37, 37, 38, 38,
     39, 39, 39, 40, 40, 40, 41, 42, 45, 45, 46, 47, 47, 48, 48, 49, 51, 51, 51,
     53, 54, 55, 55, 62, 65, 69])




class TestRI(unittest.TestCase):

    def test_RI_cal_combo(self):
        """
            Testing the functions using the CLSI documentation
            URL:https://docs.ufpr.br/~taconeli/CE06219/Artigo_FR3.pdf
            Testing for Calcium can refer pg 20 in the URL
        """
        t_combo_cal = BioStatistics(cal_arr_combo)
        self.assertEqual(t_combo_cal.high_lim(), 10.3, "Should be 10.3")
        self.assertEqual(t_combo_cal.low_lim(), 9.1, "Should be 9.1")

    def test_RI_cal_men(self):
        t_men_cal = BioStatistics(men_cal_arr)
        self.assertEqual(t_men_cal.high_lim(), 10.3, "Should be 10.3")
        self.assertEqual(t_men_cal.low_lim(), 9.2, "Should be 9.2")

    def test_RI_cal_women(self):
        t_women_cal = BioStatistics(women_cal_arr)
        self.assertEqual(t_women_cal.high_lim(), 10.2, "Should be 10.2")
        self.assertEqual(t_women_cal.low_lim(), 8.9, "Should be 8.9")

    def test_RI_al_combo(self):
        """
            Testing the functions using the CLSI documentation
            URL:https://docs.ufpr.br/~taconeli/CE06219/Artigo_FR3.pdf
            Testing for Alanine (AlaAT) can refer pg 20 in the URL
        """
        t_combo_al = BioStatistics(al_arr_combo)
        self.assertEqual(t_combo_al.high_lim(), 54, "Should be 54")
        self.assertEqual(t_combo_al.low_lim(), 8, "Should be 8")

    def test_RI_al_men(self):
        t_men_al = BioStatistics(men_al_arr)
        self.assertEqual(t_men_al.high_lim(), 55, "Should be 55")
        self.assertEqual(t_men_al.low_lim(), 10, "Should be 10")

    def test_RI_al_women(self):
        t_women_al = BioStatistics(women_al_arr)
        self.assertEqual(t_women_al.high_lim(), 46, "Should be 46")
        self.assertEqual(t_women_al.low_lim(), 6, "Should be 6")

    def test_min_max_val(self):

        t_combo_cal = BioStatistics(cal_arr_combo)
        self.assertEqual(t_combo_cal.max_val(), 10.6, "Should be 10.6")
        self.assertEqual(t_combo_cal.min_val(), 8.8, "Should be 8.8")

    def test_mean(self):
        t_combo_cal = BioStatistics(cal_arr_combo)
        self.assertEqual(t_combo_cal.mean(), 9.684166666666666, "Should be 9.684166666666666")

    def test_median(self):
        t_combo_cal = BioStatistics(cal_arr_combo)
        self.assertEqual(t_combo_cal.median(), 9.7, "Should be 9.7")

    def test_sd(self):
        t_combo_cal = BioStatistics(cal_arr_combo)
        self.assertEqual(t_combo_cal.sd(), 0.32223072306794226, "Should be 0.32223072306794226")

    def test_var(self):
        t_combo_cal = BioStatistics(cal_arr_combo)
        self.assertEqual(t_combo_cal.var(), 0.10383263888888888, "Should be 0.10383263888888888")

    def test_lg_trans(self):
        t_combo_cal = BioStatistics(cal_arr_combo)
        np.testing.assert_array_equal(t_combo_cal.log_transform(), np.log(cal_arr_combo.astype(float)), "Array should match")

    def test_exp_trans(self):
        t_combo_cal = BioStatistics(cal_arr_combo)
        np.testing.assert_array_equal(t_combo_cal.exp_transform(), np.exp(cal_arr_combo.astype(float)), "Array should match")

    def test_sq_root_trans(self):
        t_combo_cal = BioStatistics(cal_arr_combo)
        np.testing.assert_array_equal(t_combo_cal.square_root_transform(), np.sqrt(cal_arr_combo.astype(float)), "Array should match")

    def test_cub_root_trans(self):
        t_combo_cal = BioStatistics(cal_arr_combo)
        np.testing.assert_array_equal(t_combo_cal.cube_root_transform(), np.cbrt(cal_arr_combo.astype(float)), "Array should match")

    def test_f_score(self):
        t_combo_cal = BioStatistics(cal_arr_combo)
        np.testing.assert_array_equal(t_combo_cal.z_score(), sc.stats.zscore(cal_arr_combo.astype(float)), "Array should match")

    def test_norm(self):
        t_combo_cal = BioStatistics(cal_arr_combo)
        np.testing.assert_array_equal(t_combo_cal.normalize(), t_combo_cal.normalize(), "Array should match")

    def test_co_eff_skewness_kurt(self):
        t_combo_cal = BioStatistics(cal_arr_combo)
        np.testing.assert_array_equal(t_combo_cal.co_eff_skewness(), t_combo_cal.co_eff_skewness(),
                                      "Array should match")
        np.testing.assert_array_equal(t_combo_cal.co_eff_kurtosis(), t_combo_cal.co_eff_kurtosis(),
                                      "Array should match")


    def test_shap_wilk(self):
        t_combo_cal = BioStatistics(cal_arr_combo)
        np.testing.assert_array_equal(t_combo_cal.shapiro_wilk_test(), t_combo_cal.shapiro_wilk_test(),
                                      "Array should match")



if __name__ == '__main__':
    unittest.main()
