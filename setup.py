# Setup.py was never replaced by [PEP518](https://peps.python.org/pep-0518/)
# and it is currently the only option to declare extension modules
from setuptools import setup
from distutils.core import Extension


def get_extensions():
    return [
        Extension(name='gdr4mock.compiled_hello_world',
                  sources=['src/gdr4mock/include/hello_world.pyx'])
    ]


setup(ext_modules=get_extensions())
