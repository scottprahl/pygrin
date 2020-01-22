"""
A set of routines for doing GRadient Index lens calculations and plots.

import pygin

length = 7    # mm
diameter = 2  # mm
r = np.linspace(-1,1,11) # mm

n_0 = 1.48
pitch = 0.25
theta_i = 0

aplt = pygrin.principal_planes_plt(n_0, pitch, length, diameter)
for r_i in r:
    z,r = pygrin.meridional_curve(n_0, pitch, length, r_i, theta_i)
    plt.plot(z,r,color='blue')

aplt.show()
"""

# pylint: disable=invalid-name
# pylint: disable=too-many-arguments

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

__all__ = ('ABCD',
           'BFL',
           'EFL',
           'FFL',
           'NA',
           'cardinal_points',
           'full_meridional_curve',
           'gradient',
           'hyperbolic_secant_profile_index',
           'image_distance',
           'image_mag',
           'max_angle',
           'meridional_curve',
           'parabolic_profile_index',
           'period',
           'principal_planes_plt',
           )


def gradient(pitch, length):
    """
    Return the gradient of a grin lens based on its pitch and length.

    Args:
        pitch : pitch or period of the lens [unitless]
        length : length of grin lens [mm]

    Returns:
        the gradient characterizing the index of refraction profile [1/mm]
    """
    return 2 * np.pi * pitch / length


def period(grad, length):
    """
    Return the period or pitch of a grin lens based on its gradient and length.

    Args:
        grad : geometric gradient of the lens [1/mm]
        length : length of grin lens [mm]

    Returns:
        the pitch or period of the grin lens [unitless]
    """
    return length * grad / (2 * np.pi)


def parabolic_profile_index(n_0, pitch, length, r):
    """
    Return the index of a parabolic grin lens at a particular radius.

    Args:
        n_0 : index of refraction at center of grin lens [unitless]
        pitch : pitch or period of the lens [unitless]
        length : axial length of the lens [mm]
        r : distance from center of lens [mm]

    Returns:
        the index of a parabolic grin lens at r [unitless]
    """
    return n_0 * (1 - 2 * (np.pi * pitch * r / length)**2)


def hyperbolic_secant_profile_index(n_0, alpha, r):
    """
    Return the index of a hyperbolic secant grin lens at a particular radius.

    Args:
        n_0 : index of refraction at center of grin lens [unitless]
        alpha : parameter (like gradient for parabolic lens) [1/mm]
        r : distance from center of lens [mm]

    Returns:
        the index of a parabolic grin lens at r [unitless]
    """
    return np.sqrt(1 + (n_0**2 - 1.0)/np.cosh(alpha*r)**2)


def EFL(n_0, pitch, length):
    """
    Return the effective focal length of a grin lens.

    Args:
        n_0 : index of refraction at center of grin lens [unitless]
        pitch : pitch or period of the lens [unitless]
        length : axial length of the lens [mm]

    Returns:
        the effective focal length of the grin lens [mm]
    """
    return length / np.sin(2 * np.pi * pitch) / (2 * np.pi * pitch * n_0)


def FFL(n_0, pitch, length):
    """
    Return the front focal length of a grin lens.

    Args:
        n_0 : index of refraction at center of grin lens [unitless]
        pitch : pitch or period of the lens [unitless]
        length : axial length of the lens [mm]

    Returns:
        the front focal length of the grin lens [mm]
    """
    return -length / np.tan(2 * np.pi * pitch) / (2 * np.pi * pitch * n_0)


def BFL(n_0, pitch, length):
    """
    Return the back focal length of a grin lens.

    Args:
        n_0 : index of refraction at center of grin lens [unitless]
        pitch : pitch or period of the lens [unitless]
        length : axial length of the lens [mm]

    Returns:
        the back focal length of the grin lens [mm]
    """
    return length + length / np.tan(2 * np.pi * pitch) / (2 * np.pi * pitch * n_0)


def max_angle(n_0, pitch, length, diameter):
    """
    Return the maximum acceptance angle of a grin lens in air.

    Args:
        n_0 : index of refraction at center of grin lens [unitless]
        pitch : pitch or period of the lens [unitless]
        length : axial length of the lens [mm]
        diameter : diameter of the lens [mm]

    Returns:
        the maximum acceptance angle of the lens in air [radians]
    """
    return n_0 * np.sqrt(1 - np.cosh(diameter * pitch * np.pi / length)**-2)


def NA(n_0, pitch, length, diameter):
    """
    Return the numerical aperture of a grin lens in air.

    Args:
        n_0 : index of refraction at center of grin lens [unitless]
        pitch : pitch or period of the lens [unitless]
        length : axial length of the lens [mm]
        diameter : diameter of the lens [mm]

    Returns:
        the numerical aperture of the grin lens in air [unitless]
    """
    return np.sin(max_angle(n_0, pitch, length, diameter))


def ABCD(n_0, pitch, length, z):
    """
    Return ABCD matrix for meridonal ray propagation.

    Args:
        n_0 : index of refraction at center of grin lens [unitless]
        pitch : pitch or period of the lens [unitless]
        length : axial length of the lens [mm]
        z : distance within lens from front surface [mm]

    Returns:
        the ABCD matrix for meridonal ray propagation [radians]
    """
    g = gradient(pitch, length)
    cos = np.cos(g * z)
    sin = np.sin(g * z)
    return np.array([[cos, sin / g / n_0], [-n_0 * g * sin, cos]])


