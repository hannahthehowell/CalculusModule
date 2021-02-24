from const import const
from pwr import pwr
from prod import prod
from plus import plus
from deriv import deriv
from poly12 import find_poly_1_zeros
from poly12 import find_poly_2_zeros
from tof import tof
from point2d import point2d


def loc_xtrm_1st_drv_test(expr):
    tf = tof(expr)
    drv = deriv(expr)
    plus1 = expr.get_elt1()
    plus2 = plus1.get_elt1()

    if isinstance(plus2, prod):  # second degree poly - first degree deriv
        zeroX1 = find_poly_1_zeros(drv).get_val()
        zeroY1 = tf(zeroX1)
        xtrmCoord = point2d(x=const(zeroX1), y=const(zeroY1))
        leftX = zeroX1 - 0.01
        leftY = tf(leftX)
        rightX = zeroX1 + 0.01
        rightY = tf(rightX)
        if(leftY > zeroY1) and (rightY > zeroY1):
            return [tuple(['min', xtrmCoord])]
        elif(leftY < zeroY1) and (rightY < zeroY1):
            return [tuple(['max', xtrmCoord])]
        else:
            return None

    elif isinstance(plus2, plus):  # third degree poly - second degree deriv
        zeroX2 = find_poly_2_zeros(drv)
        firstX = zeroX2[0].get_val()
        firstY = tf(firstX)
        secondX = zeroX2[1].get_val()
        secondY = tf(secondX)

        xtrmCoord1 = point2d(x=const(firstX), y=const(firstY))
        xtrmCoord2 = point2d(x=const(secondX), y=const(secondY))

        leftFirstX = firstX - 0.01
        leftFirstY = tf(leftFirstX)
        rightFirstX = firstX + 0.01
        rightFirstY = tf(rightFirstX)

        leftSecondX = secondX - 0.01
        leftSecondY = tf(leftSecondX)
        rightSecondX = secondX + 0.01
        rightSecondY = tf(rightSecondX)

        if (leftFirstY > firstY) and (rightFirstY > firstY):
            elt1 = ('min', xtrmCoord1)
        elif (leftFirstY < firstY) and (rightFirstY < firstY):
            elt1 = ('max', xtrmCoord1)
        else:
            elt1 = None

        if (leftSecondY > secondY) and (rightSecondY > secondY):
            elt2 = ('min', xtrmCoord2)
        elif (leftSecondY < secondY) and (rightSecondY < secondY):
            elt2 = ('max', xtrmCoord2)
        else:
            elt2 = None

        if (elt1 is None) and (elt2 is None):
            return None
        elif elt1 is None:
            return list(elt2)
        elif elt2 is None:
            return list(elt1)
        else:
            return list((elt1, elt2))

    else:
        raise Exception('loc_xtrm_1st_drv_test: case 1: ' + str(expr))


def loc_xtrm_2nd_drv_test(expr):
    tf = tof(expr)
    firstDrv = deriv(expr)
    secondDrv = deriv(firstDrv)
    plus1 = expr.get_elt1()
    plus2 = plus1.get_elt1()

    if isinstance(plus2, prod):  # second degree poly - 0 degree 2nd deriv
        zeroX1 = find_poly_1_zeros(firstDrv).get_val()
        zeroY1 = tf(zeroX1)
        xtrmCoord = point2d(x=const(zeroX1), y=const(zeroY1))
        drvTestNum = plus2.get_mult1().get_val() * 2
        if drvTestNum > 0:
            return [tuple(['min', xtrmCoord])]
        elif drvTestNum < 0:
            return [tuple(['max', xtrmCoord])]
        else:
            return None

    elif isinstance(plus2, plus) or isinstance(plus2, pwr):  # third degree poly - first degree 2nd deriv
        zeroX2 = find_poly_2_zeros(firstDrv)
        firstX = zeroX2[0].get_val()
        firstY = tf(firstX)
        secondX = zeroX2[1].get_val()
        secondY = tf(secondX)

        xtrmCoord1 = point2d(x=const(firstX), y=const(firstY))
        xtrmCoord2 = point2d(x=const(secondX), y=const(secondY))

        tf2Drv = tof(secondDrv)

        drvTestNum1 = tf2Drv(firstX)
        drvTestNum2 = tf2Drv(secondX)

        if drvTestNum1 > 0:
            elt1 = 'min', xtrmCoord1
        elif drvTestNum1 < 0:
            elt1 = 'max', xtrmCoord1
        else:
            elt1 = None, None

        if drvTestNum2 > 0:
            elt2 = 'min', xtrmCoord2
        elif drvTestNum2 < 0:
            elt2 = 'max', xtrmCoord2
        else:
            elt2 = None, None

        return list((elt1, elt2))
