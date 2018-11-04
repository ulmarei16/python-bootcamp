import sys
if len (sys.argv) > 1:
    nazwa_pliku = sys.argv[1]

    # with open(nazwa_pliku, "a") as f:
    #     i = 1
    #     for line in f:
    #        #print(f.write(numer_lini + 1, line))
    #         print(i, line, end="") #<=== end="" powoduje, ze nie dodaje dodatkowych pustych linii
    #         i += 1

    with open(nazwa_pliku, "a") as f:
        for i, line in enumerate(f, start=1):
            print(i, line, end="")


else:
    print("Podaj nazwę pliku.")




