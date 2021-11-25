# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 10:51:05 2021

@author: Boisced
"""

import requests
import math

from zeep import Client





class App():
	def __init__(self):
		pass
	
	
	
	def BorneElec(self,X,Y,R,N):
		
		
		listeBorne=[]
		T=0
		
		
		URL = "https://opendata.reseaux-energies.fr/api/records/1.0/search/?dataset=bornes-irve&q=&rows="+str(N)+"&geofilter.distance="+str(X)+"%2C"+str(Y)+"%2C"+str(R)


		r = requests.get(url = URL)
		
		data = r.json()
		
		for i in data['records']:
			bornes=[]
			
			bornes.append(T)
			bornes.append(i['recordid'])
			bornes.append(i['fields']['ylatitude'])
			bornes.append(i['fields']['xlongitude'])
			bornes.append(i['fields']['acces_recharge'])
			listeBorne.append(bornes)
			T=T+1
		
		return listeBorne

	def calculeTrajet(self,ville1,ville2):
		None
		
		
	def trouverCoordonéeVille(self,ville):
		adresse=[]
	
		
		
		URL = "https://nominatim.openstreetmap.org/search?q="+str(ville)+"&format=json&polygon_geojson=1&addressdetails=1"


		r = requests.get(url = URL)
		
		donnee = r.json()
		adresse.append(donnee[0]['lat'])
		adresse.append(donnee[0]['lon'])
			
		return adresse
	
	
	def get_distance(self,Xville1,Yville1,Xville2,Yville2):
	
		wsdl = 'http://127.0.0.1:8000/?wsdl'
		client = Client(wsdl=wsdl)

		return client.service.get_distance(Xville1,Yville1,Xville2,Yville2)
		
	def get_time(self,distance, vitesse):
		return float(distance) / vitesse

	def nbrstop(self,distance, autonomie):
		nbr = float(distance) / int(autonomie)
		if nbr < 1:
			return 0
		else:
			return math.ceil(nbr)

	def borne(self,):
		None


	def calcule_coord(self,Ville1_1, Ville1_2, Ville2_1, Ville2_2,nbr):
		total = []
		dest = []
    
		if nbr < 1:
			total =[]
			return total
		else:
			v_lat = (float(Ville2_1) - float(Ville1_1)) / nbr
			v_lng = (float(Ville2_2) - float(Ville1_2)) / nbr
            
			dest_lat = float(Ville1_1)
			dest_lng = float(Ville1_2)
            
			for i in range(nbr-1):
				dest_lat = dest_lat + float(v_lat)
				dest_lng = dest_lng + float(v_lng)
				dest.append(dest_lat)
				dest.append(dest_lng)
				total.append(dest)
				dest =[]
			return total
	

	def trouveborne(self,point):
		borne=[]
		for i in point:
			borne.append(self.BorneElec(i[0],i[1],600000,1))
		return borne





	
    
   
    
        
		





