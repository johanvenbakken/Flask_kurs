# Importerer Flask-klassen fra flask-biblioteket.
from flask import Flask

# Lager en ny instans av Flask-applikasjonen.
# __name__ er en spesiell variabel som representerer navnet på den nåværende modulen.
# Flask bruker dette til å vite hvor den skal lete etter ressurser som HTML-filer.
app = Flask(__name__)

# Definerer en rute for hjemmesiden ('/').
@app.route('/')
def home():
    # Returnerer teksten "Hello World!" som vil vises i nettleseren.
    return "Hello World!"

# Dette sjekker om skriptet kjøres direkte (ikke importeres som modul).
# Hvis det kjøres direkte, starter Flask-applikasjonen med debug-modus aktivert.
# Debug-modus gjør det lettere å utvikle ved å automatisk laste siden på nytt ved endringer
if __name__ == '__main__':
    app.run(debug=True)