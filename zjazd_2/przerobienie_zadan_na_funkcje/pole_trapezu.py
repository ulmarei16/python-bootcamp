def pole_trapezu(a,b,h):
    pole = (a+b) * h / 2

    return pole

"""
liczy pole trapezu
:param: a: podatawa trapezu 1 - numeric
:param: b: podatawa trapezu 2 - numeric
:param: c: wysokość trapezu 1 - numeric
return 
"""

def test_pole_trapezu():
    assert pole_trapezu(3,9,6.5) == 39