from distutils.core import setup

setup(
    name='mapreduce',
    version='0.0.1',
    author='Abhiraj Butala',
    py_modules=[
        'mapreduce',
        'stopwords'
    ],
    scripts=[
        'mapreduce.py',
        'stopwords.py'
    ],
    install_requires=[
        'mincemeat >= 0.1.2'
    ]
)
