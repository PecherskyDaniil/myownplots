from setuptools import setup

with open("requirements.txt") as f:
    requirements=f.read().splitlines()

setup(
   name='myownplots',
   version='1.0',
   description='Allows to create simple plots.',
   license='MIT',
   author='Daniil Pechersky',
   author_email='cdtt38.pecherskyD@yandex.ru',
   url='https://github.com/PecherskyDaniil/myownplots',
   packages=['myownplots'],
   install_requires=requirements, # it is empty since we use standard python library
   extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
   },
   python_requires='>=3',
)
