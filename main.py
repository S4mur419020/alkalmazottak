'''hozz ltre egy osztályzatok listát és osztalyzatok=[2,4,5,3,2,4]
nevek=["Béla","Jenő","Ági","Rozi"]

neve és a nevekhez tartozó osztályzatok összetartoznak

etelek=["húsleves","palapicsa"]
ar=[1234,4235]

új adatszrkezet - ami egybe tudja kezelni az összetartozó adatokat

személy={nevek: "Béla", osztályzat:3}

kaja1={nev:"húsleves", ar:1234}
kaja2={nev:"húsleves", ar:1234}

objektumok - tulajdonságokkal (főnevek) és 
viselkedéssel (cselekvés) bíró adatszerkezet

'''


import fugvenyek

'''from Etel import Etel

etel1=Etel("húsleves",1234)
etel2=Etel("palacsinta",231)
etel3=Etel("rántott hús",2310)
etel4=Etel("sültkrumpli",1450)
etel_lista=[]
etel_lista.append(Etel("húsleves",1234))
etel_lista.append(Etel("palacsinta",231))
etel_lista.append(Etel("rántott hús",2310))
etel_lista.append(Etel("sültkrumpli",1450))

print("Szia én vagyok a"+etel1.nev+"Az állapotom "+ etel1.alapot)

etel1.keszul()
print("Szia én vagyok a"+etel1.nev+"Az állapotom "+ etel1.alapot)
print("Szia én vagyok a"+etel2.nev+"Az állapotom "+ etel2.alapot)

fugvenyek.etlap(etel_lista)

atlag_ar=fugvenyek.atlag_ar(etel_lista)
print(f"Az ételek átlaga: {atlag_ar}")

maxi=fugvenyek.legdragabb(etel_lista)
print(f"A legdragabb étel neve és ára {etel_lista[maxi].nev}, {etel_lista[maxi].ar}")'''


'''hozz létre egy alkalmazott osztályt,amelyben sz alábbi infókat tudod tárolni és cég dolgozóitól:
név
szul_dat
fizetes
pozicio

Készíts metódust , ami megmondja az adott ember korát
__str__

Hozz létre legalább 5 embert, tedd bele egy listába
- menniy az össz fizetés?
-hány éves a legidősebb ember?
-hány ember van "beosztott" pozicióba?
-kinek a legalacsonyabb a fizetése?

++az osztálynak legyen egy fizetés emelés metódusa,amelyik a fizetést megemeli a paraméterében megadott százalék értékét.
A legkisebb fizetésű ember fizetése 20%-kal.
'''
from Info import Info

munkas1=Info("Izsák",2000,260000,"HRS")
munkas2=Info("Imre",1973,297000,"Branch managger")
munkas3=Info("Jani",1999,267000,"Takarító")
munkas4=Info("István",1984,250000,"Újonc")
munkas5=Info("Frodó",1998,450000,"vezető helyettes")
munkas6=Info("Lakatos Bilbó",2001,300000,"Beosztott")
munkas7=Info("Helga",2002,600000,"CEO")
alkalmazottak=[]
alkalmazottak.append(Info("Izsák",2000,260000,"HRS"))
alkalmazottak.append(Info("Imre",1973,297000,"Branch managger"))
alkalmazottak.append(Info("Jani",1999,267000,"Takarító"))
alkalmazottak.append(Info("István",1984,250000,"Újonc"))
alkalmazottak.append(Info("Frodó",1998,450000,"vezető helyettes"))
alkalmazottak.append(Info("Lakatos Bilbó",2001,300000,"Beosztott"))
alkalmazottak.append(Info("Helga",2002,600000,"CEO"))

fugvenyek.dolgozo(alkalmazottak)

ossz_fizetes=fugvenyek.ossz_fizetes(alkalmazottak)
print(f"Az össz fizetés: {ossz_fizetes} Ft.")

legidosebb=fugvenyek.idosebb(alkalmazottak)
print(f"A legidősebb dolgozó {legidosebb} éves.")
