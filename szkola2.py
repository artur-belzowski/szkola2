class Uczen:
    def __init__(self, imie, nazwisko, klasa):
        self.imie = imie
        self.nazwisko = nazwisko
        self.klasa = klasa


class Nauczyciel:
    def __init__(self, imie, nazwisko, przedmiot, klasy):
        self.imie = imie
        self.nazwisko = nazwisko
        self.przedmiot = przedmiot
        self.klasy = klasy


class Wychowawca:
    def __init__(self, imie, nazwisko, klasa):
        self.imie = imie
        self.nazwisko = nazwisko
        self.klasa = klasa


uczniowie = []
nauczyciele = []
wychowawcy = []
klasy = []


def utworz_uzytkownika():
    typ = input("Podaj typ użytkownika: \n U - uczen\n N - nauczyciel\n W - wychowawca \n - ")
    imie = input("Podaj imię: ")
    nazwisko = input("Podaj nazwisko: ")
    if typ == "U":
        klasa = input("Podaj klasę: ")
        uczen = Uczen(imie, nazwisko, klasa)
        uczniowie.append(uczen)
    elif typ == "N":
        przedmiot = input("Podaj przedmiot: ")
        klasy = []
        print("Podaj klasy, które prowadzi nauczyciel (wpisz pustą linię, aby zakończyć):")

        nauczyciel = Nauczyciel(imie, nazwisko, przedmiot, klasy)
        nauczyciele.append(nauczyciel)

        while True:
            klasa = input()
            if klasa == "":
                break
            klasy.append(klasa)

            print(nauczyciel.klasy)
    elif typ == "W":
        klasa = input("Podaj klasę: ")
        wychowawca = Wychowawca(imie, nazwisko, klasa)
        wychowawcy.append(wychowawca)
    else:
        print("Nieprawidłowy typ użytkownika.")


def zarzadzaj_uzytkownikami():
    typ = input("Podaj typ użytkownika do zarządzania \nU - uczen\nN - nauczyciel\nW - wychowawca\nK - klasa\n - ")
    if typ == "U":
        imie = input('Podaj imie ucznia = ')
        nazwisko = input('Podaj nazwisko ucznia = ')
        for uczen in uczniowie:
            if uczen.imie == imie and uczen.nazwisko == nazwisko:
                print(f"{uczen.imie} {uczen.nazwisko}, klasa {uczen.klasa}")
    elif typ == "N":
        imie = input('Podaj imie nauczyciela = ')
        nazwisko = input('Podaj nazwisko nauczyciela = ')
        for nauczyciel in nauczyciele:
            if nauczyciel.imie == imie and nauczyciel.nazwisko == nazwisko:
                print(f"{nauczyciel.imie} {nauczyciel.nazwisko}, przedmiot {nauczyciel.przedmiot}")
                for klasa in nauczyciel.klasy:
                    print("-", klasa)

    elif typ == "W":
        for wychowawca in wychowawcy:
            print(f"{wychowawca.imie} {wychowawca.nazwisko}, klasa {wychowawca.klasa}")

    elif typ == "K":
        klasa = input("Podaj klasę: ")
        wyniki = wyszukaj_uzytkownikow(klasa)
        if wyniki:
            print("Znaleziono użytkowników w klasie:")
            for wynik in wyniki:
                print(wynik)
        else:
            print("Nie znaleziono użytkowników w podanej klasie.")

    else:
        print("Nieprawidłowy typ użytkownika.")
        return


def wyszukaj_uzytkownikow(klasa):
    wyniki = []
    for uczen in uczniowie:
        if uczen.klasa == klasa:
            wyniki.append(f"{uczen.imie} {uczen.nazwisko} (uczeń)")

    for wychowawca in wychowawcy:
        if wychowawca.klasa == klasa:
            wyniki.append(f"{wychowawca.imie} {wychowawca.nazwisko} (wychowawca)")
    return wyniki


while True:
    komenda = input("Podaj komendę: \nU - utworz \nZ - zarzadzaj \nK - koniec\n - ")
    if komenda == "U":
        utworz_uzytkownika()
    elif komenda == "Z":
        zarzadzaj_uzytkownikami()
    elif komenda == "K":
        break
    else:
        print("Nieprawidłowa komenda.")
