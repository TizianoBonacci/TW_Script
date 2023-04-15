from flask import Flask, request, jsonify
# ... (includi tutte le altre importazioni qui)
from flask import Flask, request, jsonify
from flask_cors import CORS
from tempo_produzione_unita import IO_calcolo_tempo_produzione_unita
from analisi_monete_conio import IO_monete_e_risorse_necessarie_per_n_nobili
from ricerca_villaggio_conio import IO_ricerca_villaggio_conio
app = Flask(__name__)
CORS(app)

def menu():
    menu_text = "Cosa vuoi fare?\n"
    menu_text += "1. Calcolare il tempo di addestramento (In progress)\n"
    menu_text += "2. Calcolare monete e risorse per nobili. (In progress)\n"
    menu_text += "3. Ricercare il migliore villaggio dove coniare\n"
    menu_text += "Inserisci il numero corrispondente all'azione desiderata: "
    return menu_text

@app.route('/esegui_script', methods=['POST'])
def esegui_script():
    data = request.get_json()
    scelta = data.get('scelta')

    menu_text = menu()

    if scelta == "1":
        risultato = IO_calcolo_tempo_produzione_unita()
    elif scelta == "2":
        risultato = IO_monete_e_risorse_necessarie_per_n_nobili()
    elif scelta == "3":
        risultato = IO_ricerca_villaggio_conio()
    elif scelta == "0":
        risultato = "Arrivederci!"
    else:
        risultato = "Scelta non valida. Riprova."

    return jsonify({"menu": menu_text, "risultato": risultato})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)