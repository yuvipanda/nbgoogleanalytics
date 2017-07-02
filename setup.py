import setuptools

setuptools.setup(
    name="nbgoogleanalytics",
    version='0.1.0',
    url="https://github.com/yuvipanda/nbgoogleanalytics",
    author="Yuvi Panda",
    description="Simple Jupyter extension to show how much resources (RAM) your notebook is using",
    packages=setuptools.find_packages(),
    install_requires=[
        'notebook',
    ],
    package_data={'nbgoogleanalytics': ['static/*']},
)
