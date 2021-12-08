import random

position1 = []
position2 = []
position3 = []
position4 = []
position5 = []
position6 = []
positionA = []
positionB = []
positionC = []
positionD = []
positionE = []
positionF = []
positionG = []
counter = {}

i = 0
ending = ('')
extracounter = ''
yahtzeecounter = 0
extrayahtzeepoints = 0
endscore = 0
rerollQuestion = False
allRollsc = {}

dice = [1,2,3,4,5,6]
roll1 = random.choice(dice)
roll2 = random.choice(dice)
roll3 = random.choice(dice)
roll4 = random.choice(dice)
roll5 = random.choice(dice)

print('\nຟēlk໐๓ ๖iว ฯคhtຊēē pฯth໐ຖ ē໓iti໐ຖ!\n')

def dictonary():
    global i, allRolls
    for x in range(0,5):
        if allRollsc[i] in allRollsc:
            allRollsc[allRollsc[i]] += 1
            i = int(i) + 1
        else:
            allRollsc.update({allRollsc[i] : 1})
            i = int(i) + 1 
        if x == 5:
            return allRollsc

def diceRoll():
    global rerollQuestion, ending 
    print('De gerolde getallen zijn:'+ str(roll1) +', ' + str(roll2) +', ' + str(roll3) + ', ' + str(roll4) + ', ' + str(roll5))
    rerollQuestion = input('Geef aan van welke positie(s) je nog een keer wilt rollen (bijv: "3 4 6 2") of typ "niks" als je niet nog een keer wilt. ')
    if rerollQuestion.lower() == 'geen':
        ending = True
        return False
    else:
        diceRoll()



diceRoll()
