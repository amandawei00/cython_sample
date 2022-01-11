For clarity:
1. test.pyx contains Cython code.
2. test.pxd contains method signatures of functions in test.pyx which we would like to use as integrands which we pass to LowLevelCallable. This file really only exists here because LowLevelCallable requires it in order to translate the function passed to it into native code.
3. setup.py is run with the command 'python setup.py build_ext --inplace' which will generate a shared object file from the .pyx Cython file.
4. Running setup.py will result in the file with the name test.cpython-36m-x86_64-linux-gnu.so. setup.py needs to be called whenever test.pyx is changed in order to see the changes in the shared object.
5. run.py imports the shared object file and tests the Cython version of things by calling its functions.
6. benchmark.py compares the speed of an integral as called in Python with the speed of the same integral called with Cython.

I am running the code in Linux with the following versions. Sometimes, differences in versions can cause annoying errors so this is something worth double checking.
Python 3.6.8
Cython 0.29.14
gcc 4.8.5
