import time

def Horloge():
#Déclaration des variable avec les inputs pour le temps, en spécifiant que ce sont des nombres entiers
        heure = int(input("Choissisez une heure de départ:"))
        min = int(input("choissisez minute:"))
        seconde = int(input("Choissisez secondes"))
        while(True):
#Boucle infinie pour pouvoir rajouter du temps                
#La propriété time sleep permet de faire passer des secondes dans ma boucle,les conditions sont la pour vérifier si le chrono devrait s'arrêter
#Si ils s'arrêtent, alors remettre le chrono a zero et rajouter 1 à la valeur suivante donc, seconde = min = heure, ainsi de suite
#Ensuite on affichent le résultats et on formate  pour que la longueur s'arrête à 2 chiffres, par défaut 0
                time.sleep(1)
                if(seconde == 60):
                        seconde = 0
                        min+=1
                if(min == 60):
                        min=0
                        heure+=1
                if(heure == 24):
                        heure = 0
                        print("félicitation")
                seconde+=1
                print("{:0>2}:{:0>2}:{:0>2}".format(heure,min,seconde))

Horloge()