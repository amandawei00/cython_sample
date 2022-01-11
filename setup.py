from distutils.core import setup, Extension
from Cython.Build import cythonize

name = "test"
sources = ["test.pyx"]
dirs = ['./']

setup(
    ext_modules=cythonize(Extension(name, 
                                    sources,  
                                    extra_compile_args=['-std=c99']), annotate=True))
