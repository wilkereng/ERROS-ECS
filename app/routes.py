from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    dados = {"sistema": "ECS", "empresa": "Saneago"}
    return render_template('index.html', dados=dados)


@app.route('/analises')
def analises():
    return render_template('analises.html')
