#importation des librairies utilisées
from numpy import empty
import requests
import sys
import webbrowser
import os
from typing import Optional
from fastapi import FastAPI
from shodan import Shodan
import shodan
import logging

#fichier log
logging.basicConfig(filename='tracebot.log', encoding='utf-8', level=logging.DEBUG)

class func_shodan:
    #attributs
    ip = ""
    hostname = ""
    urlMap = ""
    
    #constructeur
    def __init__(self,ip,hostname) -> None:
        self.ip = ip
        self.hostname = hostname


    #methode pour afficher la carte
    def afficheCarte(self,latitude,longitude):
        #definition de l'url en formatant la chaine de caractere dans urlMap en substituant notre chaine de caractere avec les donnes de latitude et longitude passés
        urlMap= "https://www.openstreetmap.org/?mlat={}&mlon={}#map=12".format(latitude,longitude)
        logging.info('url de la carte etabli')
        #utilisation de la lib webbrower en utilisant la methode open pour ouvrir la page web vers l'url
        #webbrowser.open(urlMap)
        self.urlMap = urlMap

    #methode pour la requete shodan    
    def serveur_shodan(self,apiKey):
        #utilisation de la methode host pour effectuer une recherche avec en parametre une ip on passe donc d'abord la cle api via la methode shodan
        
        api = shodan.Shodan(apiKey)
        logging.info('connexion a api shodan via apikey')
        
        try:
            location = api.host(self.ip)
            logging.info('recherche sur shodan avec ip')
            
            #verification du type dict donc json de reponse notre retour de la requete
            if isinstance(location, dict):
                #recuperation dans des variables pour les champs latitude et longitude
                latitude=location["latitude"]
                longitude=location["longitude"]
                #verification du type float pour nos deux variables
                if isinstance(latitude, float) and isinstance(longitude, float):
                    #appel de la methode afficheCarte avec en parametre notre latitude et longitude
                    self.afficheCarte(latitude,longitude)
                else:
                    logging.error('probleme de type valeur non float sur latitude et longitude')
            else:
                logging.error('probleme de type valeur non json sur le retour de la requete')
        
        except shodan.APIError:
            logging.error('Erreur sur la recherche via ip sur shodan')