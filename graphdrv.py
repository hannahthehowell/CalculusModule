from deriv import deriv
from tof import tof
import numpy as np
import matplotlib.pyplot as plt


def graph_drv(fexpr, xlim, ylim):
    function0 = tof(fexpr)
    drv = deriv(fexpr)
    function1 = tof(drv)

    xvals1 = np.linspace(xlim[0], xlim[1], 10000)
    yvals0 = np.array([function0(x) for x in xvals1])
    yvals1 = np.array([function1(x) for x in xvals1])

    fig1 = plt.figure(1)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.ylim(ylim)
    plt.xlim(xlim)
    plt.grid()
    plt.plot(xvals1, yvals0)
    plt.plot(xvals1, yvals1)
    plt.legend(loc='best')
    plt.show()


def graph1(fexpr, xlim, ylim, xLabel, yLabel):
    # function0 = tof(fexpr)
    xvals1 = np.linspace(xlim[0], xlim[1], 10000)
    yvals0 = np.array([fexpr(x) for x in xvals1])

    fig1 = plt.figure(1)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.ylim(ylim)
    plt.xlim(xlim)
    plt.grid()
    plt.plot(xvals1, yvals0)
    plt.legend(loc='best')
    plt.show()


def graph3(fexpr1, fexpr2, fexpr3, xlim, ylim):
    function1 = tof(fexpr1)
    function2 = tof(fexpr2)
    function3 = tof(fexpr3)
    xvals1 = np.linspace(xlim[0], xlim[1], 10000)
    yvals1 = np.array([function1(x) for x in xvals1])
    yvals2 = np.array([function2(x) for x in xvals1])
    yvals3 = np.array([function3(x) for x in xvals1])

    fig1 = plt.figure(1)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.ylim(ylim)
    plt.xlim(xlim)
    plt.grid()
    plt.plot(xvals1, yvals1)
    plt.plot(xvals1, yvals2)
    plt.plot(xvals1, yvals3)
    plt.legend(loc='best')
    plt.show()
