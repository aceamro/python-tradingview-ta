import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='tradingview_ta',
    version='2.1.0',
    description="A python module to scrape tradingview's technical analysis.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/deathlyface/python-tradingview-ta',
    author='deathlyface',
    author_email='bri4nong@gmail.com',
    packages=['tradingview_ta'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
          'selenium',
    ],
    python_requires='>=3.6')
