import math


def r(n_):
    kol = 0
    while n_ > 0:
        n_ = n_ // 10
        kol += 1
    return kol


def pi(e):
    e += 1  # предел равен единице
    n = 2
    result = 1
    while (n * n) / ((n - 1) * (n + 1)) > e:
        result *= (n * n) / ((n - 1) * (n + 1))
        n += 2
    return result*2
