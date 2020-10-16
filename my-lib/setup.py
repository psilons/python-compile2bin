from setuptools import setup
from setuptools.extension import Extension
# from distutils.core import setup
# from distutils.extension import Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize

# In Cython, we need to specify every module that we want to compile
# There is no automatic dependency traversal.
# We may group them in one entry, or use separate entries like below.
ext_modules = [
    Extension("my_lib.klotski",  ["src/my_lib/klotski.py"]),
    Extension("my_lib.stack_queue_impl",  ["src/my_lib/stack_queue_impl.py"]),
]

setup(
    name='my_lib',
    cmdclass={'build_ext': build_ext},
    ext_modules=cythonize(
        ext_modules,
        build_dir="build",
        compiler_directives={'language_level': "3"}),
)
