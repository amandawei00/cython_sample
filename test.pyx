cimport cython
import numpy as np
cimport numpy as np
from libc.math cimport exp, log, sin

cdef int a = 1
cdef double b = 2.0

# simple example 1
cpdef double f(int n):
    return a + b * n


# simple example 2
cdef double f2(double x):
    return 1/(x * x)

# example of double integral
# !!! note the format of the parameters passed to this function is not the usual (double x, double y) as we would expect in Python. In order for this function to be passable to LowLevelCallable, it must be (int n, double *xx) where n specifies the number of arguments, and xx is the array of parameters. In this example, xx = [x, y]. (The * in C means *xx is a Pointer variable) !!!
cdef double f3(int n, double *xx):
    return 1/(xx[0] * xx[0]) + 1/(xx[1] * xx[1])


# final example, interfacing with C:
cdef extern from 'source.c':
    double func1(double x, double y)
    double func2(double x)

cpdef double py_func1(double x, double y):
    return func1(x, y)

cpdef double py_func2(double x):
    return func2(x)
