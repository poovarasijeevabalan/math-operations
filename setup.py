from setuptools import setup, find_packages

classifiers = [
  "Development Status :: 5 - Production/Stable",
  "Intended Audience :: Education",
  "Operating System :: Microsoft :: Windows :: Windows 10",
  "License :: OSI Approved :: MIT License",
  "Programming Language :: Python :: 3"
]

setup(
    name='math_operations',
    version='0.0.1',
    packages=find_packages(),
    description='A simple Python library for basic math operations',
    long_description=open('README.txt').read() + "\n\n" + open("change_log.txt").read(),
    author='POOVARASI N',
    author_email='poovarasi5405@gmail.com',
    url='https://github.com/poovarasijeevabalan/math-operations',
    license="MIT",
    classifiers=classifiers,
    keywords='calculator',
    install_requires=[]
)
