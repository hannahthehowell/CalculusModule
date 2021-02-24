from const import const
from pwr import pwr
from var import var
from plus import plus
from prod import prod
from quot import quot
from deriv import deriv
from ln import ln
from absv import absv
from tof import tof
import math


def antideriv(i):
    if isinstance(i, const):
        return plus(elt1=prod(mult1=i, mult2=pwr(base=var('x'), deg=const(1.0))), elt2=const(0.0))
    elif isinstance(i, pwr):
        b = i.get_base()
        d = i.get_deg()
        if isinstance(b, var) and isinstance(d, const):
            if d.get_val() == -1:
                return plus(elt1=ln(expr=absv(expr=pwr(base=var('x'), deg=const(1.0)))), elt2=const(0.0))
            else:
                return plus(elt1=prod(mult1=const(1/(d.get_val()+1)), mult2=pwr(base=b, deg=const(d.get_val() + 1))), elt2=const(0.0))
        elif is_e_const(b):
            return plus(elt1=prod(mult1=quot(num=const(1.0), denom=deriv(d)), mult2=i), elt2=const(0.0))
        elif isinstance(b, plus):
            if d.get_val() == -1:
                return plus(elt1=ln(expr=absv(expr=b)), elt2=const(0.0))
            else:
                return plus(elt1=prod(mult1=quot(num=const(1.0), denom=deriv(b)), mult2=prod(mult1=const(1/(d.get_val()+1)), mult2=pwr(base=b, deg=const(d.get_val() + 1)))), elt2=const(0.0))
        else:
            raise Exception('antideriv: unknown case')
    elif isinstance(i, plus):
        return plus(elt1=antideriv(i.get_elt1()), elt2=antideriv(i.get_elt2()))
    elif isinstance(i, prod):
        assert isinstance(i.get_mult1(), const)
        return prod(mult1=i.get_mult1(), mult2=antideriv(i.get_mult2()))
    else:
        raise Exception('antideriv: unknown case')


def is_e_const(b):
    if isinstance(b, const):
        if b.get_val() == math.e:
            return True
    else:
        return False


def antiderivdef(expr, a, b):
    assert isinstance(a, const)
    assert isinstance(b, const)
    aexpr = antideriv(expr)
    tf = tof(aexpr)
    aval = tf(a.get_val())
    bval = tf(b.get_val())
    diff = bval - aval

    return const(diff)
