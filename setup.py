import setuptools

with open('README.md') as fh:
    long_description = fh.read()

setuptools.setup(
    name='python-smartthings-kalebr3',
    version='2020.10a1',
    author='Kaleb Redman',
    author_email='kaleb@redman.us',
    description='A Python Package for Interacting with SmartThings',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='',
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