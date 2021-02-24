from line_eq import line_eq
from maker import make_line_eq
from maker import make_var, make_const, make_prod
from maker import make_pwr, make_plus
from maker import make_point2d
from const import const
from var import var
from prod import prod
from pwr import pwr
from plus import plus
from point2d import point2d
from tof import tof


### sample line equations
lneq1 = make_line_eq(make_var('y'), make_const(2))
lneq2 = make_line_eq(make_var('y'), make_var('x'))
lneq3 = make_line_eq(make_var('y'), make_var('y'))
lneq4 = make_line_eq(make_var('y'), make_prod(make_const(2.0), make_pwr('x', 1.0)))
lneq5 = make_line_eq(make_var('y'), make_prod(make_const(5.0), make_pwr('y', 1.0)))
lneq6 = make_line_eq(make_var('y'), make_plus(make_prod(make_const(5.0), make_pwr('x', 1.0)), make_const(4.0)))
lneq7 = make_line_eq(make_var('y'), make_plus(make_prod(make_const(5.0), make_pwr('y', 1.0)), make_const(4.0)))
lneq8 = make_line_eq(make_var('y'), make_plus(make_prod(make_const(3.0), make_pwr('x', 1.0)), make_const(-4.0)))


def is_const_line(ln):
    if isinstance(ln.get_rhs(), const):
        return True
    else:
        return False


def line_intersection(lneq1, lneq2):
    tf1 = tof(lneq1.get_rhs())
    tf2 = tof(lneq2.get_rhs())

    if lneq1.get_lhs().get_name() == 'x' or lneq2.get_lhs().get_name() == 'x':
        if lneq1.get_lhs().get_name() == 'x' and lneq2.get_lhs().get_name() == 'x':
            return None
        elif lneq1.get_lhs().get_name() == 'x':
            if isinstance(lneq2.get_rhs(), const):
                x = lneq1.get_rhs().get_val()
                y = lneq2.get_rhs().get_val()
                return point2d(x=const(x), y=const(y))
            else:
                y = tf2(lneq1.get_rhs().get_val())
                x = lneq1.get_rhs().get_val()
                return point2d(x=const(x), y=const(y))
        elif lneq2.get_lhs().get_name() == 'x':
            if isinstance(lneq1.get_rhs(), const):
                x = lneq2.get_rhs().get_val()
                y = lneq1.get_rhs().get_val()
                return point2d(x=const(x), y=const(y))
            else:
                y = tf1(lneq2.get_rhs().get_val())
                x = lneq2.get_rhs().get_val()
            return point2d(x=const(x), y=const(y))

    else:
        if is_const_line(lneq1) and is_const_line(lneq2):
            return None
        elif is_const_line(lneq1):
            if isinstance(lneq2.get_rhs(), plus):
                if isinstance(lneq2.get_rhs().get_elt1(), pwr):
                    zero = (0.0 - lneq2.get_rhs().get_elt2().get_val())
                    x = lneq1.get_rhs().get_val() + zero
                    y = tf1(x)
                    return point2d(x=const(x), y=const(y))
                elif isinstance(lneq2.get_rhs().get_elt1(), prod):
                    zero = (0.0 - lneq2.get_rhs().get_elt2().get_val())
                    x = lneq1.get_rhs().get_val() + zero
                    x = x / lneq2.get_rhs().get_elt1().get_mult1().get_val()
                    y = tf1(x)
                    return point2d(x=const(x), y=const(y))
                else:
                    Exception("lI: 2 Error")
            elif isinstance(lneq2.get_rhs(), prod):
                x = lneq1.get_rhs().get_val() / lneq2.get_rhs().get_mult1().get_val()
                y = tf1(x)
                return point2d(x=const(x), y=const(y))
            elif isinstance(lneq2.get_rhs(), pwr):
                x = lneq1.get_rhs().get_val()
                y = lneq1.get_rhs().get_val()
                return point2d(x=const(x), y=const(y))
            else:
                Exception("lI: 1 Error")

        elif is_const_line(lneq2):
            if isinstance(lneq1.get_rhs(), plus):
                if isinstance(lneq1.get_rhs().get_elt1(), pwr):
                    zero = (0.0 - lneq1.get_rhs().get_elt2().get_val())
                    x = lneq2.get_rhs().get_val() + zero
                    y = tf2(x)
                    return point2d(x=const(x), y=const(y))
                elif isinstance(lneq1.get_rhs().get_elt1(), prod):
                    zero = (0.0 - lneq1.get_rhs().get_elt2().get_val())
                    x = lneq2.get_rhs().get_val() + zero
                    x = x / lneq1.get_rhs().get_elt1().get_mult1().get_val()
                    y = tf2(x)
                    return point2d(x=const(x), y=const(y))
                else:
                    Exception("lI: 4 Error")
            elif isinstance(lneq1.get_rhs(), prod):
                x = lneq2.get_rhs().get_val() / lneq1.get_rhs().get_mult1().get_val()
                y = tf2(x)
                return point2d(x=const(x), y=const(y))
            elif isinstance(lneq1.get_rhs(), pwr):
                x = lneq2.get_rhs().get_val()
                y = lneq2.get_rhs().get_val()
                return point2d(x=const(x), y=const(y))
            else:
                Exception("lI: 3 Error")

        else:
            if isinstance(lneq1.get_rhs(), plus):
                a = lneq1.get_rhs().get_elt1().get_mult1().get_val()
                b = lneq1.get_rhs().get_elt2().get_val()
            elif isinstance(lneq1.get_rhs(), prod):
                a = lneq1.get_rhs().get_mult1().get_val()
                b = 0
            elif isinstance(lneq1.get_rhs(), pwr):
                a = 1
                b = 0
            else:
                Exception("lI: 5 Error")

            if isinstance(lneq2.get_rhs(), plus):
                c = lneq2.get_rhs().get_elt1().get_mult1().get_val()
                d = lneq2.get_rhs().get_elt2().get_val()
            elif isinstance(lneq2.get_rhs(), prod):
                c = lneq2.get_rhs().get_mult1().get_val()
                d = 0
            elif isinstance(lneq2.get_rhs(), pwr):
                c = 1
                d = 0
            else:
                Exception("lI: 6 Error")

            if a == c:
                return None

            f = a - c
            g = d - b

            x = g / f
            y = tf1(x)

            return point2d(x=const(x), y=const(y))


