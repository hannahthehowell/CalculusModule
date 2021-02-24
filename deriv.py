from var import var
from const import const
from pwr import pwr
from prod import prod
from plus import plus
from quot import quot
from ln import ln
from absv import absv
import math


def deriv(expr):
    if isinstance(expr, const):
        return const_deriv(expr)
    elif isinstance(expr, pwr):
        return pwr_deriv(expr)
    elif isinstance(expr, prod):
        return prod_deriv(expr)
    elif isinstance(expr, plus):
        return plus_deriv(expr)
    elif isinstance(expr, quot):
        return quot_deriv(expr)
    elif isinstance(expr, ln):
        return ln_deriv(expr)
    elif isinstance(expr, absv):
        return absv_deriv(expr)
    else:
        raise Exception('deriv:' + repr(expr))


def const_deriv(c):
    assert isinstance(c, const)
    return const(val=0.0)


def plus_deriv(s):
    assert isinstance(s, plus)
    return plus(elt1=deriv(s.get_elt1()), elt2=deriv(s.get_elt2()))


def ln_deriv(l):
    assert isinstance(l, ln)
    return prod(mult1=quot(num=const(1.0), denom=l.get_expr()), mult2=deriv(l.get_expr()))


def absv_deriv(a):
    assert isinstance(a, absv)
    return deriv(a.get_expr())


def pwr_deriv(p):
    assert isinstance(p, pwr)
    b = p.get_base()
    d = p.get_deg()
    minus1 = const(val=-1.0)
    if isinstance(b, var):
        if isinstance(d, const):
            if d.get_val() == 0.0:
                return const(val=0.0)
            else:
                return prod(mult1=d, mult2=pwr(b, const.add(d, minus1)))
        else:
            raise Exception('pwr_deriv: case 1: ' + str(p))
    elif isinstance(b, pwr): 
        if isinstance(d, const):
            innerBase = b.get_base()
            innerDegree = b.get_deg()
            return prod(mult1=prod(mult1=d, mult2=pwr(b, const.add(d, minus1))),
                        mult2=prod(mult1=innerDegree, mult2=pwr(innerBase, const.add(innerDegree, minus1))))
        else:
            raise Exception('pwr_deriv: case 2: ' + str(p))
    elif isinstance(b, plus):
        if isinstance(d, const):
            return prod(mult1=prod(mult1=d, mult2=pwr(b, const.add(d, minus1))),
                        mult2=plus_deriv(b))
        else:
            raise Exception('pwr_deriv: case 3: ' + str(p))
    elif isinstance(b, prod):
        if isinstance(d, const):
            return prod(mult1=prod(mult1=d, mult2=pwr(b, const.add(d, minus1))),
                        mult2=prod_deriv(b))
        else:
            raise Exception('pwr_deriv: case 4: ' + str(p))
    elif isinstance(b, quot):
        if isinstance(d, const):
            return prod(mult1=prod(mult1=d, mult2=pwr(b, const.add(d, minus1))),
                        mult2=quot_deriv(b))
        else:
            raise Exception('pwr_deriv: case 5: ' + str(p))
    elif isinstance(b, const):
        if b.get_val() == math.e:
            return prod(mult1=p, mult2=deriv(d))
        elif b.get_val() == (-1 * math.e):
            return prod(mult1=p, mult2=deriv(d))
        else:
            raise Exception('power_deriv: case 6: ' + str(p))
    elif isinstance(b, ln):
        if isinstance(d, const):
            return prod(mult1=prod(mult1=d, mult2=pwr(b, const.add(d, minus1))),
                        mult2=ln_deriv(b))
        else:
            raise Exception('pwr_deriv: case 7: ' + str(p))
    else:
        raise Exception('power_deriv: case 8: ' + str(p))


