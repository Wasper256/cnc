"""Here is utils to calculate satelites orbits ksp."""
import math


def get_angle_between_satelites(n):
    """
    Calculate angle between satelites in radians.

    Where n is number of satelites, if less that 3 -> return.
    """
    if n <= 2:
        # need at least 3 satelites to get stable connection around the planet
        return
    angle = (((n - 2) * math.pi) / n)
    return angle


def get_final_orbital_radius_due_to_angle_between_satelites(rp, sa):
    """
    Calulate radius of final orbit due to sats angle and radius of planet.

    Where:
    rp - radius of planet witch we calculating in kilomeeters,
    sa - angle betweeen the satelites in radians,
    ro - radius of final orbit on kilomeeters.
    """
    ro = (rp / (math.sin(sa / 2)))
    return ro


def get_orbital_peiod_final_orbit(ro, sgp):
    """
    Calulate final orbital period.

    Where:
    ro - radius of our final orbit in kilomeeters,
    sgp - standard gravitational parameter of planet in (km^3)/(s^2),
    tf - period of final orbit in seconds.
    """
    tf = 2 * math.pi * math.sqrt(pow(ro, 3) / sgp)
    return tf


def get_orbital_period_transfer_orbit(tf, inner, p):
    """
    Calculate period of transfer orbit due to final orbit.

    Where:
    tf - period of final orbit in seconds,
    inner - boolean parameter to mark inner or outer orbit priod is nedeed,
    p - number of periods,
    ti - period of initial in seconds.
    """
    if inner:
        ti = ((p - 1) / p) * tf
    else:
        ti = ((p + 1) / p) * tf
    return ti


def get_semi_major_axes_of_transfer_orbit(ti, sgp):
    """
    Calculate semi major axes of transfer orbit.

    Where:
    ti - period of initial in seconds,
    sgp - standard gravitational parameter of planet in (km^3)/(s^2),
    at - semi major axes of transfer orbit in kilomeeters.
    """
    at = pow(((sgp * pow(ti, 2)) / (4 * pow(math.pi, 2))), 1 / 3)
    return at


def get_perigee_of_transfer_orbit(ro, at):
    """
    Calculate semi major axes of transfer orbit.

    Where:
    ro - radius of our final orbit in kilomeeters(apoaps of transfer orbit),
    at - semi major axes of transfer orbit in kilomeeters.
    pgt - periaps of transfer orbit
    """
    pgt = 2 * at - ro
    return pgt


def get_velocity_neded_for_orbit(ro, at, sgp):
    """
    Calulate velocity for final orbit.

    Where:
    ro - radius of our final orbit in kilometers(apoaps of transfer orbit),
    at - semi major axes of transfer orbit in kilomeeters,
    sgp - standard gravitational parameter of planet in (km^3)/(s^2),
    v - velocity fir final orbit in km/s.
    """
    v = math.sqrt(((2 * sgp) / ro) - (sgp / at))
    return v


def get_attitude_from_radiuses(ro, pgt, rp):
    """
    Calculate semi major axes of transfer orbit.

    Where:
    ro - radius of our final orbit in kilomeeters(apoaps of transfer orbit),
    pgt - periaps of transfer orbit in kilometers,
    rp - radius of planet witch we calculating in kilomeeters,
    apa - apoaps altitude in kilometers,
    pga - periaps altitude in kilometers.
    """
    apa = ro - rp
    pga = pgt - rp
    return apa, pga
