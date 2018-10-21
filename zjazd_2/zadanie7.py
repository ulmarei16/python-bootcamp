
def liczenie_w_nawiasie(napis, start="<", end=">"):
    #napis = input(str("Podaj napis i umieść jedno słowo w nawiasie <> : "))
    #il_znak = 0
    # czy_miedzy_nawias = False
    # for znak in napis:
    #     if znak == "<":
    #         czy_miedzy_nawias = True
    #     elif znak == ">":
    #         czy_miedzy_nawias = False
    #     elif czy_miedzy_nawias:
    #         il_znak += 1
    start_i = 0
    wynik = 0
    end_i = 0

    if "<" in napis:
        start_i = napis.index("<")

    if ">" in napis:
        end_i = napis.index(">")

    wynik = end_i - start_i -1
    return wynik





def test_liczenie_w_nawiasie_ostrokatnym():
    assert liczenie_w_nawiasie("ala ma <kota> a kot ma ale") == 4

# def test_liczenie_w_nawiasie_ostrokatnym_kilka_poziomow():
#      assert liczenie_w_nawiasie("a <a<a<a>>>") == 6