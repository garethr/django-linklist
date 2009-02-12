from setuptools import setup, find_packages

setup(
    name = "django-linklist",
    version = "0.1",
    
    packages = find_packages('src'),
    package_dir = {'':'src'},
)