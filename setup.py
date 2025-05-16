import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='itp',
    version='1.1.0',
    author='Jeff Grant, Jiaming Chang',
    author_email='justinchang2021@outlook.com',
    description='An extended package for querying Ice Tethered Profiler data with additional features',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/JustinTrenchcoat/ITP-Python',
    project_urls={
        'Original Project': 'https://github.com/WHOI-ITP/ITP-Python',
        'Bug Tracker': 'https://github.com/JustinTrenchcoat/ITP-Python/issues',
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    package_dir={'': 'src'},
    packages=['itp'],
    python_requires='>=3.8',
    install_requires=[
        'numpy',
        'gsw'
    ]
)
