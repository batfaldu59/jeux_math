import random

NOMBRE_MIN = 1
NOMBRE_MAX = 10
NB_QUESTIONS = 4


def poser_question():
    a = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    b = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    # 0 -> +, 1 -> *
    choix_operateur = random.randint(0, 1)
    operateur = "+"
    if choix_operateur == 1:
        operateur = "*"
    reponse_str = input(f"Calculez: {a} {operateur} {b} = ")
    calcul = a+b
    if operateur == "*":
        calcul = a*b
    reponse_int = int(reponse_str)
    if reponse_int == calcul:
        return True
    return False


nb_points = 0
moyenne = int(NB_QUESTIONS/2)
for i in range(NB_QUESTIONS):
    print(f"Question n°{i+1} sur {NB_QUESTIONS}")
    if poser_question():
        print("Bonne réponse")
        nb_points += 1
    else:
        print("Mauvaise réponse")
    print()

print(f"Votre score est de {nb_points}/{NB_QUESTIONS}")
if nb_points == NB_QUESTIONS:
    print("EXCELLENT!")
elif nb_points == 0:
    print("Révisez vos maths!")
elif nb_points > moyenne:
    print("Pas mal")
else:
    print("Peu mieux faire")