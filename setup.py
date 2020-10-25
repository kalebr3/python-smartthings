import setuptools

with open('README.md') as fh:
    long_description = fh.read()

setuptools.setup(
    name='python-smartthings',
    version='1.0.0',
    author='Kaleb Redman',
    author_email='dev@redman.us',
    description='A Python Package for Interacting with SmartThings',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/kalebr3/python-smartthings',
    packages=setuptools.find_packages(),
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)