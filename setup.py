from setuptools import setup

setup(
    name='annotation_converter',
    version='0.1.0',    
    description='An API to convert annotation formats from kognic to openlabel styles',
    url='https://github.com/Anqi-Li/API-annotated_file_converter',
    author='Anqi Li',
    author_email='li.a.titech@gmail.com',
    # license='BSD 2-clause',
    packages=['annotation_converter'],
    install_requires=['flask',
                      'requests',
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        # 'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)