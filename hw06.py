import math
import numpy as np
import matplotlib.pyplot as plt

from const import const
from prod import prod
from pwr import pwr
from var import var
from plus import plus
from quot import quot
from maker import make_prod, make_const, make_pwr, make_e_expr, make_plus, make_quot
from tof import tof
from deriv import deriv


# ************* Problem 1 ******************

def percent_retention_model(lmbda, a):
    assert isinstance(lmbda, const)
    assert isinstance(a, const)
    return plus(elt1=prod(mult1=const(100 - a.get_val()), mult2=pwr(base=const(math.e), deg=prod(mult1=prod(mult1=const(-1.0), mult2=lmbda), mult2=pwr(base=var('t'), deg=const(1.0))))), elt2=a)


def plot_retention(lmbda, a, t0, t1):
    assert isinstance(lmbda, const)
    assert isinstance(a, const)
    assert isinstance(t0, const)
    assert isinstance(t1, const)
    fun = percent_retention_model(lmbda, a)
    graph(fun, t0, t1, 'Ebbinghaus Model of Forgetting', 't', 'prf and dprf', 'prf', 'dprf')


# ************* Problem 2 ******************

def spread_of_disease_model(p, t0, p0, t1, p1):
    assert isinstance(p, const)
    assert isinstance(t0, const) and isinstance(p0, const)
    assert isinstance(t1, const) and isinstance(p1, const)
    b = const(p.get_val() / p0.get_val() - 1)
    c = const((-1 * math.log((p.get_val()/p1.get_val() - 1) / b.get_val())) / (t1.get_val()))
    return quot(num=p, denom=plus(elt1=const(1.0), elt2=prod(mult1=b, mult2=pwr(base=const(math.e), deg=prod(mult1=const(-1.0), mult2=prod(mult1=c, mult2=pwr(base=var('t'), deg=const(1.0))))))))


def plot_spread_of_disease(p, t0, p0, t1, p1, tl, tu):
    assert isinstance(p, const) and isinstance(t0, const)
    assert isinstance(p0, const) and isinstance(t1, const)
    fun = spread_of_disease_model(p, t0, p0, t1, p1)
    graph(fun, tl, tu, 'Spread of Disease', 't', 'sdf and dsdf', 'sdf', 'dsdf')


# ************* Problem 3 ******************

def plant_growth_model(m, t1, x1, t2, x2):
    assert isinstance(m, const)
    assert isinstance(t1, const) and isinstance(x1, const)
    assert isinstance(t2, const) and isinstance(x2, const)
    k = const((-1 * math.log((m.get_val()/x2.get_val() - 1) / (m.get_val()/x1.get_val() - 1)) / (m.get_val() * (t2.get_val() - t1.get_val()))))
    b = const((m.get_val() / x1.get_val() - 1) / (math.e ** (-1 * m.get_val() * k.get_val() * t1.get_val())))
    return quot(num=m, denom=plus(elt1=const(1.0), elt2=prod(mult1=b, mult2=pwr(base=const(math.e), deg=prod(mult1=const(-1.0), mult2=prod(mult1=m, mult2=prod(mult1=k, mult2=pwr(base=var('t'), deg=const(1.0)))))))))


def plot_plant_growth(m, t1, x1, t2, x2, tl, tu):
    assert isinstance(m, const)
    assert isinstance(t1, const) and isinstance(x1, const)
    assert isinstance(t2, const) and isinstance(x2, const)
    assert isinstance(tl, const) and isinstance(tu, const)
    fun = plant_growth_model(m, t1, x1, t2, x2)
    # offset
    graph(fun, tl, tu, 'Plant Growth', 't', 'pgf and dpgf', 'pgf', 'dpgf')


# ************* Problem 4 ******************

def spread_of_news_model(p, k):
    assert isinstance(p, const) and isinstance(k, const)
    return prod(mult1=p, mult2=plus(elt1=const(1.0), elt2=pwr(base=const(-1 * math.e), deg=prod(mult1=const(-1 * k.get_val()), mult2=pwr(base=var('t'), deg=const(1.0))))))


def plot_spread_of_news(p, k, tl, tu):
    assert isinstance(p, const) and isinstance(k, const)
    assert isinstance(tl, const) and isinstance(tu, const)
    fun = spread_of_news_model(p, k)
    graph(fun, tl, tu, 'Spread of News', 't', 'snf and dsnf', 'snf', 'dsnf')


def graph(fun, tl, tu, title, xlabel, ylabel, legend1, legend2):
    drv = deriv(fun)
    tf = tof(fun)
    dtf = tof(drv)

    xvals1 = np.linspace(tl.get_val(), tu.get_val(), 10000)
    yvals0 = np.array([tf(x) for x in xvals1])
    yvals1 = np.array([dtf(x) for x in xvals1])

    fig1 = plt.figure(1)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xlim(tl.get_val(), tu.get_val())
    plt.grid()
    plt.plot(xvals1, yvals0, 'r')
    plt.plot(xvals1, yvals1, 'b')
    plt.legend((legend1, legend2), loc='best')
    plt.show()


