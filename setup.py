from setuptools import setup

version = '0.0.1'
name = 'myapp'
short_description = 'myapp'

setup(
    name=name,
    version=version,
    author='Takashi Nishibayashi(hagino3000)',
    author_email="takashi.nishibayashi@gmail.com",
    description=short_description,
    install_requires=[],
    url='https://github.com/hagino3000/xxxxxx',
    packages=['myapp'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
)
