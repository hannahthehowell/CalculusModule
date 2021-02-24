import unittest
import math
from maker import make_const, make_quot, make_pwr, make_plus, make_prod
from maker import make_e_expr, make_pwr_expr
from tof import tof
from deriv import deriv
from antideriv import antideriv

class Assign07UnitTests(unittest.TestCase):

    def test_assign_07_prob_01_ut_01(self):
        print('\n***** Assign 07: Problem 01: Unit Test 01 *****')
        fex = make_pwr('x', 2.0)
        print(fex)
        afex = antideriv(fex)
        assert not afex is None
        def gt(x): return (1.0/3.0)*(x**3.0)
        afexf = tof(afex)
        assert not afexf is None
        err = 0.0001
        for i in range(1, 101):
            assert abs(afexf(i) - gt(i)) <= err
        print(afex)
        print('Assign 07: Problem 01: Unit Test 01: pass')

    def test_assign_07_prob_01_ut_02(self):
        print('\n***** Assign 07: Problem 01: Unit Test 02 *****')
        fex = make_pwr('x', 3.0)
        print(fex)
        afex = antideriv(fex)
        assert not afex is None
        def gt(x): return (1.0/4.0)*(x**4.0)
        afexf = tof(afex)
        assert not afexf is None
        err = 0.0001
        for i in range(1, 101):
            assert abs(afexf(i) - gt(i)) <= err
        print(afex)
        print('Assign 07: Problem 01: Unit Test 02: pass')

    def test_assign_07_prob_01_ut_03(self):
        print('\n***** Assign 07: Problem 01: Unit Test 03 *****')
        fex = make_e_expr(make_prod(make_const(-2.0),
                                    make_pwr('x', 1.0)))
        print(fex)
        afex = antideriv(fex)
        assert not afex is None
        def gt(x): return (-0.5)*(math.e**(-2.0*x))
        afexf = tof(afex)
        assert not afexf is None
        err = 0.0001
        for i in range(0, 101):
            assert abs(afexf(i) - gt(i)) <= err
        print(afex)
        print('Assign 07: Problem 01: Unit Test 03: pass')

    def test_assign_07_prob_01_ut_04(self):
        print('\n***** Assign 07: Problem 01: Unit Test 04 *****')
        fex = make_e_expr(make_prod(make_const(-3.0),
                                    make_pwr('x', 1.0)))
        print(fex)
        afex = antideriv(fex)
        assert not afex is None
        def gt(x): return (-1.0/3.0)*(math.e**(-3.0*x))
        afexf = tof(afex)
        assert not afexf is None
        err = 0.0001
        for i in range(0, 101):
            assert abs(afexf(i) - gt(i)) <= err
        print(afex)
        print('Assign 07: Problem 01: Unit Test 04: pass')

    def test_assign_07_prob_01_ut_05(self):
        print('\n***** Assign 07: Problem 01: Unit Test 05 *****')
        fex = make_pwr('x', 0.5)
        print(fex)
        afex = antideriv(fex)
        assert not afex is None
        def gt(x): return (2.0/3.0)*(x**(3.0/2.0))
        afexf = tof(afex)
        assert not afexf is None
        err = 0.0001
        for i in range(1, 101):
            assert abs(afexf(i) - gt(i)) <= err
        print(afex)
        print('Assign 07: Problem 01: Unit Test 05: pass')

    def test_assign_07_prob_01_ut_06(self):
        print('\n***** Assign 07: Problem 01: Unit Test 06 *****')
        fex = make_pwr('x', -2.0)
        print(fex)
        afex = antideriv(fex)
        assert not afex is None
        def gt(x): return -1.0/x
        afexf = tof(afex)
        assert not afexf is None
        err = 0.0001
        for i in range(1, 101):
            assert abs(afexf(i) - gt(i)) <= err
        print(afex)
        print('Assign 07: Problem 01: Unit Test 06: pass')

    def test_assign_07_prob_01_ut_07(self):
        print('\n***** Assign 07: Problem 01: Unit Test 07 *****')
        fex = make_pwr('x', -1.0)
        print(fex)
        afex = antideriv(fex)
        print(afex)
        assert not afex is None
        afexf = tof(afex)
        assert not afexf is None
        def gt(x): return math.log(abs(x), math.e)
        err = 0.0001
        for i in range(1, 101):
            assert abs(afexf(i) - gt(i)) <= err
        for i in range(-101, 0):
            assert abs(afexf(i) - gt(i)) <= err
        print('Assign 07: Problem 01: Unit Test 07: pass')

    def test_assign_07_prob_01_ut_08(self):
        print('\n***** Assign 07: Problem 01: Unit Test 08 *****')
        fex1 = make_pwr('x', -3.0)
        fex2 = make_prod(make_const(7.0),
                         make_e_expr(make_prod(make_const(5.0),
                                               make_pwr('x', 1.0))))
        fex3 = make_prod(make_const(4.0),
                         make_pwr('x', -1.0))
        fex4 = make_plus(fex1, fex2)
        fex = make_plus(fex4, fex3)
        print(fex)
        afex = antideriv(fex)
        assert not afex is None
        print(afex)
        def gt(x):
            v1 = -0.5*(x**(-2.0))
            v2 = (7.0/5.0)*(math.e**(5.0*x))
            v3 = 4.0*(math.log(abs(x), math.e))
            return v1 + v2 + v3
        afexf = tof(afex)
        assert not afexf is None
        err = 0.0001
        for i in range(1, 101):
            #print(afexf(i), gt(i))
            assert abs(afexf(i) - gt(i)) <= err * gt(i)
        print('Assign 07: Problem 01: Unit Test 08: pass')

    def test_assign_07_prob_01_ut_09(self):
        print('\n***** Assign 07: Problem 01: Unit Test 09 *****')
        fex = make_prod(make_const(4.0), make_pwr('x', 3.0))
        print(fex)
        afex = antideriv(fex)
        assert not afex is None
        print(afex)
        fexf = tof(fex)
        assert not fexf is None
        fex2 = deriv(afex)
        assert not fex2 is None
        print(fex2)
        fex2f = tof(fex2)
        assert not fex2f is None
        err = 0.0001
        for i in range(11):
            assert abs(fexf(i) - fex2f(i)) <= err
        print('Assign 07: Problem 01: Unit Test 09: pass')

    def test_assign_07_prob_01_ut_10(self):
        print('\n***** Assign 07: Problem 01: Unit Test 10 *****')
        fex1 = make_plus(make_prod(make_const(5.0),
                                   make_pwr('x', 1.0)),
                         make_const(-7.0))
        fex = make_pwr_expr(fex1, -2.0)
        print(fex)
        afex = antideriv(fex)
        assert not afex is None
        print(afex)
        afexf = tof(afex)
        err = 0.0001
        def gt(x):
            return (-1.0/5.0)*((5*x - 7.0)**-1)
        for i in range(1, 100):
            assert abs(afexf(i) - gt(i)) <= err
        print('Assign 07: Problem 01: Unit Test 10: pass')

    def test_assign_07_prob_01_ut_11(self):
        print('\n***** Assign 07: Problem 01: Unit Test 11 *****')
        fex0 = make_plus(make_pwr('x', 1.0), make_const(2.0))
        fex1 = make_pwr_expr(fex0, -1.0)
        fex = make_prod(make_const(3.0), fex1)
        print(fex)
        afex = antideriv(fex)
        err = 0.0001
        afexf = tof(afex)
        def gt(x):
            return 3.0*math.log(abs(2.0 + x), math.e)
        for i in range(1, 101):
            assert abs(afexf(i) - gt(i)) <= err
        assert not afex is None
        print(afex)
        fexf = tof(fex)
        assert not fexf is None
        fex2 = deriv(afex)
        assert not fex2 is None
        print(fex2)
        fex2f = tof(fex2)
        assert not fex2f is None
        for i in range(1, 1000):
            assert abs(fexf(i) - fex2f(i)) <= err
        print('Assign 07: Problem 01: Unit Test 11: pass')

    def test_assign_07_prob_01_ut_12(self):
        print('\n***** Assign 07: Problem 01: Unit Test 12 *****')
        fex0 = make_prod(make_const(3.0), make_pwr('x', 1.0))
        fex1 = make_plus(fex0, make_const(2.0))
        fex = make_pwr_expr(fex1, 4.0)
        print(fex)
        afex = antideriv(fex)
        assert not afex is None
        print(afex)
        afexf = tof(afex)
        err = 0.0001
        def gt(x):
            return (1.0/15)*((3*x + 2.0)**5)
        for i in range(1, 10):
            assert abs(afexf(i) - gt(i)) <= err
        fexf = tof(fex)
        assert not fexf is None
        fex2 = deriv(afex)
        assert not fex2 is None
        print(fex2)
        fex2f = tof(fex2)
        assert not fex2f is None
        for i in range(1, 1000):
            assert abs(fexf(i) - fex2f(i)) <= err
        print('Assign 07: Problem 01: Unit Test 12: pass')

    def runTest(self):
        pass


if __name__ == '__main__':
    unittest.main()
