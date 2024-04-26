from setuptools import setup, find_packages

setup(
    name='LinterProject',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'flake8',
        'pylint',

    ],

    author='Sultan Alkhamshi, Atif Alanazi, Anas Altalhi',
    author_email='4020077@upm.edu.sa, 4211596@upm.edu.sa, 4211594@upm.edu.sa',
    description='In the rapidly evolving world of software development, maintaining code quality and security is paramount.'
                ' This project, Identifying Suspicious Code via ProgramAnalysis,'
                ' aims to utilize advanced linting tools to detect and address potentialvulnerabilities and inefficiencies in code.'
                ' By integrating sophisticated linters intothe development pipeline, the project seeks to enhance code '
                'reliability and securityproactively.',

    keywords='code, analysis, linting, flake8, pylint',
    url='http://url-to-your-project',
    project_urls={
        'Source Code': 'https://github.com/VIZIIER',
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
