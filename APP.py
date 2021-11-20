from flask import Flask, render_template, request



app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    liste_eq = get_equipement()
    return render_template('index.html', equipements = liste_eq)


    
