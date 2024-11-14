from datetime import datetime
class Info:
    def __init__(self,nev:str="",szul_dat:int="",fizetes:int=250000,pozicio:str=""):
        self.nev=nev
        self.szul_dat=szul_dat
        self.fizetes=fizetes
        self.pozicio=pozicio
        self.kor=self.korbeallit()
        
    def korbeallit(self):
        jelenlegi_ev= datetime.now().year
        return jelenlegi_ev-self.szul_dat
        
        
    def __str__(self):
        return f"Név:{self.nev}, Kor: {self.korbeallit} éves, Születési dátum: {self.szul_dat} Beosztás:{self.pozicio}, Fizetés:{self.fizetes} Ft"

    def fizetes_emeles(self, szazalek):
        self.fizetes *=(1+szazalek/100)