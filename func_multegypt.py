import logging

#fichier log
logging.basicConfig(filename='tracebot.log', encoding='utf-8', level=logging.DEBUG)

class func_multegypt:
    #attributs
    int1 = 0
    int2 = 0
    
    #constructeur
    def __init__(self,a,b) -> None:
        #cast en entier
        self.int1 = int(a)
        self.int2 = int(b)
    
    def multiplication_egyptienne(self):
        logging.info('processus du calcul de la multiplication egyptienne')
        #init de la variable resultat
        resultat=0
        #on cree des variable qui vont contenir les valeurs passes par l'utilisateur
        nb1 = self.int1
        nb2 = self.int2
        #tant que le premier nombre est different de 0 on procede aux calculs
        while(nb1 != 0):
            #si le premier nombre est impair
            if(nb1 % 2 == 1):
                #le resultat s'incremente de la valeur nb2, du deuxieme nombre
                resultat += nb2
            #on multiplie nb2 par 2
            nb2*=2
            #et nb1 est egale a la valeur arrondi de sa division par 2
            nb1 = round(nb1/2)
        #on retourne le resultat
        return resultat
    