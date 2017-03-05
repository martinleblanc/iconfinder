from setuptools import setup


setup(
    version='1.0.0',
    author='babykick',
    license='BSD',
    py_modules=['iconfinder', 'unmark'],
    install_requires=open('requirements.txt').read().splitlines(),
    entry_points={
        'console_scripts':['iconfinder=iconfinder:cli'],
    },

)