import random

Kaarten = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
Kleur = ['groen', 'blauw', 'geel', 'rood']
Special = ['+2', 'sla een beurt over', 'reverse']
Kleurloos = ["+4", "kies een kleur"]
Stapel = []
Spelerskaarten = []
AIKaarten = []
pile = []

for x in range(4):
    color = Kleur[x]
    Stapel.append(color + " 0")
    for z in range(2): 
        for y in range(9):
            Stapel.append(color +" "+ Kaarten[y])
        for c in range(3):
            Stapel.append(color + " " + Special[c])
for x in range(4):
    for y in range(2):
        Stapel.append(Kleurloos[y])
random.shuffle(Stapel)

def startGame():
    input("Druk ENTER om te beginnen met UNO!")
    startTurn = random.randint(0, 1)
    for x in range(7):
        AIKaarten.append(Stapel[0])
        Stapel.pop(0)
        Spelerskaarten.append(Stapel[0])
        Stapel.pop(0)
    pile.append(Stapel[0])
    Stapel.pop(0)
    if startTurn == 0:
        print("Player begins.")
    if startTurn == 1:
        print("Opponent begins.")


def showDevinfo():
    print("de stapel in het midden van de tafel: "+ ", ".join(pile))
    print("uw huidige hand: "+ ", ".join(Spelerskaarten))
    print("de huidige hand van de tegenstander: " + ", ".join(AIKaarten))

startGame()
showDevinfo()