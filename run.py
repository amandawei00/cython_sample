from scipy import LowLevelCallable as llc
from scipy.integrate import quad, nquad
import test

# simple example 1
x = test.f(2)
print(x)

# simple example 2
f2_py = llc.from_cython(test, 'f2')
i2 = quad(f2_py, 0.5, 4)
print(i2)

# example of double integral
f3_py = llc.from_cython(test, 'f3', signature='double (int, double *)')
i3 = nquad(f3_py, [[0.5, 4],[0.5, 4]])
print(i3)

# final example
p1 = test.py_func1(2.5, 3.5)
p2 = test.py_func2(2.0)

print(p1)
print(p2)
