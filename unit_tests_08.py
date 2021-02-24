import unittest
import math
from maker import make_e_expr, make_prod, make_const
from maker import make_plus, make_pwr, make_ln
from maker import make_pwr_expr, make_quot
from antideriv import antideriv, antiderivdef
from deriv import deriv
from tof import tof
from riemann import riemann_approx_with_gt
from riemann import plot_riemann_error, riemann_approx
from defintegralapprox import midpoint_rule, trapezoidal_rule, simpson_rule


class CS3430S19Assign08UnitTests(unittest.TestCase):

    ### ================= Problem 1 =========================
    
    def test_prob_01_ut_01(self):
        print('\n***** Assign 08: Problem 01: Unit Test 01 *****')
        fex = make_prod(make_const(3.0), make_pwr('x', 2.0))
        fex = make_plus(fex, make_e_expr(make_pwr('x', 1.0)))
        print(fex)
        #afex = antideriv(fex)
        #assert not afex is None
        err_list = riemann_approx_with_gt(fex, make_const(-1.0),
                                           make_const(1.0),
                                           make_const(4.35),
                                           make_const(10),
                                           pp=0)
        for n, err in err_list:
            print(n, err)
        print('Assign 08: Problem 01: Unit Test 01: pass')

    def test_prob_01_ut_02(self):
        print('\n***** Assign 08: Problem 01: Unit Test 02 *****')
        fex = make_prod(make_const(3.0), make_pwr('x', 2.0))
        fex = make_plus(fex, make_e_expr(make_pwr('x', 1.0)))
        print(fex)
        #afex = antideriv(fex)
        #assert not afex is None
        err_list = riemann_approx_with_gt(fex, make_const(-1.0),
                                           make_const(1.0),
                                           make_const(4.35),
                                           make_const(10),
                                           pp=-1)
        for n, err in err_list:
            print(n, err)
        print('Assign 08: Problem 01: Unit Test 02: pass')

    def test_prob_01_ut_03(self):
        print('\n***** Assign 08: Problem 01: Unit Test 03 *****')
        fex = make_prod(make_const(3.0), make_pwr('x', 2.0))
        fex = make_plus(fex, make_e_expr(make_pwr('x', 1.0)))
        print(fex)
        #afex = antideriv(fex)
        #assert not afex is None
        err_list = riemann_approx_with_gt(fex, make_const(-1.0),
                                           make_const(1.0),
                                           make_const(4.35),
                                           make_const(10),
                                           pp=+1)
        for n, err in err_list:
            print(n, err)
        print('Assign 08: Problem 01: Unit Test 03: pass')

    def test_prob_01_ut_04(self):
        print('\n***** Assign 08: Problem 01: Unit Test 04 *****')
        fex = make_const(2.0)
        print(fex)
        #afex = antideriv(fex)
        #assert not afex is None
        err = 0.0001
        approx = riemann_approx(fex, make_const(1.0), make_const(4.0),
                                make_const(10))
        assert abs(approx.get_val() - 6.0) <= err
        print('Assign 08: Problem 01: Unit Test 04: pass')

    def test_prob_01_ut_05(self):
        print('\n***** Assign 08: Problem 01: Unit Test 05 *****')
        fex = make_prod(make_const(-1.0), make_pwr('x', 1.0))
        print(fex)
        err = 0.0001
        approx = riemann_approx(fex, make_const(-2.0), make_const(0.0),
                                make_const(10), pp=0)
        assert abs(approx.get_val() - 2.0) <= err
        print('Assign 08: Problem 01: Unit Test 05: pass')

    def test_prob_01_ut_06(self):
        print('\n***** Assign 08: Problem 01: Unit Test 06 *****')
        fex = make_ln(make_pwr('x', 1.0))
        print(fex)
        err = 0.0001
        approx = riemann_approx(fex, make_const(1.0), make_const(2.0),
                                make_const(100), pp=0)
        assert abs(approx.get_val() - 0.386296444432) <= err
        print('Assign 08: Problem 01: Unit Test 06: pass')

    def test_prob_01_ut_07(self):
        print('\n***** Assign 08: Problem 01: Unit Test 07 *****')
        fex = make_prod(make_const(3.0), make_pwr('x', 2.0))
        fex = make_plus(fex, make_e_expr(make_pwr('x', 1.0)))
        print(fex)
        plot_riemann_error(fex, make_const(-1.0),
                           make_const(1.0),
                           make_const(4.35),
                           make_const(50))
        print('Assign 08: Problem 01: Unit Test 07: pass')

    ### ================= Problem 2 ==========================
       
    def test_prob_02_ut_01(self):
        print('\n***** Assign 08: Problem 02: Unit Test 01 *****')
        fexpr = make_plus(make_pwr('x', 2.0),
                          make_const(5.0))
        a, b, n = make_const(0.0), make_const(4.0), make_const(250)
        approx = midpoint_rule(fexpr, a, b, n)
        print(approx)
        err = 0.0001
        iv = antiderivdef(fexpr, a, b)
        print(iv)
        assert abs(approx.get_val() - iv.get_val()) <= err
        print('Assign 08: Problem 02: Unit Test 01: pass')

    def test_prob_02_ut_02(self):
        print('\n***** Assign 08: Problem 02: Unit Test 02 *****')
        fex = make_plus(make_pwr('x', 2.0), make_const(5.0))
        a, b, n = make_const(0.0), make_const(4.0), make_const(350)
        approx = trapezoidal_rule(fex, a, b, n)
        print(approx)
        err = 0.0001
        iv = antiderivdef(fex, a, b)
        print(iv)
        assert abs(approx.get_val() - iv.get_val()) <= err
        print('Assign 08: Problem 02: Unit Test 02: pass')

    def test_prob_02_ut_03(self):
        print('\n***** Assign 08: Problem 02: Unit Test 03 *****')
        fex = make_plus(make_pwr('x', 2.0), make_const(5.0))
        a, b, n = make_const(0.0), make_const(4.0), make_const(10)
        approx = simpson_rule(fex, a, b, n)
        print(approx)
        err = 0.0001
        iv = antiderivdef(fex, a, b)
        print(iv)
        assert abs(approx.get_val() - iv.get_val()) <= err
        print('Assign 08: Problem 02: Unit Test 03: pass')

    def test_prob_02_ut_04(self):
        print('\n***** Assign 08: Problem 02: Unit Test 04 *****')
        fex = make_pwr('x', -2.0)
        a, b, n = make_const(1.0), make_const(5.0), make_const(50)
        approx = simpson_rule(fex, a, b, n)
        print(approx)
        err = 0.0001
        iv = antiderivdef(fex, a, b)
        print(iv)
        assert abs(approx.get_val() - iv.get_val()) <= err
        print('Assign 08: Problem 02: Unit Test 04: pass')

    def test_prob_02_ut_05(self):
        print('\n***** Assign 08: Problem 02: Unit Test 05 *****')
        fex = make_plus(make_pwr('x', 1.0), make_const(-0.5))
        fex = make_pwr_expr(fex, 2.0)
        a, b, n = make_const(1.0), make_const(5.0), make_const(50)
        approx = simpson_rule(fex, a, b, n)
        print(approx)
        err = 0.0001
        iv = antiderivdef(fex, a, b)
        print(iv)
        assert abs(approx.get_val() - iv.get_val()) <= err
        print('Assign 08: Problem 02: Unit Test 05: pass')

    def test_prob_02_ut_06(self):
        print('\n***** Assign 08: Problem 02: Unit Test 06 *****')
        fex = make_plus(make_prod(make_const(2.0), make_pwr('x', 1.0)),
                        make_const(-3.0))
        fex = make_pwr_expr(fex, 3.0)
        a, b, n = make_const(1.0), make_const(5.0), make_const(50)
        approx = simpson_rule(fex, a, b, n)
        print(approx)
        err = 0.0001
        iv = antiderivdef(fex, a, b)
        print(iv)
        assert abs(approx.get_val() - iv.get_val()) <= err
        print('Assign 08: Problem 02: Unit Test 06: pass')

    def test_prob_02_ut_07(self):
        print('\n***** Assign 08: Problem 02: Unit Test 07 *****')
        fex = make_prod(make_prod(make_const(2.0),
                                  make_pwr('x', 1.0)),
                        make_e_expr(make_pwr('x', 2.0)))
        a, b, n = make_const(0.0), make_const(2.0), make_const(100)
        approx = simpson_rule(fex, a, b, n)
        print(approx)
        err = 0.0001
        assert abs(approx.get_val() - 53.5981514272) <= err
        print('Assign 08: Problem 02: Unit Test 07: pass')

    def test_prob_02_ut_08(self):
        print('\n***** Assign 08: Problem 02: Unit Test 08 *****')
        fex = make_plus(make_const(1.0),
                        make_pwr('x', 3.0))
        fex = make_pwr_expr(fex, 0.5)
        a, b, n = make_const(0.0), make_const(2.0), make_const(100)
        approx = simpson_rule(fex, a, b, n)
        print(approx)
        err = 0.0001
        assert abs(approx.get_val() - 3.24124) <= err
        print('Assign 08: Problem 02: Unit Test 07: pass')



    def runTest(self):
        pass


if __name__ == '__main__':
    unittest.main()
