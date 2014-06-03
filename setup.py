#
# This file is autogenerated during plugin quickstart and overwritten during
# plugin makedist. DO NOT CHANGE IT if you plan to use plugin makedist to update 
# the distribution.
#

from setuptools import setup, find_packages

kwargs = {'author': 'Kennth T. Moore',
 'author_email': 'kenneth-t-moore-1@nasa.gov',
 'classifiers': ['Intended Audience :: Science/Research',
                 'Topic :: Scientific/Engineering'],
 'description': 'OpenMDAO component wrapper for PDCYL',
 'download_url': '',
 'entry_points': '[openmdao.component]\npdcyl_comp.pdcyl_comp.PdcylComp=pdcyl_comp.pdcyl_comp:PdcylComp\n\n[openmdao.container]\npdcyl_comp.pdcyl_comp.PdcylComp=pdcyl_comp.pdcyl_comp:PdcylComp',
 'include_package_data': True,
 'install_requires': ['openmdao.main'],
 'keywords': ['openmdao'],
 'license': 'Apache License, Version 2.0',
 'maintainer': 'Kennth T. Moore',
 'maintainer_email': 'kenneth.t.moore-1@nasa.gov',
 'name': 'pdcyl_comp',
 'package_data': {'pdcyl_comp': ['sphinx_build/html/index.html',
                                 'sphinx_build/html/.buildinfo',
                                 'sphinx_build/html/py-modindex.html',
                                 'sphinx_build/html/objects.inv',
                                 'sphinx_build/html/searchindex.js',
                                 'sphinx_build/html/search.html',
                                 'sphinx_build/html/pkgdocs.html',
                                 'sphinx_build/html/usage.html',
                                 'sphinx_build/html/genindex.html',
                                 'sphinx_build/html/srcdocs.html',
                                 'sphinx_build/html/_sources/usage.txt',
                                 'sphinx_build/html/_sources/pkgdocs.txt',
                                 'sphinx_build/html/_sources/index.txt',
                                 'sphinx_build/html/_sources/srcdocs.txt',
                                 'sphinx_build/html/_static/plus.png',
                                 'sphinx_build/html/_static/comment-bright.png',
                                 'sphinx_build/html/_static/comment.png',
                                 'sphinx_build/html/_static/down-pressed.png',
                                 'sphinx_build/html/_static/sidebar.js',
                                 'sphinx_build/html/_static/doctools.js',
                                 'sphinx_build/html/_static/ajax-loader.gif',
                                 'sphinx_build/html/_static/default.css',
                                 'sphinx_build/html/_static/down.png',
                                 'sphinx_build/html/_static/jquery.js',
                                 'sphinx_build/html/_static/underscore.js',
                                 'sphinx_build/html/_static/minus.png',
                                 'sphinx_build/html/_static/up-pressed.png',
                                 'sphinx_build/html/_static/up.png',
                                 'sphinx_build/html/_static/pygments.css',
                                 'sphinx_build/html/_static/searchtools.js',
                                 'sphinx_build/html/_static/file.png',
                                 'sphinx_build/html/_static/basic.css',
                                 'sphinx_build/html/_static/websupport.js',
                                 'sphinx_build/html/_static/comment-close.png',
                                 'sphinx_build/html/_modules/index.html',
                                 'sphinx_build/html/_modules/pdcyl_comp/pdcyl_comp.html',
                                 'sphinx_build/html/_modules/pdcyl_comp/test/test_pdcyl_comp.html',
                                 'test/transport.dump',
                                 'test/__init__.py',
                                 'test/transport.in',
                                 'test/test_pdcyl_comp.py',
                                 'test/transport.out',
                                 'test/openmdao_log.txt']},
 'package_dir': {'': 'src'},
 'packages': ['pdcyl_comp', 'pdcyl_comp.test'],
 'url': 'https://github.com/OpenMDAO-Plugins/pdcyl_comp',
 'version': '0.4.1',
 'zip_safe': False}


setup(**kwargs)

