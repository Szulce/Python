from setuptools import find_packages, setup

with open('README.md') as f:
    readme = f.read()

setup(
    name='UMNWWCHS',
    version='1.0.0',
    long_description=readme,
    author='Magdalena Szulc',
    include_package_data=True,
    zip_safe=False,
    packages=find_packages(exclude=('Tests', 'Docs')),
    install_requires=[
        'flask', 'scikit-learn'
    ],
)
