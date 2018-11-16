
def liczenie_w_nawiasie(napis, start="<", stop=">"):
    level = 0
    wynik = 0
    for znak in napis:
        if znak == start:
            level += 1
        elif znak == stop:
            level -= 1
        else:
            wynik += level

    return print(wynik)

liczenie_w_nawiasie("a <a<a<a>>>")



def test_liczenie_w_nawiasie_ostrokatnym():
    assert liczenie_w_nawiasie("ala ma <kota> a kot ma ale") == 4

def test_liczenie_w_nawiasie_ostrokatnym_kilka_poziomow():
      assert liczenie_w_nawiasie("a <a<a<a>>>") == 6

def test_licznie_w_nawiasie_kwadrartowym():
    assert liczenie_w_nawiasie("ala [kota [a kot]] ma [ale]", "[", "]") == 18