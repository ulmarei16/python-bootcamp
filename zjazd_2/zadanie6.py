def wiecej_niz(napis,zadana_liczba):
    licznik_lit = {}
    wiecej_niz_zadana = set()
    for znak in napis:
        znak = znak.lower
        licznik_lit[znak] = licznik_lit.get(znak,0) + 1
        if int(licznik_lit[znak]) > zadana_liczba:
            wiecej_niz_zadana.add(znak)
    print(wiecej_niz_zadana)

# napis = input("Podaj napis: ")
# zadana_liczba = int(input("Więcej niż ile: "))
# wiecej_niz(napis)

def test_wiecej_niz_dla_pustego_napisu():
    assert wiecej_niz("",0) == set()

def test_wiecej_niz_dla_nie_pustego_napisu():
    assert wiecej_niz("aaaaaaaabbbbccd",2) == set('a','b')

def test_wiecej_niz_dla_nie_pustego_napisu_male_duze():
    assert wiecej_niz("aaaaaAAAabbbccd",4) == set('a')
