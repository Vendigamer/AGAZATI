from klassz import *

class Megoldas:
    lista = []

    def Fileolv(self):
        f = open("varosok.txt", "r", encoding="utf-8")
        f.readline()
        for sor in f:
            self.lista.append(varos(sor))
        f.close()

    def Count(self):
        print(f"3.feladat: Városok száma: {len(self.lista)}")

    def India(self):
        x = 0
        for i in self.lista:
            if i.orszag == "India":
                x += i.szam
        print(f"4.Feladat: Indiai nagyvárosok lakosságának összege: {x*1000} fő")

    def MaxKeres(self):
        x = self.lista[0]
        for i in self.lista:
            if i.szam > x.szam:
                x = i
        print(f"5.Feladat: A legnagyobb város adatai:\n\tNév: {x.nev}\n\tOrszág: {x.orszag}\n\tLakosság: {x.szam} ezer fő")

    def Magyar(self):
        x = 0
        for i in self.lista:
            if i.orszag == "Magyarország":
                x += 1
        if x == 0:
            print("6.Feladat: Nincs magyar város az adatok között!")
        else:
            print("6.Feladat: Van magyar város az adatok között!")
    def Szokoz(self):
        x = 0
        for i in self.lista:
            nev = i.nev
            adat = nev.split(" ")
            if len(adat) == 2:
                x += 1
        print(f"7.Feladat: Városok egy szóközzel: {x} db")

    def Statisztika(self):
        print("8. feladat: Statisztika:")
        stat = {}
        for i in self.lista:
            if i.orszag in stat.keys():
                stat[i.orszag] += 1
            else:
                stat[i.orszag] = 1
        for key,value in stat.items():
                print(f"{key} - {value} db")

    def FileIr(self):
        f = open("kina.txt", "w", encoding="utf-8")
        for i in self.lista:
            if i.orszag == "Kína":
                f.write(f"{i.nev};{i.szam}\n")
        f.close()

