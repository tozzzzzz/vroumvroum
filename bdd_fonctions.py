# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 16:59:35 2021

@author: user
"""

import mysql.connector

def connection_BDD():
    mydb = mysql.connector.connect(
      host="idelont.fr",
      port="59435",
      user="rvoiture",
      password="!NtM$nQ52zT3",
      database="projet_irve",
      auth_plugin="mysql_native_password"
    )
    return mydb
    
### FONCTIONS POUR LES Voitures



def get_voitures():
    mydb = connection_BDD()
    
    mycursor = mydb.cursor()
    
    mycursor.execute("SELECT * FROM Voiture;")
    
    myresult = mycursor.fetchall()
    
    liste_eq = []
    for x in myresult:
      liste_eq.append(x)
    
    return liste_eq

