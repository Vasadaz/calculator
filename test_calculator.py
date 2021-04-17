import unittest
from calculator import fun_calculator


class TestCalculator(unittest.TestCase):

    def test_1(self):
        assert fun_calculator("2*2") == 2 * 2  # 4

    def test_2(self):
        assert fun_calculator("(-4)/4") == (-4) / 4  # -1

    def test_3(self):
        assert fun_calculator("(-4)/4**2") == (-4) / 4 ** 2  # -0.25

    def test_4(self):
        assert fun_calculator("3*(-4)/4") == 3 * (-4) / 4  # -3

    def test_5(self):
        assert fun_calculator("(-2)*3*(-4)/6") == (-2) * 3 * (-4) / 6  # 4

    def test_6(self):
        assert fun_calculator("(5+6)*(-9)+20") == (5 + 6) * (-9) + 20  # -79

    def test_7(self):
        assert fun_calculator("5*5+(100/10*(-4 *(-4)))") == \
               5 * 5 + (100 / 10 * (-4 * (-4)))  # 185

    def test_8(self):
        assert fun_calculator("5*5+(100/10*(-4 *(-4))**2)") == \
               5 * 5 + (100 / 10 * (-4 * (-4)) ** 2)  # 2585

    def test_9(self):
        assert fun_calculator("-3+4+(-2+(5-7)*(-4))-1") == \
               -3 + 4 + (-2 + (5 - 7) * (-4)) - 1  # 6

    def test_10(self):
        assert fun_calculator("-2**(-2)") == -2 ** (-2)  # -0.25

    def test_11(self):
        assert fun_calculator("-2**2+10") == -2 ** 2 + 10  # 6

    def test_12(self):
        assert fun_calculator("-(2**2)/4") == -(2 ** 2) / 4  # -1

    def test_13(self):
        assert fun_calculator("3*(-4)/4**2") == 3 * (-4) / 4 ** 2  # -0.75

    def test_14(self):
        assert fun_calculator("-3+4+(-2**(-2)+(5-7)*(-4))-1") == \
               -3 + 4 + (-2 ** (-2) + (5 - 7) * (-4)) - 1  # 7.75

    def test_15(self):
        assert fun_calculator("-(3+4)+(-2**(-2)+(5-7)*(-4))-1") == \
               -(3 + 4) + (-2 ** (-2) + (5 - 7) * (-4)) - 1  # -0.25

    def test_16(self):
        assert fun_calculator("(5+6)*((-9)**(-2))+20") == \
               (5 + 6) * ((-9) ** (-2)) + 20  # 20.135802469135804

    def test_17(self):
        assert fun_calculator("10+(-(2*3+4))+(-(2*3+4))+(-(2*3+4))+(-(2*3+4))") == \
               10 + (-(2 * 3 + 4)) + (-(2 * 3 + 4)) + (-(2 * 3 + 4)) + (-(2 * 3 + 4))  # -30

    def test_18(self):
        assert fun_calculator("-3+4+(-(2**(2))+(5-7)*(-4))-1") == \
                -3 + 4 + (-(2 ** 2) + (5 - 7) * (-4)) - 1  # 4

    def test_19(self):
        assert fun_calculator("-3,50000000000000+4.2+( - (2**(2))+ (5,7-7) * (-4.6    )) - 1") == \
               -3.50000000000000 + 4.2 + (-(2 ** 2) + (5.7 - 7) * (-4.6)) - 1  # 1.6799999999999988

    def test_20(self):
        assert fun_calculator("-(17*3/(42*8/7**3))+105050.000007*8/90**2") == \
               -(17 * 3 / (42 * 8 / 7 ** 3)) + 105050.000007 * 8 / 90 ** 2  # 51.690586426666655

    """
    def test_(self):
        assert fun_calculator("") ==
    """
