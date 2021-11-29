import random
import time
import string
KleineLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
HoofdLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
SpecialeTekens = ['@', '#', '$', '%', '&', '_', '?', '.']
Cijfer = ['0', '2', '3', '4', '5', '6', '7', '8', '9']
Wachtwoord = []

for x in range (random.randint(2,6)):
    randomHoofdletters = random.randint(0,23)
    random.choice(HoofdLetters)
    Wachtwoord.append(HoofdLetters[randomHoofdletters])

for x in range (random.randint(4,7)):
    randomcijfers = random.randint(0,8)
    random.choice(Cijfer)
    Wachtwoord.append(Cijfer[randomcijfers])

for x in range(random.randint(3,3)):
    randomSpecials = random.randint(0,6)
    random.choice(SpecialeTekens)
    Wachtwoord.append(SpecialeTekens[randomSpecials])

while len(Wachtwoord) != 24:
    kleineLettersList = list(string.ascii_lowercase)
    randomKleineLetters = random.randint(0,23)
    Wachtwoord.append(KleineLetters[randomKleineLetters])
    random.shuffle(SpecialeTekens)
print('Generating password...')
time.sleep(1)

print(Wachtwoord)