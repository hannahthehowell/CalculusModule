#!/usr/bin/python

###########################################
# module: hw05.py
# Hannah Galli
# A02080896
###########################################

from var import var
from const import const
from pwr import pwr
from prod import prod
from quot import quot
from tof import tof
from deriv import deriv
import math


###################### Problem 1 ########################

def solve_pdeq(k1, k2):
    assert isinstance(k1, const)
    assert isinstance(k2, const)
    val = k2.get_val() / k1.get_val()
    return pwr(base=const(math.e), deg=prod(mult1=const(val), mult2=pwr(base=var('x'), deg=const(1.0))))


def solve_pdeq_with_init_cond(y0, k):
    assert isinstance(y0, const)
    assert isinstance(k, const)
    return prod(mult1=y0, mult2=pwr(base=const(math.e), deg=prod(mult1=k, mult2=pwr(base=var('x'), deg=const(1.0)))))


############################ Problem 2 ########################

def find_growth_model(p0, t, n):
    assert isinstance(p0, const)
    assert isinstance(t, const)
    assert isinstance(n, const)
    k = math.log(n.get_val()) / t.get_val()
    return prod(mult1=p0, mult2=pwr(base=const(math.e), deg=prod(mult1=const(k), mult2=pwr(base=var('t'), deg=const(1.0)))))


############################# Problem 3 ##############################

def radioactive_decay(lmbda, p0, t):
    assert isinstance(lmbda, const)
    assert isinstance(p0, const)
    assert isinstance(t, const)
    return prod(p0, pwr(const(math.e), prod(lmbda, pwr(var('x'), const(1)))))


############################# Problem 4 ##############################

def c14_carbon_dating(c14_percent):
    assert isinstance(c14_percent, const)
    lmbda = (-1.0 * math.log(1/2)) / 5777
    t = math.log(c14_percent.get_val()) / (-1.0 * lmbda)
    return const(math.ceil(t))


############################# Problem 5 ##############################

def demand_elasticity(demand_eq, price):
    assert isinstance(price, const)
    drv = deriv(demand_eq)
    elastic_eq = quot(num=prod(mult1=prod(mult1=const(-1.0), mult2=price), mult2=drv), denom=demand_eq)
    tf = tof(elastic_eq)
    elastic_val = tf(price.get_val())
    return const(elastic_val)


def is_demand_elastic(demand_eq, price):
    assert isinstance(price, const)
    elastic_val = demand_elasticity(demand_eq, price)
    if elastic_val.get_val() > 1:
        return True
    elif elastic_val.get_val() < 1:
        return False
    else:
        raise Exception("is_demand_elastic error 1")


def expected_rev_dir(demand_eq, price, price_direction):
    assert isinstance(price, const)
    assert isinstance(price_direction, const)
    assert price_direction.get_val() == 1 or price_direction.get_val() == -1
    is_elastic = is_demand_elastic(demand_eq, price)
    if is_elastic:
        if price_direction.get_val() == 1:
            return -1
        elif price_direction.get_val() == -1:
            return 1
    elif not is_elastic:
        if price_direction.get_val() == 1:
            return 1
        elif price_direction.get_val() == -1:
            return -1
    else:
        raise Exception("expected_rev_dir error 1")



