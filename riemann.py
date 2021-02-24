import numpy as np
from const import const
from tof import tof
import matplotlib.pyplot as plt


def riemann_approx(fexpr, a, b, n, pp=0):
    '''
    pp=0 - approximate with reimann midpoint
    pp=+1 - approximate with reimann right point
    pp=-1 - approximate with reiman left point
    '''
    assert isinstance(a, const)
    assert isinstance(b, const)
    assert isinstance(n, const)
    tf = tof(fexpr)
    partitionSize = (b.get_val() - a.get_val()) / n.get_val()
    if pp == 0:
        startingX = a.get_val() + partitionSize/2
    elif pp == 1:
        startingX = a.get_val() + partitionSize
    elif pp == -1:
        startingX = a.get_val() + 0
    else:
        raise Exception("not correct pp")

    total_estimate = 0
    x = startingX
    for i in range(0, n.get_val()):
        piece = tf(x) * partitionSize
        total_estimate = total_estimate + piece
        x = x + partitionSize

    return const(total_estimate)


def riemann_approx_with_gt(fexpr, a, b, gt, n_upper, pp=0):
    assert isinstance(a, const)
    assert isinstance(b, const)
    assert isinstance(gt, const)
    assert isinstance(n_upper, const)
    approxList = []
    for n in range(1, n_upper.get_val()+1):
        approx = riemann_approx(fexpr, a, b, const(n), pp)
        diff = abs(gt.get_val() - approx.get_val())
        approxList.append((approx, const(diff)))

    return approxList


def plot_riemann_error(fexpr, a, b, gt, n_upper):
    assert isinstance(a, const)
    assert isinstance(b, const)
    assert isinstance(gt, const)
    assert isinstance(n_upper, const)
    m_riemann = riemann_approx_with_gt(fexpr, a, b, gt, n_upper, pp=0)
    l_riemann = riemann_approx_with_gt(fexpr, a, b, gt, n_upper, pp=-1)
    r_riemann = riemann_approx_with_gt(fexpr, a, b, gt, n_upper, pp=1)

    xvals = np.array(range(1, n_upper.get_val() + 1))

    m_list = []
    for i, j in m_riemann:
        m_list.append(j.get_val())

    l_list = []
    for i, j in l_riemann:
        l_list.append(j.get_val())

    r_list = []
    for i, j in r_riemann:
        r_list.append(j.get_val())

    m_yvals = np.array(m_list)
    l_yvals = np.array(l_list)
    r_yvals = np.array(r_list)

    fig1 = plt.figure(1)
    plt.xlabel('n')
    plt.ylabel('err')
    plt.title("Riemann Approximation Error")
    plt.xlim(0, n_upper.get_val())
    plt.grid()
    plt.plot(xvals, m_yvals, 'r')
    plt.plot(xvals, l_yvals, 'g')
    plt.plot(xvals, r_yvals, 'b')
    plt.legend(('mid', 'left', 'right'), loc='best')
    plt.show()