### a few tests

def test_01():
    ln1 = make_line_eq(make_var('y'), make_const(1.0))
    ln2 = make_line_eq(make_var('x'), make_const(1.0))
    assert is_const_line(ln1)
    assert is_const_line(ln2)
    print(line_intersection(ln1, ln2))

def test_02():
    ln1 = make_line_eq(make_var('y'), make_const(2.0))
    ln2 = make_line_eq(make_var('y'), make_plus(make_pwr('x', 1.0), make_const(-6.0)))
    print(line_intersection(ln1, ln2))
    print(line_intersection(ln2, ln1))

def test_03():
    ln1 = make_line_eq(make_var('y'), make_const(-2.0))
    ln2 = make_line_eq(make_var('y'), make_plus(make_pwr('x', 1.0), make_const(10.0)))
    print(line_intersection(ln1, ln2))
    print(line_intersection(ln2, ln1))

def test_04():
    ln1 = make_line_eq(make_var('y'), make_const(2.0))
    ln2 = make_line_eq(make_var('y'), make_plus(make_prod(make_const(2.0), make_pwr('x', 1.0)), make_const(-6.0)))
    print(line_intersection(ln1, ln2))
    print(line_intersection(ln2, ln1))

def test_05():
    ln1 = make_line_eq(make_var('y'), make_pwr('x', 1.0))
    ln2 = make_line_eq(make_var('y'), make_prod(make_const(2.0), make_pwr('x', 1.0)))
    ln3 = make_line_eq(make_var('y'), make_plus(make_prod(make_const(3.0), make_pwr('x', 1.0)), make_const(-10.0)))
    print(get_line_coeffs(ln1))
    print(get_line_coeffs(ln2))
    print(get_line_coeffs(ln3))

def test_06():
    ln1 = make_line_eq(make_var('y'), make_pwr('x', 1.0))
    ln2 = make_line_eq(make_var('y'), make_plus(make_prod(make_const(-1.0), make_pwr('x', 1.0)), make_const(6.0)))
    print(line_intersection(ln1, ln2))

def test_07():
    ln1 = make_line_eq(make_var('y'), make_plus(make_prod(make_const(-1.0/5.0), make_pwr('x', 1.0)), make_const(10.0)))
    ln2 = make_line_eq(make_var('y'), make_plus(make_prod(make_const(1.0/5.0), make_pwr('x', 1.0)), make_const(5.0)))
    print(line_intersection(ln1, ln2))

def test_08():
    ln1 = make_line_eq(make_var('y'), make_const(1.0))
    ln2 = make_line_eq(make_var('y'), make_plus(make_prod(make_const(-1.0), make_pwr('x', 1.0)), make_const(6.0)))
    print(line_intersection(ln1, ln2))

def test_09():
    ln1 = make_line_eq(make_var('y'), make_const(5.0))
    ln2 = make_line_eq(make_var('y'), make_plus(make_prod(make_const(-1.0), make_pwr('x', 1.0)), make_const(6.0)))
    print(line_intersection(ln1, ln2))


