#!/usr/bin/env python

from setuptools import setup
import pip

pip.main(['install', '-r', 'requirements.txt'])

setup(
    name='Deck_Evaluator',
    version='0.1.0',
    description='Deck Evaluator',
    packages=['Deck_Evaluator'],
    entry_points={
        'console_scripts': ['balance-tester=Deck_Evaluator.mages:main']
    }
)
