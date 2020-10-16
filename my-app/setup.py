from setuptools import setup, find_packages


setup(
    name='klotski_app',

    package_dir={'': 'src'},
    packages=find_packages("src"),

    install_requires=['my_lib'],

    dependency_links=[
        'file://../my-lib/dist/my_lib-0.0.0-cp38-cp38-win_amd64.whl',
    ]
)
