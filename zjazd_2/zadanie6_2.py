def wiecej_niz(napis, zadana_liczba):
    wiecej_niz_zadana = set()
    napis = napis.lower()
    for znak in napis:
        if napis.count(znak) > zadana_liczba:
            wiecej_niz_zadana.add(znak)
    return wiecej_niz_zadana



def test_wiecej_niz_dla_pustego_napisu():
    assert wiecej_niz("", 0) == set()


def test_wiecej_niz_dla_nie_pustego_napisu():
    assert wiecej_niz("aaaaaaaabbbbccd", 2) == set('a', 'b')


def test_wiecej_niz_dla_nie_pustego_napisu_male_duze():
    assert wiecej_niz("aaaaaAAAabbbccd", 4) == set('a')