from setuptools import setup, find_packages

setup(

    name=   'mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_required = ['numpy'],
    url='http',
    author='<Mahmoud Saad>',
    author_email='<mahmoudsaad191988@gmail.com>'

)
