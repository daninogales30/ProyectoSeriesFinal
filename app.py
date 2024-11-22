from flask import Flask, request, render_template, url_for, redirect, session

app = Flask(__name__)
app.secret_key = "python_mejor_que_javascript"
usuarios = {
    "Dani": {
        "password": "12",
        "series": {
            "megustariaver": [],
            "estoyviendo": [],
            "hevisto": []
        }
    }
}


@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']
        if usuario in usuarios:
            error = "El nombre del usuario ya esta en uso, por favor, cambie su nombre"
            return render_template("registrar.html", error=error)
        usuarios[usuario] = {
            "password": password,
            "series": {
                "megustariaver": [],
                "estoyviendo": [],
                "hevisto": []
            }
        }
        return redirect(url_for("login"))
    return render_template("registrar.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']
        if usuario in usuarios and usuarios[usuario]["password"] == password:
            session['usuario'] = usuario
            return redirect(url_for("home"))
        error = "El nombre de usuario o la contraseña no son correctos"
        return render_template("login.html", error=error)

    return render_template("login.html")

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.route('/anadir_serie', methods=['GET', 'POST'])
def anadir_serie():
    if "usuario" not in session:
        return redirect(url_for("home"))
    usuario = session["usuario"]
    if request.method == "POST":
        nombre_serie = request.form['nombreSerie']
        sinopsis = request.form['sinopsiSerie']
        nota = request.form['notaSerie']
        genero = request.form['generoSerie']
        fecha = request.form['fechaSerie']
        n_temporadas = request.form['temporadaSerie']
        n_episodios = request.form['episodioSerie']
        categoria = request.form['categoria']

        nueva_serie = {
            "nombreSerie": nombre_serie,
            "sinopsis": sinopsis,
            "nota": nota,
            "genero": genero,
            "fecha": fecha,
            "n_temporadas": n_temporadas,
            "n_episodios": n_episodios,
        }

        usuarios[usuario]["series"][categoria].append(nueva_serie)

        return redirect(url_for("home"))
    return render_template("anadir_serie.html")


@app.route('/')
def home():
    if 'usuario' not in session:
        return redirect(url_for("registrar"))
    return render_template("home.html",
                           usuario=session["usuario"],
                           series_me_gustaria_ver=usuarios[session["usuario"]]["series"]["megustariaver"],
                           series_he_visto=usuarios[session["usuario"]]["series"]["hevisto"],
                           series_estoy_viendo=usuarios[session["usuario"]]["series"]["estoyviendo"])


if __name__ == '__main__':
    app.run()
