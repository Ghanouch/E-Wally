# -*- coding: utf-8 -*-
"""
@author: E-Wall Group
"""

import sqlite3
import openhab
import datetime
import selectionBDD as DB


base_url = 'http://localhost:8080/rest'


# fetch all items
#items = openhab.fetch_all_items(base_url)


#--------------------------------------get Sentiment from OpenHub
print('GET SENTIMENT ...')
sentiment = openhab.get_item(base_url, 'emotion_item')
#sentiment.state = 'Suprised'
#Happy  Sad  Suprised  Neutral  Angry
#--------------------------------------get dependances of configurations from Sqlite ( )
print('GET DEPENDANCES FROM DATABASE ...')

#Connection Database 
conn = sqlite3.connect('/home/amine/projets/Emotions_project/Dependances/db/WALL-E-Motion.db')

#get Properties and Animation 
properties=DB.getProperties(conn,sentiment.state)[0]
animation =DB.getAnimation(conn,sentiment.state)[0]


property_color=properties[0]
property_frequence=properties[1]
property_intensite=properties[2]
property_texte=properties[3]
property_secondaryColor=properties[4]
property_listColor=properties[5]

animation_id=animation[0] 
animation_nom=animation[1]
animation_lien=animation[2]
animation_frequence=animation[3]
animation_intensite=animation[4]

#print('PROPERTIES',property_color, property_frequence, property_intensite, property_secondaryColor, property_listColor)
#print('ANIMATION ', animation_id, animation_nom, animation_lien, animation_frequence, animation_intensite)

#Close Database 
conn.close()


#------------------------------Change the items configuration on OpenHub
print('SET THE CONFIGURATION ON OpenHub...')

# ------  Set the Brightness 

plafond_intensite = openhab.get_item(base_url, 'plafond_intensite')
constellation_intensite = openhab.get_item(base_url, 'constellation_intensite')

bande_basse_N_intensite = openhab.get_item(base_url, 'bande_basse_N_intensite') 
bande_basse_S_intensite = openhab.get_item(base_url, 'bande_basse_S_intensite')
bande_basse_E_intensite = openhab.get_item(base_url, 'bande_basse_E_intensite')
bande_basse_W_intensite = openhab.get_item(base_url, 'bande_basse_W_intensite')

bande_haute_N_intensite = openhab.get_item(base_url, 'bande_haute_N_intensite')
bande_haute_S_intensite = openhab.get_item(base_url, 'bande_haute_S_intensite')
bande_haute_E_intensite = openhab.get_item(base_url, 'bande_haute_E_intensite')
bande_haute_W_intensite = openhab.get_item(base_url, 'bande_haute_W_intensite')

plafond_intensite.state = property_intensite
constellation_intensite.state= property_intensite
bande_basse_N_intensite.state= property_intensite
bande_basse_S_intensite.state= property_intensite
bande_basse_E_intensite.state= property_intensite
bande_basse_W_intensite.state= property_intensite
bande_haute_N_intensite.state= property_intensite
bande_haute_S_intensite.state= property_intensite
bande_haute_E_intensite.state= property_intensite
bande_haute_W_intensite.state= property_intensite


# ------  Set the Frequence

plafond_frequence       = openhab.get_item(base_url, 'plafond_frequence')
constellation_frequence = openhab.get_item(base_url, 'constellation_frequence')

bande_basse_N_frequence = openhab.get_item(base_url, 'bande_basse_N_frequence')
bande_basse_S_frequence = openhab.get_item(base_url, 'bande_basse_S_frequence')
bande_basse_E_frequence = openhab.get_item(base_url, 'bande_basse_E_frequence')
bande_basse_W_frequence = openhab.get_item(base_url, 'bande_basse_W_frequence')

bande_haute_N_frequence = openhab.get_item(base_url, 'bande_haute_N_frequence')
bande_haute_S_frequence = openhab.get_item(base_url, 'bande_haute_S_frequence')
bande_haute_E_frequence = openhab.get_item(base_url, 'bande_haute_E_frequence')
bande_haute_W_frequence = openhab.get_item(base_url, 'bande_haute_W_frequence')

plafond_frequence.state = int(property_frequence) 
constellation_frequence.state = int(property_frequence)
bande_basse_N_frequence.state = int(property_frequence)
bande_basse_S_frequence.state = int(property_frequence)
bande_basse_E_frequence.state = int(property_frequence)
bande_basse_W_frequence.state = int(property_frequence)
bande_haute_N_frequence.state = int(property_frequence)
bande_haute_S_frequence.state = int(property_frequence)
bande_haute_E_frequence.state = int(property_frequence)
bande_haute_W_frequence.state = int(property_frequence)


#------ set the list of colors 


plafond_couleurs  	   = openhab.get_item(base_url, 'plafond_couleurs')	
constellation_couleurs = openhab.get_item(base_url, 'constellation_couleurs')

bande_basse_N_couleurs = openhab.get_item(base_url, 'bande_basse_N_couleurs')
bande_basse_S_couleurs = openhab.get_item(base_url, 'bande_basse_S_couleurs')
bande_basse_E_couleurs = openhab.get_item(base_url, 'bande_basse_E_couleurs')
bande_basse_W_couleurs = openhab.get_item(base_url, 'bande_basse_W_couleurs')

