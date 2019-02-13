#!/usr/bin/env python
import numpy as np


def main():
    a = 1
    b = -10000000.0000001
    c = 1
    print("first program:")
    solve_quadratic(a, b, c)
    print("second program:")
    solve_quadratic_fixed(a, b, c)


def solve_quadratic(a, b, c):
    desc = b*b - 4*a*c
    x1 = (-b + np.sqrt(desc)) / 2 * a
    x2 = (-b - np.sqrt(desc)) / 2 * a
    print("x1= %s\nx2= %s" % (x1, x2))
    x1_sol = a * x1 * x1 + b * x1 + c
    x2_sol = a * x2 * x2 + b * x2 + c
    print("for x1 solution is %s" % x1_sol)
    print("for x2 solution is %s\n" % x2_sol)


def solve_quadratic_fixed(a, b, c):
    desc = b*b - 4*a*c
    x1 = (-b + np.sqrt(desc)) / 2 * a
    x2 = (-2*c) / (b - np.sqrt(desc))
    print("x1= %s\nx2= %s" % (x1, x2))
    x1_sol = a * x1 * x1 + b * x1 + c
    x2_sol = a * x2 * x2 + b * x2 + c
    print("for x1 solution is %s" % x1_sol)
    print("for x2 solution is %s" % x2_sol)


if __name__ == '__main__':
    main()

