from traceback import print_tb
from click import launch
import discord
import logging
from func_shodan import func_shodan
from func_syracuse import func_syracuse
from func_multegypt import func_multegypt
from argparse import ArgumentParser, Namespace
import json

#fichier log
logging.basicConfig(filename='tracebot.log', encoding='utf-8', level=logging.DEBUG)

#creation d'un client discord
client = discord.Client()

#parse pour recuper le nom du fichier de configuration JSON en parametre
def parse_args() -> Namespace:
        parser = ArgumentParser()
        parser.add_argument(
            "-c", "--config", help="Config file", required=True, dest="config"
        )
        return parser.parse_args()

#parse
args = parse_args()
#chargement dans data des donnes JSON
with open(args.config) as json_data_file:
    data = json.load(json_data_file)
logging.info('Parse sur le fichier de configuration JSON')

class MyBot:

    #methode event du bot discord connexion
    @client.event
    async def on_ready():
        channel = client.get_channel(986278767473336373)
        await channel.send("BoBOT is connected ! Tape **!help** for more informations")
        logging.info('BOT is connected')
    
    #methode event du bot discord message
    @client.event
    async def on_message(message):
        #commande !iplocation
        if message.content.startswith('!iplocation'):
            logging.info('Traitement de la commande !iplocation')
            #split pour separer les parametres passes
            response = message.content.split(" ")
            if len(response) > 3:
                logging.error('Nombre de parametre passé superieur a 3')
                await message.channel.send("Vous avez saisi trop de parametre, il faut une ip et un hostname")
            if len(response) < 3:
                logging.error('Nombre de parametre passé inferieur a 3')
                await message.channel.send("Il manque un ou des parametres, il faut une ip et un hostname")
            else:
                if isinstance(response[1], int) or isinstance(response[1], float) or isinstance(response[2], int) or isinstance(response[2], float):
                    logging.error('Parametre passé est/sont des entiers ou des floats')
                    await message.channel.send("Vous avez saisi des valeurs numeriques, il faut une ip et un hostname")
                else:
                    logging.info('Traitement de la requete shodan')
                    #creation d'un objet func_shodan
                    shodan = func_shodan(response[1],response[2])
                    #appel de la methode pour requeter shodan
                    shodan.serveur_shodan(data['apiKey'])
                    #message sur le channel de l'url
                    await message.channel.send(shodan.urlMap)
                    logging.info('Traitement de la commande !iplocation terminé')
        
        #commande !syracuse    
        if message.content.startswith('!syracuse'):
            logging.info('Traitement de la commande !syracuse')
            #split pour separer les parametres passes
            response = message.content.split(" ")
            if len(response) > 2:
                logging.error('Nombre de parametre passé superieur a 2')
                await message.channel.send("Vous avez saisi trop de parametre, il faut un entier")
            if len(response) < 2:
                logging.error('Nombre de parametre passé inferieur a 2')
                await message.channel.send("Il manque un parametre, il faut un entier")
            else:
                if isinstance(response[1], str):
                    logging.error('Parametre passé est une chaine de caractere')
                    await message.channel.send("Vous avez saisi une chaine de caractere, il faut un entier")
                else:
                    logging.info('Traitement de la conjecture de syracuse')
                    #creation d'un objet func_syracuse
                    syracuse = func_syracuse(response[1])
                    #appel de la methode de conjecture qui retourne le resultat dans la methode pour envoyer un message
                    await message.channel.send(syracuse.conjecture_syracuse())
                    logging.info('Traitement de la conjecture de syracuse terminé')
        
        #commande !multegypt  
        if message.content.startswith('!multegypt'):
            logging.info('Traitement de la commande !multegypt')
            #split pour separer les parametres passes
            response = message.content.split(" ")
            if len(response) > 3:
                logging.error('Nombre de parametre passé superieur a 3')
                await message.channel.send("Vous avez saisi trop de parametre, il faut deux entiers")
            if len(response) < 3:
                logging.error('Nombre de parametre passé inferieur a 3')
                await message.channel.send("Il manque un ou des parametres, il faut deux entiers")
            else:
                if isinstance(response[1], str) or isinstance(response[2], str):
                    logging.error('Parametre passé est/sont des chaine de caractere')
                    await message.channel.send("Vous avez saisi des chaine de caractere, il faut deux entiers")
                else:
                    logging.info('Traitement de la multiplication egyptienne')
                    #creation d'un objet func_egypt
                    multegypt = func_multegypt(response[1],response[2])
                    #appel de la methode multiplication egyptienne qui retourne le resultat dans la methode pour envoyer un message
                    await message.channel.send(multegypt.multiplication_egyptienne())
                    logging.info('Traitement de la multiplication egyptienne terminé')
        
        #commande !help  
        if message.content.startswith('!help'):
            logging.info('Traitement de la commande !help')
            await message.channel.send("Bonjour je suis BoBOT, \n Voici mes fonctionnalitées : \n **!iplocation <ip> <hostname>** , pour localiser un adresse IP sur OpenStreetMap \n **!syracuse <int>** , pour calculer une suite de syracuse sur un entier \n **!multegypt <int> <int>** , pour calculer la multiplication egyptienne deux entiers")

    #pour demarer le bot
    def launch(self):
        client.run(data['botToken'])
        logging.info('Lancement du BOT')
    

#main
if __name__ == "__main__":
    #creation d'un objet bot
    bot = MyBot()
    #lancement du bot avec methode launch
    bot.launch()