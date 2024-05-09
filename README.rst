.. |pypi| image:: https://img.shields.io/pypi/v/pygrin?color=68CA66
   :target: https://pypi.org/project/pygrin/
   :alt: pypi

.. |github| image:: https://img.shields.io/github/v/tag/scottprahl/pygrin?label=github&color=68CA66
   :target: https://github.com/scottprahl/pygrin
   :alt: github

.. |conda| image:: https://img.shields.io/conda/vn/conda-forge/pygrin?label=conda&color=68CA66
   :target: https://github.com/conda-forge/pygrin-feedstock
   :alt: conda

.. |doi| image:: https://zenodo.org/badge/116033943.svg
   :target: https://zenodo.org/badge/latestdoi/116033943
   :alt: doi  

.. |license| image:: https://img.shields.io/github/license/scottprahl/pygrin?color=68CA66
   :target: https://github.com/scottprahl/pygrin/blob/main/LICENSE.txt
   :alt: License

.. |test| image:: https://github.com/scottprahl/pygrin/actions/workflows/test.yaml/badge.svg
   :target: https://github.com/scottprahl/pygrin/actions/workflows/test.yaml
   :alt: Testing

.. |docs| image:: https://readthedocs.org/projects/pygrin/badge?color=68CA66
   :target: https://pygrin.readthedocs.io
   :alt: Docs

.. |downloads| image:: https://img.shields.io/pypi/dm/pygrin?color=68CA66
   :target: https://pypi.org/project/pygrin/
   :alt: Downloads

pygrin
======

by Scott Prahl

|pypi| |github| |conda| |doi|

|license| |test| |docs| |downloads|

A basic collection of routines to ray trace through graded index (GRIN) lenses with a
parabolic radial profile.

.. image:: https://raw.githubusercontent.com/scottprahl/pygrin/main/docs/pitch.png
   :alt: full pitch lens

Example
-------

Properties of a 0.25 pitch GRIN lens from an ancient Melles Griot Catalog::

    import pygrin
    n = 1.608 
    gradient = 0.339 
    length = 5.37
    diameter = 1.8
    
    pitch = pygrin.period(gradient, length)
    ffl = pygrin.FFL(n,pitch,length)
    efl = pygrin.EFL(n,pitch,length)
    na = pygrin.NA(n,pitch,length,diameter)

    angle = pygrin.max_angle(n,pitch,length,diameter)
    print('expected pitch = 0.29,            calculated %.2f' % pitch)
    print('expected FFL = 0.46 mm,           calculated %.2f' % ffl)
    print('expected NA = 0.46,               calculated %.2f' % na)
    print('expected full accept angle = 55°, calculated %.0f°' % (2*angle*180/np.pi))
    print('working distance = %.2f mm'%(efl-ffl))

Produces::

    expected pitch = 0.29,            calculated 0.29
    expected FFL = 0.46,              calculated 0.47
    expected NA = 0.46,               calculated 0.46
    expected full accept angle = 55°, calculated 55°
    working distance = 1.43 mm

But the real utility of this module is creating plots that show the path of rays through
a GRIN lens.   For examples, see <https://pygrin.readthedocs.io>

Installation
------------

Use ``pip``::

    pip install pygrin

or ``conda``::

    conda install -c conda-forge pygrin

or use immediately by clicking the Google Colaboratory button below

.. image:: https://colab.research.google.com/assets/colab-badge.svg
  :target: https://colab.research.google.com/github/scottprahl/pygrin/blob/main
  :alt: Colab

License
-------
``pygrin`` is licensed under the terms of the MIT license.