from flask import Flask,render_template
from flask import request
from flask import flash, redirect, url_for
import time
from pytest import main
from TuclaseExamen import TuclaseExamen

app=Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/",methods=["GET"])
def home():
    return render_template("FormExam.html")

@app.route("/resultado",methods=["POST"])
def resultado():
    cadena = request.form.get("txtCadena")
    lista = cadena.split(",")
    obj=TuclaseExamen()
    cadena1=obj.arithmetic_arranger(lista, True)
    return render_template("resultado.html",cadena=cadena1)

if __name__ == "__main__":
    app.run(debug=True,port=3000)