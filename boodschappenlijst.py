
a = 0 

boodschappenlijst = []
boodschappenlijst2 = []

def BoodSchappen():
    print("Wat wilt u toevoegen op uw boodschappenlijst?")
    product = input("")
    hoeveelheid = input("Hoeveel wil er van dit product?: ")
    meer = input("wilt u nog meer producten?: ")
    if meer == 'ja':
        boodschappenlijst2 = (product, hoeveelheid)
        boodschappenlijst.append(boodschappenlijst2)
        BoodSchappen()
    else:
        boodschappenlijst2 = (product,hoeveelheid )
        boodschappenlijst.append(boodschappenlijst2)
        print(boodschappenlijst)

BoodSchappen()