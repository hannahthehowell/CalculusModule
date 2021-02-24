from prod import prod
from const import const
from pwr import pwr
from plus import plus
import math


def find_poly_1_zeros(expr):
    elt1 = expr.get_elt1()
    elt2 = expr.get_elt2()
    if isinstance(elt1, prod):  # If normal expression
        if isinstance(elt2, const):
            coeff = elt1.get_mult1()
            zero = (0.0 - elt2.get_val()) / (coeff.get_val())
            return const(zero)
    elif isinstance(elt1, plus):  # If deriv expression
        piece1 = elt1.get_elt1()
        piece2 = elt1.get_elt2()
        if isinstance(piece1, prod):
            if isinstance(piece2, prod):
                xCoeff = piece1.get_mult1()
                num = piece2.get_mult1()
                zero = (0.0 - num.get_val()) / (xCoeff.get_val() * 2)
                return const(zero)
        else:
            raise Exception('find_poly_1-zeros: case 2: ' + str(expr))
    else:
        raise Exception('find_poly_1-zeros: case 1: ' + str(expr))


def find_poly_2_zeros(expr):
    plus1 = expr.get_elt1()
    plus2 = plus1.get_elt1()

    if isinstance(plus2, pwr):  # If normal expression
        powersOfx = expr.get_elt1()
        elt1 = powersOfx.get_elt1()

        if isinstance(elt1, prod):
            a = elt1.get_mult1().get_val()
        elif isinstance(elt1, pwr):
            a = 1.0

        elt2 = powersOfx.get_elt2()

        if isinstance(elt2, prod):
            b = elt2.get_mult1().get_val()
        elif isinstance(elt2, pwr):
            b = 1.0

        c = expr.get_elt2().get_val()
        zero1 = (0 - b - math.sqrt((b * b) - (4 * a * c))) / (2 * a)
        zero2 = (0 - b + math.sqrt((b * b) - (4 * a * c))) / (2 * a)
        return const(zero1), const(zero2)

    # tests 4, 8 depend on this
    if isinstance(plus2, prod):  # If normal expression
        a = plus2.get_mult1().get_val()

        piece2 = plus1.get_elt2()
        if isinstance(piece2, pwr):
            b = 1.0
        elif isinstance(piece2, prod):
            b = piece2.get_mult1().get_val()

        c = expr.get_elt2().get_val()

        zero1 = (0 - b - math.sqrt((b * b) - (4 * a * c))) / (2 * a)
        zero2 = (0 - b + math.sqrt((b * b) - (4 * a * c))) / (2 * a)
        return const(zero1), const(zero2)

    elif isinstance(plus2, plus):  # If deriv expression
        plus3 = plus2.get_elt1()
        prod1 = plus3.get_mult2()

        if isinstance(prod1, pwr):
            a = 3.0
        elif isinstance(prod1, prod):
            a = plus3.get_mult1().get_val() * 3.0

        prod2 = plus2.get_elt2()
        prod3 = prod2.get_mult2()

        if isinstance(prod3, pwr):
            b = 2.0
        elif isinstance(prod3, prod):
            b = prod2.get_mult1().get_val() * 2.0

        prod4 = plus1.get_elt2()
        prod5 = prod4.get_mult2()

        if isinstance(prod5, pwr):
            c = 1.0
        elif isinstance(prod5, prod):
            c = prod4.get_mult1().get_val()

        zero1 = (0 - b - math.sqrt((b * b) - (4 * a * c))) / (2 * a)
        zero2 = (0 - b + math.sqrt((b * b) - (4 * a * c))) / (2 * a)
        return const(zero1), const(zero2)
    else:
        raise Exception('find_poly_2_zeros: case 1: ' + str(expr))
