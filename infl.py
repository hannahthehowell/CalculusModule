from const import const
from prod import prod
from pwr import pwr
from deriv import deriv
from tof import tof
from point2d import point2d


def find_infl_pnts(expr):  # currently only works with functions that are third degree polynomials
    firstDrv = deriv(expr)
    secondDrv = deriv(firstDrv)
    tf = tof(expr)

    elt1 = secondDrv.get_elt1()
    elt2 = elt1.get_elt1()
    elt3 = elt2.get_elt1()
    elt4 = elt3.get_mult2()
    elt5 = elt4.get_mult2()
    if isinstance(elt5, pwr):  # There was no original coefficient on x^3 term
        xCoeff = 6
    elif isinstance(elt5, prod):  # There was a coefficient on x^3 originally
        xCoeff = elt3.get_mult1().get_val() * 6

    elt6 = elt2.get_elt2()
    num = elt6.get_mult1().get_val() * 2

    inflX = (0.0 - num) / xCoeff
    inflY = tf(inflX)

    inflPoint = point2d(const(inflX), const(inflY))
    listOfInflPoints = [inflPoint]
    return listOfInflPoints
