from setuptools import find_packages, setup

with open('README.md') as f:
    readme = f.read()

setup(
    name='UMNWWCHS',
    version='1.0.0',
    description='Sample package for Python-Guide.org',
    long_description=readme,
    author='Magdalena Szulc',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=[
        'flask', 'scikit-learn'
    ],
)