from flask import Flask, render_template
app = Flask("brejao")

@app.route("/")
def hello():
    return render_template("index.html")

@app.route('/contato')
def contato():
    return render_template("contato.html")

@app.route("/estrutura")
def estrutura():
    return render_template("estrutura.html")

@app.route("/galeria")
def galeria():
    return render_template("galeria.html")

@app.route("/historia")
def historia():
    return render_template("historia.html")

@app.route("/moradores/")
def moradores():
    return render_template("moradores.html")

if __name__ == "__main__":
    app.run(debug=True)
