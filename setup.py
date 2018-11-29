from setuptools import setup,find_packages

config = {
    'include_package_data': True,
    'description': 'Deep RegulAtory GenOmic Neural Networks (DragoNN)',
    'download_url': 'https://github.com/kundajelab/dragonn',
    'version': '0.2',
    'packages': ['dragonn'],
    'setup_requires': [],
    'install_requires': ['numpy>=1.9', 'keras>=2.2.0','tensorflow>=1.6','deeplift', 'shapely', 'simdna==0.3', 'matplotlib',
                         'scikit-learn', 'pydot_ng==1.0.0', 'h5py'],
    'extras_requires':{'tensorflow with gpu':['tensorflow-gpu>=1.7']},
    'dependency_links': ["https://github.com/kundajelab/simdna/tarball/0.3#egg=simdna-0.3"],
    'scripts': [],
    'entry_points': {'console_scripts': ['dragonn = dragonn.__main__:main']},
    'name': 'dragonn'
}

if __name__== '__main__':
    setup(**config)