def maximize_obj_fun(f, corner_points):
    vals = []
    for point in corner_points:
        x = point.get_x().get_val()
        y = point.get_y().get_val()

        val = f(x, y)
        vals.append(val)

    x = vals[0]
    for i in range(0, len(vals)):
        if vals[i] > x:
            x = i
            point = corner_points[i]
    return point


def minimize_obj_fun(f, corner_points):
    vals = []
    for point in corner_points:
        x = point.get_x().get_val()
        y = point.get_y().get_val()

        val = f(x, y)
        vals.append(val)

    x = vals[0]
    for i in range(0, len(vals)):
        if vals[i] < x:
            x = i
            point = corner_points[i]
    return point


### more tests

def test_10():
    f1 = lambda x, y: 2*x + y
    corner_points = [make_point2d(1, 1), make_point2d(1, 5), make_point2d(5, 1)]
    print(maximize_obj_fun(f1, corner_points))
    f2 = lambda x, y: x - 2*y
    print(minimize_obj_fun(f2, corner_points))


def test_11():
    ln1 = make_line_eq(make_var('x'), make_const(1.0))
    ln2 = make_line_eq(make_var('y'), make_prod(make_const(0.5), make_pwr('x', 1.0)))
    print(line_intersection(ln1, ln2))
    ln3 = make_line_eq(make_var('y'), make_plus(make_prod(make_const(-3.0/4), make_pwr('x', 1.0)), make_const(3.0)))
    print(line_intersection(ln1, ln3))
    print(line_intersection(ln2, ln3))


def test_12():
    ln1 = make_line_eq(make_var('x'), make_const(0.0))
    ln2 = make_line_eq(make_var('y'), make_const(0.0))
    ln3 = make_line_eq(make_var('y'), make_plus(make_prod(make_const(-4.0/3), make_pwr('x', 1.0)), make_const(160.0)))
    ln4 = make_line_eq(make_var('y'), make_plus(make_prod(make_const(-0.5), make_pwr('x', 1.0)), make_const(120.0)))
    # print(ln1)
    # print(ln3)
    print(line_intersection(ln1, ln3))
    # print(ln2)
    # print(ln3)
    print(line_intersection(ln2, ln3))
    print(line_intersection(ln3, ln4))


# write your answer to problem 1a as x, y, mv
# (5,1) with value 11
def opt_prob_1a():
    f = lambda x, y: 2*x + y
    ln1 = make_line_eq(make_var('x'), make_const(1.0))
    ln2 = make_line_eq(make_var('y'), make_const(1.0))
    ln3 = make_line_eq(make_var('x'), make_const(5.0))
    ln4 = make_line_eq(make_var('y'), make_const(5.0))
    ln5 = make_line_eq(make_var('y'), plus(prod(const(-1), pwr(var('x'), const(1.0))), const(6.0)))

    cp1 = line_intersection(ln1, ln2)
    cp2 = line_intersection(ln1, ln5)
    cp3 = line_intersection(ln2, ln5)
    corner_points = []
    corner_points.append(cp1)
    corner_points.append(cp2)
    corner_points.append(cp3)

    ans = maximize_obj_fun(f, corner_points)
    return ans


# write your answer to problem 1b as x, y, mv
# (2,2) with value 3
def opt_prob_1b():
    f = lambda x, y: x/2 + y
    ln1 = make_line_eq(make_var('x'), make_const(0.0))
    ln2 = make_line_eq(make_var('y'), make_const(2.0))
    ln3 = make_line_eq(make_var('y'), pwr(var('x'), const(1.0)))
    ln4 = make_line_eq(make_var('y'), plus(prod(const(-1), pwr(var('x'), const(1.0))), const(6.0)))

    cp1 = line_intersection(ln2, ln3)
    cp2 = line_intersection(ln2, ln4)
    cp3 = line_intersection(ln3, ln4)
    corner_points = []
    corner_points.append(cp1)
    corner_points.append(cp2)
    corner_points.append(cp3)

    ans = minimize_obj_fun(f, corner_points)
    return ans


# write your answer to problem 1c as x, y, mv
# (2.5, 2.5) with value 2.5
def opt_prob_1c():
    f = lambda x, y: 3*x - 2*y
    ln1 = make_line_eq(make_var('y'), prod(const(-1.0), pwr(var('x'), const(1.0))))
    ln2 = make_line_eq(make_var('y'), pwr(var('x'), const(1.0)))
    ln3 = make_line_eq(make_var('y'), plus(prod(const(0.5), pwr(var('x'), const(1.0))), const(1.25)))

    cp1 = line_intersection(ln1, ln2)
    cp2 = line_intersection(ln1, ln3)
    cp3 = line_intersection(ln2, ln3)
    corner_points = []
    corner_points.append(cp1)
    corner_points.append(cp2)
    corner_points.append(cp3)

    ans = maximize_obj_fun(f, corner_points)
    return ans






