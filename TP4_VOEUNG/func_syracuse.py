import logging

#fichier log
logging.basicConfig(filename='tracebot.log', encoding='utf-8', level=logging.DEBUG)

class func_syracuse:
    #attributs
    intSyracuse = 0
    
    #constructeur
    def __init__(self,intsyr) -> None:
        #cast en entier
        self.intSyracuse = int(intsyr)
        
    def conjecture_syracuse(self):
        logging.info('processus du calcul de la conjecture de syracuse')
        #on cree une variable nb qui va contenir la valeur passe par l'utilisateur
        nb = self.intSyracuse
        #tant que le resultat n'est pas egale a 1 on procede aux calculs de l'algo
        while nb != 1:
            #si le nb est pair
            if nb % 2 == 0:
                #on le divise par 2
                nb = nb//2
            else:
                #sinon on le multiplie par 3 et on ajoute 1
                nb = nb*3+1
        #on retourne le resultat final
        return nb