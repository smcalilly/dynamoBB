from setuptools import setup

setup(
    name='dynamo-bb',
    version='0.0.11',
    description='Baby wrapper classes for interfacing with DynamoDB',
    url='git@github.com:smcalilly/dynamoBB.git',
    author='Sam McAlilly',
    author_email='smcalilly@gmail.com',
    license='MIT',
    packages=['dynamoBB'],
    install_requires=[
        'boto3'
    ],
    zip_safe=False
)