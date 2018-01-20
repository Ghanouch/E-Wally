import openhab
import colorsys

#Import colorsys bt type :  python3 >> import colorsys 
#https://docs.python.org/2/library/colorsys.html


def convert_hls_to_rgb(hls):
	h, l, s= hls.split(',')
	rgb= colorsys.hls_to_rgb(round(float(h))/360.0,round(float(l))/100.,round(float(s))/100.)
	return rgb

base_url = 'http://localhost:8080/rest'	

#---------------  GET THE COLOR 

#get the Item color from OpenHab
plafond_couleur =  openhab.get_item(base_url, 'plafond_couleur') 
#get the Color HLS
HLS = plafond_couleur.state
#COnvert Hls to RGB Triplet
RGB = convert_hls_to_rgb(plafond_couleur.state)


#Convert from % to Value
R = int(RGB[0]*255)
G = int(RGB[1]*255)
B = int(RGB[2]*255)


print('RGB : ( ',R, ' --  ' , G, ' -- ', B,' )')


#--------------- GET THE FREQUENCE 

Propertie_frequence = openhab.get_item(base_url, 'plafond_frequence')
valeur_frequence    = Propertie_frequence.state

# ------  Set the Brightness 
plafond_intensite = openhab.get_item(base_url, 'plafond_intensite')


#------ set the list of colors 
plafond_couleurs  	   = openhab.get_item(base_url, 'plafond_couleurs')	


#------ Set the Secondary Color  
plafond_couleur_second       =  openhab.get_item(base_url, 'plafond_couleur_second') 


