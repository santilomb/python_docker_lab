from flask import Flask
import os
import socket

# Connect to Redis

app = Flask(__name__)

@app.route("/")
def hello():
    texto = "<i>prueba de apps python3 container</i>"

    html = "<h3>Hola {name}!</h3>" \
           "<b>Te estamos atendiendo desde:</b> {hostname}<br/>" \
           "<b>Var:</b> {texto}"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), texto=texto)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
