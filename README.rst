pygrin
======

A basic collection of routines to ray trace through graded
index (GRIN) lenses with a parabolic radial profile.

Usage
-----

Example Light paths in a 0.25 pitch GRIN lens from an ancient Melles Griot Catalog::

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

Source code is available at <https://github.com/scottprahl/pygrin> or the module
can be installed using `pip`::

    pip install --user pygrin

License
-------
pygrin is licensed under the terms of the MIT license.