#!/usr/bin/python3

from fractions import fraction as fh

frac1, frac2, op = tuple(input('Enter expression: ').split())

try:
    frac1 = tuple(map(int, frac1.split('/')))
    frac2 = tuple(map(int, frac2.split('/')))
except TypeError:
    print('The numerator and denominator need to be integers.')

a = fh(frac1[0], frac1[1])
b = fh(frac2[0], frac2[1])

print('{0}, {1}'.format(a, b))