# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 10:51:05 2021

@author: Boisced
"""

import requests


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
	
	
	def get_distance2(self,Xville1,Yville1,Xville2,Yville2):
	
		wsdl = 'http://127.0.0.1:8000/?wsdl'
		client = Client(wsdl=wsdl)

		return client.service.get_distance(Xville1,Yville1,Xville2,Yville2)
		
	def get_time(self,distance, vitesse):
		return float(distance) / vitesse
	
    
   
    
        
		

app1 =App()

x=48.8520930694
y=2.34738897685
r=1000
n=1

print(app1.BorneElec(x,y,r,n))

Ville1=app1.trouverCoordonéeVille("Marignier")
Ville2=app1.trouverCoordonéeVille("Paris")
print(Ville1)
print(Ville2)

print("avant")
a=app1.get_distance2(Ville1[0], Ville1[1], Ville2[0], Ville2[1])
print("la distance est ",a)
print(a)
print("la vitesse est "+str(app1.get_time(a,130)))
print("apres")




