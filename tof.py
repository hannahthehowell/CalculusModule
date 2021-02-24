from var import var
from const import const
from pwr import pwr
from prod import prod
from plus import plus
from quot import quot
from ln import ln
from absv import absv
import math


def tof(expr):
    if isinstance(expr, const):
        return const_tof(expr)
    elif isinstance(expr, pwr):
        return pwr_tof(expr)
    elif isinstance(expr, prod):
        return prod_tof(expr)
    elif isinstance(expr, plus):
        return plus_tof(expr)
    elif isinstance(expr, quot):
        return quot_tof(expr)
    elif isinstance(expr, ln):
        return ln_tof(expr)
    elif isinstance(expr, absv):
        return absv_tof(expr)
    else:
        raise Exception('tof: ' + str(expr))


# here is how you can implement converting
# a constant to a function.
def const_tof(c):
    assert isinstance(c, const)

    def f(x):
        return c.get_val()
    return f


def pwr_tof(expr):
    assert isinstance(expr, pwr)
    expb = expr.get_base()
    d = expr.get_deg()
    if isinstance(expb, const):
        if expb.get_val() == math.e:
            tf = tof(d)
            return lambda x: math.e ** tf(x)
        if expb.get_val() == (-1 * math.e):
            tf = tof(d)
            return lambda x: -1 * math.e ** tf(x)
        else:
            return const_tof(expb)
    elif isinstance(expb, var):
        if isinstance(d, const):
            degree = d.get_val()
            return lambda x: x ** degree
        else:
            raise Exception('pw_tof: case 1:' + str(expr))
    elif isinstance(expb, plus):
        if isinstance(d, const):
            degree = d.get_val()
            tf = plus_tof(expb)
            return lambda x: tf(x) ** degree
        else:
            raise Exception('pw_tof: case 2:' + str(expr))
    elif isinstance(expb, pwr):
        if isinstance(d, const):
            degree = d.get_val()
            tf = pwr_tof(expb)
            return lambda x: tf(x) ** degree
        else:
            raise Exception('pw_tof: case 3:' + str(expr))
    elif isinstance(expb, prod):
        if isinstance(d, const):
            degree = d.get_val()
            tf = prod_tof(expb)
            return lambda x: tf(x) ** degree
        else:
            raise Exception('pw_tof: case 4:' + str(expr))
    elif isinstance(expb, quot):
        if isinstance(d, const):
            degree = d.get_val()
            tf = quot_tof(expb)
            return lambda x: tf(x) ** degree
        else:
            raise Exception('pw_tof: case 5:' + str(expr))
    elif isinstance(expb, ln):
        if isinstance(d, const):
            degree = d.get_val()
            tf = ln_tof(expb)
            return lambda x: tf(x) ** degree
        else:
            raise Exception('pw_tof: case 6:' + str(expr))
    else:
        raise Exception('pw_tof: case 7:' + str(expr))


def prod_tof(expr):
    mult1 = tof(expr.get_mult1())
    mult2 = tof(expr.get_mult2())
    return lambda x: mult1(x) * mult2(x)


def plus_tof(expr):
    elt1 = tof(expr.get_elt1())
    elt2 = tof(expr.get_elt2())
    return lambda x: elt1(x) + elt2(x)


def quot_tof(expr):
    num = tof(expr.get_num())
    denom = tof(expr.get_denom())
    return lambda x: (num(x)) / (denom(x))


def ln_tof(expr):
    ln = tof(expr.get_expr())
    return lambda x: math.log(ln(x))


def absv_tof(expr):
    fun = tof(expr.get_expr())
    return lambda x: abs(fun(x))
