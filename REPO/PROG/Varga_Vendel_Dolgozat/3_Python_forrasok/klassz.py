class varos:
    def __init__(self, sor):
        adatok = sor.strip().split(";")
        self.nev = adatok[0]
        self.orszag = adatok[1]
        self.szam = int(adatok[2])