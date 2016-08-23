from setuptools import setup,find_packages

setup(
name = 'pygron',
version = '0.3.1',
license = 'MIT',
author = 'Akshay B N',
description = 'Helps JSON become greppable',
zip_safe = False,
url = 'https://github.com/akshbn/pygron',
packages = find_packages(),
entry_points = {"console_scripts":["pygron=pygron.cli_entry:main"]}
)
