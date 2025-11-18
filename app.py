from flask import Flask, render_template, request
import requests


app = Flask(__name__)


API_KEY = "udJqwbKLuDZTGgIEmmOlAre5tV47sjQ5ichJxxQO"

tipos = {
"Branded": "Producto de marca comercial",
"Survey (FNDDS)": "Alimento de encuesta nacional",
"Foundation": "Alimento base (datos detallados)",
"SR Legacy": "Base de datos antigua del USDA",
"Sample": "Muestra analizada en laboratorio"
}


@app.route("/", methods=["GET", "POST"])
def index():
    alimentos = []
    query = ""
    if request.method == "POST":
        query = request.form["query"]
        url = f"https://api.nal.usda.gov/fdc/v1/foods/search?query={query}&api_key={API_KEY}"
        response = requests.get(url)


        if response.status_code == 200:
            data = response.json()
            alimentos = data.get("foods", [])
        else:
            alimentos = []


    return render_template("index.html", alimentos=alimentos, query=query, tipos=tipos)




@app.route("/detalle/<int:fdc_id>")
def detalle(fdc_id):
    url = f"https://api.nal.usda.gov/fdc/v1/food/{fdc_id}?api_key={API_KEY}"
    response = requests.get(url)


    if response.status_code == 200:
        data = response.json()
    else:
        data = None


    return render_template("detalle.html", alimento=data)




if __name__ == "__main__":
    app.run(debug=True)(debug=True)