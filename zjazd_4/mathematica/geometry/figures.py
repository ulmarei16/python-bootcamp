def square_area(bok):
    if bok < 0:
        print("Bok musi być większy od zera.")
        return None
    return bok**2

def triangle_area(podst,wys):
    if podst < 0 or wys < 0:
        print("Podstawa i/lub wysokość musi być większy od zera.")
        return None
    return podst*wys/2