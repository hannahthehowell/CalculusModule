from const import const
from tof import tof
from riemann import riemann_approx

 
def midpoint_rule(fexpr, a, b, n):
    assert isinstance(a, const)
    assert isinstance(b, const)
    assert isinstance(n, const)
    approx = riemann_approx(fexpr, a, b, n, pp=0)
    return approx


def trapezoidal_rule(fexpr, a, b, n):
    assert isinstance(a, const)
    assert isinstance(b, const)
    assert isinstance(n, const)
    tf = tof(fexpr)
    partitionSize = (b.get_val() - a.get_val()) / n.get_val()
    total_estimate = tf(a.get_val()) + tf(b.get_val())
    x = a.get_val() + partitionSize
    for i in range(0, n.get_val()-1):
        piece = 2 * tf(x)
        total_estimate = total_estimate + piece
        x = x + partitionSize

    total_estimate = total_estimate * partitionSize/2
    return const(total_estimate)


def simpson_rule(fexpr, a, b, n):
    assert isinstance(a, const)
    assert isinstance(b, const)
    assert isinstance(n, const)
    midApprox = midpoint_rule(fexpr, a, b, n)
    trapApprox = trapezoidal_rule(fexpr, a, b, n)
    simpApprox = (2 * midApprox.get_val() + trapApprox.get_val()) / 3
    return const(simpApprox)

