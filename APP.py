# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 16:59:35 2021

@author: Boisced
"""



from flask import Flask, render_template, request
from bdd_fonctions import *
from Fonction import *


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    voitures = get_voitures()
    return render_template('index.html', voitures = voitures)

@app.route('/choisir', methods=['POST'])
def choisir():
    result = request.form
    return render_template('choisir.html', voiture = result)

@app.route('/affichage', methods=['POST'])
def affichage():
    result = request.form
    print(result)
    app1 =App(result['adresse_1'],result['adresse_2'],result['Autonomie'],result['Charge'])
    trajet =app1.get_add_trajet()
    duree=app1.get_temps()
    print(trajet)
    print(duree)
    return render_template('affichage.html', voiture = result,trajets=trajet,time=duree)




if __name__ == "__main__":
    app.run(debug=True)   
