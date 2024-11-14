class Etel:
    def __init__(self,nev:str="",ar:int=1000):
        self.nev=nev
        self.ar=ar
        self.alapot="készül"
    def keszul(self):
        self.alapot="Kész"