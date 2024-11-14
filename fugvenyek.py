def etlap(lista):
    for i in range(0,len(lista),1):
        print(f"** {lista[i].nev} {lista[i].ar:>8}FT **")

def atlag_ar(lista):
    ossz:float=0
    for i in range(0, len(lista),1):
        ossz+=lista[i].ar
    return ossz/len(lista)

def legdragabb(lista):
    max_index=0
    for i in range(0,len(lista),1):
        if (lista[i].ar>lista[max_index].ar):
            max_index=i
    return max_index

'''Alkalmazottak feladat'''
def dolgozo(lista):
    for i in range(0,len(lista),1):
        print(f" Név:{lista[i].nev}, Kor: {lista[i].kor} éves, Születési dátum: {lista[i].szul_dat} Beosztás:{lista[i].pozicio}, Fizetés:{lista[i].fizetes} Ft")
        
def ossz_fizetes(lista):
    ossz:int=0
    for i in range(0,len(lista),1):
        ossz+=lista[i].fizetes
    return ossz

def idosebb(lista):
    max_index=0
    for i in range(0,len(lista),1):
        if (lista[i].kor>lista[max_index].kor):
            max_index=i
    return max_index