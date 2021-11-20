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
    app1 =App()
    Ville1=app1.trouverCoordonéeVille(result['adresse_1'])
    Ville2=app1.trouverCoordonéeVille(result['adresse_2'])
    print(Ville1)
    print(Ville2)
    distance=app1.get_distance(Ville1[0], Ville1[1], Ville2[0], Ville2[1])
    print(distance)
    print(result['Autonomie'])
    nbr=app1.nbrstop(distance,int(result['Autonomie']))
    print(nbr)
    return render_template('affichage.html', voiture = result)




if __name__ == "__main__":
    app.run(debug=True)   
