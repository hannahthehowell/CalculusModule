from maker import make_prod, make_const, make_pwr, make_var, make_plus
from const import const
from deriv import deriv
from poly12 import find_poly_1_zeros, find_poly_2_zeros
from tof import tof
from pwr import pwr
from prod import prod
from plus import plus
import math


def maximize_revenue(dmnd_eq, constraint=lambda x: x >= 0):
    elt1 = dmnd_eq.get_elt1()

    if isinstance(elt1, prod):  # if dmnd_eq is 1st degree poly
        elt2 = dmnd_eq.get_elt2()
        assert isinstance(elt2, const)
        f1 = make_prod(elt1.get_mult1(), make_pwr('x', 2.0))
        f2 = make_prod(elt2, make_pwr('x', 1.0))
        f3 = make_plus(f1, f2)
        f4 = make_const(0.0)
        revEqn = make_plus(f3, f4)
        margRev = deriv(revEqn)

        zeroX = find_poly_1_zeros(margRev).get_val()

    elif isinstance(elt1, pwr):
        elt2 = dmnd_eq.get_elt2()
        assert isinstance(elt2, const)
        f1 = make_pwr('x', 2.0)
        f2 = make_prod(elt2, make_pwr('x', 1.0))
        f3 = make_plus(f1, f2)
        f4 = make_const(0.0)
        revEqn = make_plus(f3, f4)
        margRev = deriv(revEqn)

        zeroX = find_poly_1_zeros(margRev).get_val()

    elif isinstance(elt1, plus):  # elif dmnd_eq is 2nd degree poly:
        elt2 = elt1.get_elt1()
        elt3 = elt1.get_elt2()

        if isinstance(elt2, prod) and isinstance(elt3, prod):
            f1 = make_prod(elt2.get_mult1(), make_pwr('x', 3.0))
            f2 = make_prod(elt3.get_mult1(), make_pwr('x', 2.0))
        elif isinstance(elt2, pwr) and isinstance(elt3, prod):
            f1 = make_pwr('x', 3.0)
            f2 = make_prod(elt3.get_mult1(), make_pwr('x', 2.0))
        elif isinstance(elt2, prod) and isinstance(elt3, pwr):
            f1 = make_prod(elt2.get_mult1(), make_pwr('x', 3.0))
            f2 = make_pwr('x', 2.0)
        elif isinstance(elt2, pwr) and isinstance(elt3, pwr):
            f1 = make_pwr('x', 3.0)
            f2 = make_pwr('x', 2.0)

        elt4 = dmnd_eq.get_elt2()
        f3 = make_plus(f1, f2)
        f4 = make_prod(elt4, make_pwr('x', 1.0))
        f5 = make_const(0.0)
        f6 = make_plus(f3, f4)
        revEqn = make_plus(f6, f5)
        margRev = deriv(revEqn)

        tfRev = tof(revEqn)
        zeros = find_poly_2_zeros(margRev)
        firstX = zeros[0].get_val()
        firstY = tfRev(firstX)
        secondX = zeros[1].get_val()
        secondY = tfRev(secondX)

        if firstY > secondY:
            zeroX = firstX
        elif firstY < secondY:
            zeroX = secondX
        else:
            zeroX = firstX


    if constraint(zeroX) is False:
        return const(0.0), const(0.0), const(0.0)

    tfDmnd = tof(dmnd_eq)
    price = tfDmnd(zeroX)
    num_units = zeroX
    rev = num_units * price

    return const(num_units), const(rev), const(price)


def dydt_given_x_dxdt(yt, x, dxdt):
    drv = deriv(yt)
    f1 = prod(mult1=drv, mult2=dxdt)
    tf = tof(f1)
    dydt = tf(x.get_val())

    return const(dydt)


def oil_disk_test():
    yt = make_prod(make_const(0.02 * math.pi), make_pwr('r', 2.0))
    print(yt)
    dydt = dydt_given_x_dxdt(yt, make_const(150.0), make_const(20.0))
    assert not dydt is None
    assert isinstance(dydt, const)
    print(dydt)


def arm_tumor_test():
    yt = make_prod(make_const(0.003 * math.pi), make_pwr('r', 3.0))
    print(yt)
    dydt = dydt_given_x_dxdt(yt, make_const(10.3), make_const(-1.75))
    assert not dydt is None
    assert isinstance(dydt, const)
    print(dydt)

