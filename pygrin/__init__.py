"""
Gradient Index lens calculations and plots.

More documentation at <https://pygrin.readthedocs.io>

Functions to locate focal points and cardinal points::
    BFL(n_0, pitch, length)
    EFL(n_0, pitch, length)
    FFL(n_0, pitch, length)
    NA(n_0, pitch, length, diameter)
    cardinal_points(n_0, pitch, length)

Functions to find properties of GRIN lens::
    gradient(pitch, length)
    period(grad, length)
    max_angle(n_0, pitch, length, diameter)
    ABCD(n_0, pitch, length, z)
    image_distance(n_0, pitch, length, s)
    image_mag(n_0, pitch, length, s)

Functions to determine refractive index profile::
    hyperbolic_secant_profile_index(n_0, alpha, r)
    parabolic_profile_index(n_0, pitch, length, r)

Functions to help raytrace through GRIN lens.
    full_meridional_curve(n_0, pitch, length, z_obj, r_obj, r_lens)
    meridional_curve(n_0, pitch, length, r_i, theta_i)
    plot_principal_planes(n_0, pitch, length, diameter)
"""
from .pygrin import *