def prod_deriv(p):
    assert isinstance(p, prod)
    m1 = p.get_mult1()
    m2 = p.get_mult2()
    if isinstance(m1, const):
        if isinstance(m2, const):
            return const_deriv(m1)
        else:
            return prod(mult1=m1, mult2=deriv(m2))
    elif isinstance(m1, plus):
        if isinstance(m2, const):
            return prod(mult1=m2, mult2=plus_deriv(m1))
        else:
            return plus(elt1=prod(mult1=m1, mult2=deriv(m2)), elt2=prod(mult1=m2, mult2=plus_deriv(m1)))
    elif isinstance(m1, pwr):
        if isinstance(m2, const):
            return prod(mult1=m2, mult2=pwr_deriv(m1))
        else:
            return plus(elt1=prod(mult1=m1, mult2=deriv(m2)), elt2=prod(mult1=m2, mult2=pwr_deriv(m1)))
    elif isinstance(m1, prod):
        if isinstance(m2, const):
            return prod(mult1=m2, mult2=prod_deriv(m1))
        else:
            return plus(elt1=prod(mult1=m1, mult2=deriv(m2)), elt2=prod(mult1=m2, mult2=prod_deriv(m1)))
    elif isinstance(m1, quot):
        if isinstance(m2, const):
            return prod(mult1=m2, mult2=quot_deriv(m1))
        else:
            return plus(elt1=prod(mult1=m1, mult2=deriv(m2)), elt2=prod(mult1=m2, mult2=quot_deriv(m1)))
    elif isinstance(m1, ln):
        if isinstance(m2, const):
            return prod(mult1=m2, mult2=ln_deriv(m1))
        else:
            return plus(elt1=prod(mult1=m1, mult2=deriv(m2)), elt2=prod(mult1=m2, mult2=ln_deriv(m1)))

    else:
        raise Exception('prod_deriv: case 4:' + str(p))


def quot_deriv(p):
    assert isinstance(p, quot)
    m1 = p.get_num()
    m2 = p.get_denom()
    squared = const(val=2.0)
    if isinstance(m1, const):
        if isinstance(m2, const):
            return const_deriv(m1)
        else:
            return quot(num=prod(mult1=prod(const(-1.0), m1), mult2=deriv(m2)), denom=pwr(m2, squared))
    elif isinstance(m1, plus):
        if isinstance(m2, const):
            return quot(num=plus_deriv(m1), denom=m2)
        else:
            return quot(num=plus(elt1=prod(mult1=m2, mult2=plus_deriv(m1)),
                                 elt2=prod(mult1=const(-1.0), mult2=prod(mult1=m1, mult2=deriv(m2)))),
                        denom=pwr(m2, squared))
    elif isinstance(m1, pwr):
        if isinstance(m2, const):
            return quot(num=pwr_deriv(m1), denom=m2)
        elif isinstance(m2, plus):
            return quot(num=plus(elt1=prod(mult1=m2, mult2=pwr_deriv(m1)),
                                 elt2=prod(mult1=const(-1.0), mult2=prod(mult1=m1, mult2=deriv(m2)))),
                        denom=pwr(m2, squared))
    elif isinstance(m1, prod):
        if isinstance(m2, const):
            return quot(num=prod_deriv(m1), denom=m2)
        elif isinstance(m2, plus):
            return quot(num=plus(elt1=prod(mult1=m2, mult2=prod_deriv(m1)),
                                 elt2=prod(mult1=const(-1.0), mult2=prod(mult1=m1, mult2=deriv(m2)))),
                        denom=pwr(m2, squared))
    elif isinstance(m1, ln):
        if isinstance(m2, const):
            return quot(num=ln_deriv(m1), denom=m2)
        else:
            return quot(num=plus(elt1=prod(mult1=m2, mult2=ln_deriv(m1)),
                                 elt2=prod(mult1=const(-1.0), mult2=prod(mult1=m1, mult2=deriv(m2)))),
                        denom=pwr(m2, squared))
    else:
        raise Exception('quot_deriv: case 4:' + str(p))


def logdiff(expr):
    assert isinstance(expr, prod)
    addendsList1 = list()
    addendsList2 = list()

    def recurse(exp):
        assert isinstance(exp, prod)
        m1 = exp.get_mult1()
        assert not isinstance(m1, prod)
        addendsList1.append(m1)

        m2 = exp.get_mult2()
        if isinstance(m2, prod):
            recurse(m2)
        else:
            addendsList1.append(m2)
            return
        return

    recurse(expr)

    numAddends = len(addendsList1)
    if numAddends == 0:
        raise Exception('logdiff: case 1:' + str(expr))
    elif numAddends == 1:
        raise Exception('logdiff: case 2:' + str(expr))
    else:
        for a in addendsList1:
            addendsList2.append(ln_deriv(ln(a)))

    backIndex = numAddends - 1
    addends = plus(elt1=addendsList2[backIndex - 1], elt2=addendsList2[backIndex])
    backIndex = backIndex - 2
    while backIndex >= 0:
        addends = plus(elt1=addends, elt2=addendsList2[backIndex])
        backIndex = backIndex - 1

    return prod(mult1=expr, mult2=addends)