bande_haute_N_couleurs = openhab.get_item(base_url, 'bande_haute_N_couleurs')
bande_haute_S_couleurs = openhab.get_item(base_url, 'bande_haute_S_couleurs')
bande_haute_E_couleurs = openhab.get_item(base_url, 'bande_haute_E_couleurs')
bande_haute_W_couleurs = openhab.get_item(base_url, 'bande_haute_W_couleurs')

plafond_couleurs.state = property_listColor
constellation_couleurs.state = property_listColor
bande_basse_N_couleurs.state = property_listColor
bande_basse_S_couleurs.state = property_listColor
bande_basse_E_couleurs.state = property_listColor
bande_basse_W_couleurs.state = property_listColor
bande_haute_N_couleurs.state = property_listColor
bande_haute_S_couleurs.state = property_listColor
bande_haute_E_couleurs.state = property_listColor
bande_haute_W_couleurs.state = property_listColor

#------ Set the Main Principal Color  

plafond_couleur       =  openhab.get_item(base_url, 'plafond_couleur') 
constellation_couleur =  openhab.get_item(base_url, 'constellation_couleur')

bande_basse_N_couleur =  openhab.get_item(base_url, 'bande_basse_N_couleur')
bande_basse_S_couleur =  openhab.get_item(base_url, 'bande_basse_S_couleur')
bande_basse_E_couleur =  openhab.get_item(base_url, 'bande_basse_E_couleur')
bande_basse_W_couleur =  openhab.get_item(base_url, 'bande_basse_W_couleur')

bande_haute_N_couleur =  openhab.get_item(base_url, 'bande_haute_N_couleur')
bande_haute_S_couleur =  openhab.get_item(base_url, 'bande_haute_S_couleur')
bande_haute_E_couleur =  openhab.get_item(base_url, 'bande_haute_E_couleur')
bande_haute_W_couleur =  openhab.get_item(base_url, 'bande_haute_W_couleur')

plafond_couleur.state = property_color
constellation_couleur.state = property_color
bande_basse_N_couleur.state = property_color
bande_basse_S_couleur.state = property_color
bande_basse_E_couleur.state = property_color
bande_basse_W_couleur.state = property_color
bande_haute_N_couleur.state = property_color
bande_haute_S_couleur.state = property_color
bande_haute_E_couleur.state = property_color
bande_haute_W_couleur.state = property_color


#------ Set the Secondary Color  

plafond_couleur_second       =  openhab.get_item(base_url, 'plafond_couleur_second') 
constellation_couleur_second =  openhab.get_item(base_url, 'constellation_couleur_second')

bande_basse_N_couleur_second =  openhab.get_item(base_url, 'bande_basse_N_couleur_second')
bande_basse_S_couleur_second =  openhab.get_item(base_url, 'bande_basse_S_couleur_second')
bande_basse_E_couleur_second =  openhab.get_item(base_url, 'bande_basse_E_couleur_second')
bande_basse_W_couleur_second =  openhab.get_item(base_url, 'bande_basse_W_couleur_second')

bande_haute_N_couleur_second =  openhab.get_item(base_url, 'bande_haute_N_couleur_second')
bande_haute_S_couleur_second =  openhab.get_item(base_url, 'bande_haute_S_couleur_second')
bande_haute_E_couleur_second =  openhab.get_item(base_url, 'bande_haute_E_couleur_second')
bande_haute_W_couleur_second =  openhab.get_item(base_url, 'bande_haute_W_couleur_second')

plafond_couleur_second.state = property_secondaryColor
constellation_couleur_second.state = property_secondaryColor
bande_basse_N_couleur_second.state = property_secondaryColor
bande_basse_S_couleur_second.state = property_secondaryColor
bande_basse_E_couleur_second.state = property_secondaryColor
bande_basse_W_couleur_second.state = property_secondaryColor
bande_haute_N_couleur_second.state = property_secondaryColor
bande_haute_S_couleur_second.state = property_secondaryColor
bande_haute_E_couleur_second.state = property_secondaryColor
bande_haute_W_couleur_second.state = property_secondaryColor


#------ Set the SConfiguration of The Animation 

plafond_animation	   =openhab.get_item(base_url, 'plafond_animation') 
constellation_animation=openhab.get_item(base_url, 'constellation_animation') 

bande_basse_N_animation=openhab.get_item(base_url, 'bande_basse_N_animation') 
bande_basse_S_animation=openhab.get_item(base_url, 'bande_basse_S_animation') 
bande_basse_E_animation=openhab.get_item(base_url, 'bande_basse_E_animation') 
bande_basse_W_animation=openhab.get_item(base_url, 'bande_basse_W_animation') 

bande_haute_N_animation=openhab.get_item(base_url, 'bande_haute_N_animation') 
bande_haute_S_animation=openhab.get_item(base_url, 'bande_haute_S_animation')
bande_haute_E_animation=openhab.get_item(base_url, 'bande_haute_E_animation') 
bande_haute_W_animation=openhab.get_item(base_url, 'bande_haute_W_animation') 

plafond_animation.state = animation_id
constellation_animation.state = animation_id
bande_basse_N_animation.state = animation_id
bande_basse_S_animation.state = animation_id
bande_basse_E_animation.state = animation_id
bande_basse_W_animation.state = animation_id
bande_haute_N_animation.state = animation_id
bande_haute_S_animation.state = animation_id
bande_haute_E_animation.state = animation_id
bande_haute_W_animation.state = animation_id


print('FIN JOB  ')