def image_distance(n_0, pitch, length, s):
    """
    Return the image distance for an object.

    Args:
        n_0 : index of refraction at center of grin lens [unitless]
        pitch : pitch or period of the lens [unitless]
        length : axial length of the lens [mm]
        s : distance from front of lens to object [mm]

    Returns:
        the image distance from the back of the lens [mm]
    """
    g = gradient(pitch, length)
    numer = s * np.cos(2 * np.pi * pitch) - np.sin(2 * np.pi * pitch) / g / n_0
    denom = n_0 * g * s * np.sin(2 * np.pi * pitch) + np.cos(2 * np.pi * pitch)
    return numer / denom


def image_mag(n_0, pitch, length, s):
    """
    Return the transverse magnification of an object located at s.

    Args:
        n_0 : index of refraction at center of grin lens [unitless]
        pitch : pitch or period of the lens [unitless]
        length : axial length of the lens [mm]
        s : distance from front of lens to object [mm]

    Returns:
        the transvers magnification [unitless]
    """
    g = gradient(pitch, length)
    twopp = 2 * np.pi * pitch
    return 1 / (g * n_0 * s * np.sin(twopp) - np.cos(twopp))


def cardinal_points(n_0, pitch, length, offset=0):
    """
    Return the cardinal points of a grin lens relative to first surface.

    Args:
        n_0 : index of refraction at center of grin lens [unitless]
        pitch : pitch or period of the lens [unitless]
        length : axial length of the lens [mm]

    Returns:
        the Front focal point, first lens, first principal plane,
        second principal plane, second lens, back focal point [mm]
    """
    efl = EFL(n_0, pitch, length)
    ffl = FFL(n_0, pitch, length)
    bfl = BFL(n_0, pitch, length)

    FF = offset + ffl
    FL = offset
    FPP = offset + ffl + efl
    SPP = offset + bfl - efl
    SL = offset + length
    BF = offset + bfl

    return FF, FL, FPP, SPP, SL, BF


def meridional_curve(n_0, pitch, length, r_i, theta_i, npoints=40):
    """
    Return arrays describing the path of a ray passing through a grin lens.

    Args:
        n_0 : index of refraction at center of grin lens [unitless]
        pitch : pitch or period of the lens [unitless]
        length : axial length of the lens [mm]
        r_i : radial distance that ray hits grin lens [mm]
        theta_i : angle of incidence [radians]
        npoints : (integer) number of points in the returned curve

    Returns:
        z, r: arrays of points along the curve inside the grin lens [mm]
    """
    z = np.linspace(0, length, npoints)
    V = np.array([r_i, n_0 * np.cos(np.pi / 2 - theta_i)])

    # there must be a better way to do this
    r = np.zeros(npoints)
    for i in range(npoints):
        abcd = ABCD(n_0, pitch, length, z[i])
        r[i], _ = np.dot(abcd, V)
    return z, r


def full_meridional_curve(n_0, pitch, length, z_obj, r_obj, r_lens, npoints=40):
    """
    Return arrays for the path for a ray in a GRIN lens.
    
    The light ray starts at (z_obj,r_obj) and hits the front surface of
    the front face of the GRIN lens at (0,r_lens).

    Args:
        n_0 : index of refraction at center of grin lens [unitless]
        pitch : pitch or period of the lens [unitless]
        length : axial length of the lens [mm]
        z_obj : axial position of the object [mm]
        r_obj : radius at which the ray leaves the object [mm]
        r_lens : radius at which the ray hits the lens [mm]
        npoints : (optional) number of points in the returned curve

    Returns:
        two arrays (z,r) describing the path from the object to the image
    """
    # angle in air
    theta_i = np.arctan((r_obj - r_lens) / z_obj)

    # angle inside lens at front surface
    n_lens = parabolic_profile_index(n_0, pitch, length, r_lens)
    theta_lens = np.arcsin(np.sin(theta_i) / n_lens)

    z, r = meridional_curve(n_0, pitch, length, r_lens,
                            theta_lens, npoints=npoints - 2)

    # insert point at top of object
    z = np.insert(z, 0, z_obj)
    r = np.insert(r, 0, r_obj)

    # append point at image of object
    z_img = image_distance(n_0, pitch, length, z_obj)
    mag = image_mag(n_0, pitch, length, z_obj)
    z = np.insert(z, -1, length + z_img)
    r = np.insert(r, -1, mag * r_obj)

    return z, r


def principal_planes_plt(n_0, pitch, length, diameter):
    """
    Return a plot for a grin lens showing the cardinal points.

    Args:
        n_0 : index of refraction at center of grin lens [unitless]
        pitch : pitch or period of the lens [unitless]
        length : axial length of the lens [mm]
        diameter : diameter of the lens [mm]

    Returns:
        a plot of the lens
    """
    FF, FL, FPP, SPP, SL, BF = cardinal_points(n_0, pitch, length)
    radius = diameter / 2

    rect = patches.Rectangle((FL, -radius), length,
                             diameter, lw=0, facecolor='lightgray', alpha=0.3)

    plt.axes().add_patch(rect)
    plt.plot([FL, SL], [0, 0], lw=0.5, color='black')

    if np.abs(FPP) < 10 * length:
        plt.plot([FPP, FPP], [-radius, radius], ':k')
        plt.annotate('H ', xy=(FPP, -radius), ha='right', fontsize=16)

    if np.abs(SPP) < 10 * length:
        plt.plot([SPP, SPP], [-radius, radius], ':k')
        plt.annotate(" H'", xy=(SPP, -radius), ha='left', fontsize=16)

    if np.abs(FF) < 10 * length:
        plt.scatter([FF], [0], s=50, color='black')
        plt.annotate('f ', xy=(FF, 0), ha='right', fontsize=16)

    if np.abs(BF) < 10 * length:
        plt.scatter([BF], [0], s=50, color='black')
        plt.annotate(" f'", xy=(BF, 0), ha='left', fontsize=16)

    plt.title(r'pitch=%.2f, n$_0$=%.3f' % (pitch, n_0))
    return plt
