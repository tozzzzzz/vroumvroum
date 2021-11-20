# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 16:59:35 2021

@author: user
"""

import mysql.connector

def connection_BDD():
    mydb = mysql.connector.connect(
      host="192.168.141.251",
      user="dev",
      password="Adm1n/BCCB",
      database="POC_SUPERVISION",
      auth_plugin="mysql_native_password"
    )
    return mydb
    
### FONCTIONS POUR LES EQUIPEMENTS

def add_equipement(name, ip_addr, description, modele, supervision,communaute):
    mydb = connection_BDD()
    
    mycursor = mydb.cursor()
    mycursor.execute("""INSERT INTO Equipements(nom, adresse_ip, id_modele,etat_supervision, communaute) VALUES (%s, %s, %s, %s, %s)""",(name, ip_addr, modele, supervision, communaute))
    mydb.commit()
    return 1

def get_equipement():
    mydb = connection_BDD()
    
    mycursor = mydb.cursor()
    
    mycursor.execute("SELECT * FROM Equipements;")
    
    myresult = mycursor.fetchall()
    
    liste_eq = []
    for x in myresult:
      liste_eq.append(x)
    
    return liste_eq

def del_equipement(id):
    mydb = connection_BDD()
    
    mycursor = mydb.cursor()
    mycursor.execute("""DELETE FROM Equipements WHERE id="""+id+""";""")
    mydb.commit()
    return 1


def mod_equipement(champ, valeure, id_eq):
    mydb = connection_BDD()
    
    mycursor = mydb.cursor()
    mycursor.execute("""UPDATE Equipements SET %s = %s WHERE id = %s""",(champ,valeure,id_eq))
    #mycursor.execute("""UPDATE Equipements SET """+champ+""" = """+valeure+""" WHERE id = """+id_eq+"""""")
    mydb.commit()
    return 1
### FONCTIONS POUR LES REQUETES


def add_requete(name_rqt,oid):
    mydb = connection_BDD()
    
    mycursor = mydb.cursor()
    #mycursor.execute("INSERT INTO Requete(nom, MIB) VALUES ( "+name_rqt+","+oid+")")

    mycursor.execute("""INSERT INTO Requetes(nom, MIB) VALUES (%s, %s)""",(name_rqt, oid))
    mydb.commit()
    
    return 1

def get_requete():
    mydb = connection_BDD()
    
    mycursor = mydb.cursor()
    
    mycursor.execute("SELECT * FROM Requetes;")
    
    myresult = mycursor.fetchall()
    
    liste_rqt = []
    for x in myresult:
      liste_rqt.append(x)
    
    return liste_rqt
def del_requete(id):
    mydb = connection_BDD()
    
    mycursor = mydb.cursor()
    mycursor.execute("""DELETE FROM Requetes WHERE id="""+id+""";""")
    mydb.commit()
    return 1
 
def get_myrequete(id_rqt):
    mydb = connection_BDD()
    
    mycursor = mydb.cursor()

    mycursor.execute("""SELECT * FROM Requetes WHERE id ="""+id_rqt+""";""")
    myinfo = mycursor.fetchall()
    liste_requetes_mdl = []
    for asso in myinfo:
        liste_requetes_mdl.append(asso)
        
    return liste_requetes_mdl

### FONCTIONS BDD POUR LES MODELES

def add_modele(name_mdl):
    mydb = connection_BDD()
    
    mycursor = mydb.cursor()

    mycursor.execute("""INSERT INTO Modeles(nom) VALUES ('"""+name_mdl+"""')""")
    mydb.commit()
    
    return 1

def get_modele():
    mydb = connection_BDD()
    
    mycursor = mydb.cursor()
    
    mycursor.execute("SELECT * FROM Modeles;")
    
    myresult = mycursor.fetchall()
    
    liste_mdl = []
    for x in myresult:
      liste_mdl.append(x)
    
    return liste_mdl

def info_du_modele(id_mdl):
    mydb = connection_BDD()
    
    mycursor = mydb.cursor()

    mycursor.execute("""SELECT * FROM Modeles WHERE id="""+id_mdl+""";""")
    myinfo = mycursor.fetchall()
    
    liste_info_modele = []
    for inf in myinfo:
        liste_info_modele.append(inf)
        
    return liste_info_modele

### FONCTIONS BDD POUR LA TABLE DE JOINTURE MODELE REQUETE

def get_association(id_mdl):
    mydb = connection_BDD()
    
    mycursor = mydb.cursor()

    mycursor.execute("""SELECT id_rqt FROM Jointure_modele_requete WHERE id_modele ="""+id_mdl+""";""")
    myinfo = mycursor.fetchall()
    
    liste_association_mdl = []
    for asso in myinfo:
        liste_association_mdl.append(asso)
        
    return liste_association_mdl

def get_jointure():
    mydb = connection_BDD()
    
    mycursor = mydb.cursor()

    mycursor.execute("""SELECT * FROM Jointure_modele_requete;""")
    myinfo = mycursor.fetchall()
    
    liste_association_mdl = []
    for asso in myinfo:
        liste_association_mdl.append(asso)
        
    return liste_association_mdl

def association_modele_requete(id_mdl, id_rqt):
    mydb = connection_BDD()
    
    mycursor = mydb.cursor()

    mycursor.execute("""INSERT INTO Jointure_modele_requete(id_rqt, id_modele) VALUES(%s,%s)""",(id_rqt,id_mdl))
    mydb.commit()
    
    return 1

### FONCTIONS BDD POUR LES DONNEES SNMP

def add_data(id_equipement, date, heure, nom_rqt, value):
    mydb = connection_BDD()
    
    mycursor = mydb.cursor()

    mycursor.execute("""INSERT INTO Data(id_equipement, date, temps, requete, valeur) VALUES (%s,%s,%s,%s,%s)""",(id_equipement,date,heure,nom_rqt,value))
    mydb.commit()
    
    return 1