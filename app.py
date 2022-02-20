import requests
from flask import Flask, render_template


app = Flask (__name__)

#API de msg motivacional/rota index do site 
@app.route("/")
def index ():
    busca = requests.get('https://api.adviceslip.com/advice')
    resul = busca.json()
    resultado = resul['slip']['advice']
    return render_template('index.html', msg = resultado)






