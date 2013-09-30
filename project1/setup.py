from distutils.core import setup

setup(
    name='mapreduce',
    version='0.0.1',
    author='Abhiraj Butala',
    py_modules=[
        'src.mapreduce',
        'src.stopwords'
    ],
    scripts=[
        'src/mapreduce.py',
        'src/stopwords.py'
    ],
    install_requires=[
        'mincemeat >= 0.1.2'
    ]
)
