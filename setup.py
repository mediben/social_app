from setuptools import setup

setup (
    name='Socially',
    version='1.0.0',
    author='Mehdi Ben Taarit',
    description="A small Social Networking package",
    py_modules=['socially'],
    entry_points='''
        [console_scripts]
        socially=app.__init__:main
    '''
)
