from setuptools import setup

setup(
    name='ebird-count-scripts',
    version='0.1',
    url='',
    license='Apache',
    author='steve pousty',
    author_email='steve.pousty@gmail.com',
    description='some scripts I put together to help section leads tabulate their counts from eBird',
    install_requires=[
        'ebird.api==3.0.6'
    ],
    package_data={
        'aba_crosswalk': ['bird_lookup.json'],
        'surveys': ['survey_lists.txt']
    }
)
