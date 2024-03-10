import numpy as np
import sys

NbrTour = 0
Tableau = np.array([[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]])

def Afficher(tab):
    print("-------")
    for i in range(0,3):
        for j in range(0,3):
            if j == 0:
                print("|", end='')
            print(tab[i, j], end='')
            print("|", end='')
        print()
        print("-------")

def jouer(Chiffre):
    
    global NbrTour

    if Chiffre == 1:
        x = 2
        y = 0
    elif Chiffre == 2:
        x = 2
        y = 1
    elif Chiffre == 3:
        x = 2
        y = 2
    elif Chiffre == 4:
        x = 1
        y = 0
    elif Chiffre == 5:
        x = 1
        y = 1
    elif Chiffre == 6:
        x = 1
        y = 2
    elif Chiffre == 7:
        x = 0
        y = 0
    elif Chiffre == 8:
        x = 0
        y = 1
    elif Chiffre == 9:
        x = 0
        y = 2

    if NbrTour % 2 == 0:
        Symb = "x"
    else:
        Symb = "o"

    if(Tableau[x, y] == " "):
        Tableau[x, y] = Symb
        NbrTour += 1

    else:
        print("Déjà Joué")

def testVic():
    
    if (Tableau[0, 0] != " " and Tableau[0, 0] == Tableau[0, 1] and Tableau[0, 1] == Tableau[0, 2]) or\
       (Tableau[1, 0] != " " and Tableau[1, 0] == Tableau[1, 1] and Tableau[1, 1] == Tableau[1, 2]) or\
       (Tableau[2, 0] != " " and Tableau[2, 0] == Tableau[2, 1] and Tableau[2, 1] == Tableau[2, 2]):
       
        print("Gagné")
        Afficher(Tableau)
        sys.exit()
     
    elif (Tableau[0, 0] != " " and Tableau[0, 0] == Tableau[1, 0] and Tableau[1, 0] == Tableau[2, 0]) or\
         (Tableau[0, 1] != " " and Tableau[0, 1] == Tableau[1, 1] and Tableau[1, 1] == Tableau[2, 1])or\
         (Tableau[0, 2] != " " and Tableau[0, 2] == Tableau[1, 2] and Tableau[1, 2] == Tableau[2, 2]):
        
        print("Gagné")
        Afficher(Tableau)
        sys.exit()
    
    elif (Tableau[0, 0] != " " and Tableau[0, 0] == Tableau[1, 1] and Tableau[1, 1] == Tableau[2, 2])or\
         (Tableau[0, 2] != " " and Tableau[0, 2] == Tableau[1, 1] and Tableau[1, 1] == Tableau[2, 0]):
        
        print("Gagné")
        Afficher(Tableau)
        sys.exit()
    
def main():
    while True:
        Afficher(Tableau)
        jouer(int(input("Choisi une case : ")))
        testVic()

if __name__ == "__main__":
    main()