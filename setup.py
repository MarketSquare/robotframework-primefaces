from setuptools import setup, find_packages

setup(
    name='robotframework-primefaces',
    version='0.0.1',
    description="""A PrimeFaces extension to Robot Framework's SeleniumLibrary.""",
    url='https://github.com/emanlove/robotframework-primefaces',
    author='Ed Manlove',
    author_email='devPyPlTw@verizon.net',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Robot Framework :: Library',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programing Language :: JavaScript',
        'Topic :: Software Development :: Testing',
    ],
    keywords='robotframework testing testautomation primefaces javaserverfaces selenium webdriver',
    package_dir={'':'src'},
    packages=find_packages('src'),
    install_requires=['robotframework', 'robotframework-seleniumlibrary'],
    
)
