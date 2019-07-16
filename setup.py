from setuptools import setup
from os import path


here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='lumes',
    version='0.0.2a3',
    description='A simple wraper for screenshot',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/juliancoffee/lumes',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Utilities',
        'Operating System :: POSIX :: Linux',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3, <4',
    keywords='screenshot',
    packages=['lumes'],
    entry_points={
        'console_scripts': [
            'lumes=lumes.__main__:main',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/juliancoffee/lumes/issues',
        'Source': 'https://github.com/juliancoffee/lumes/',
    },
)
