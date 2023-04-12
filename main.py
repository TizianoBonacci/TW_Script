from tempo_produzione_unita import IO_calcolo_tempo_produzione_unita
from analisi_monete_conio import IO_monete_e_risorse_necessarie_per_n_nobili
from replit import db
import requests
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
# Inizializza l'applicazione Firebase con le tue credenziali di progetto
cred = credentials.Certificate("contatoretw-firebase-adminsdk-mzqnw-6fcec2f4a2.json")
firebase_admin.initialize_app(cred, {'databaseURL': 'https://contatoretw-default-rtdb.firebaseio.com/'})

# Leggi il contatore dal database
def read_counter():
    counter_ref = db.reference('counter')
    counter = counter_ref.get()
    if counter is None:
        counter = 0
    return counter

# Aggiorna il contatore nel database
def update_counter(counter):
    counter_ref = db.reference('counter')
    counter_ref.set(counter)
  
def menu():
    print("Cosa vuoi fare?")
    print("1. Calcolare il tempo di addestramento")
    print("2. Calcolatore monete/risorse conio monete")

    #print("0. Esci")
    scelta = input("Inserisci il numero corrispondente all'azione desiderata: ")
    return scelta
  
counter = read_counter()
print(f"Questo script è stato utilizzato {counter} volte!.")
print("\n")
counter = read_counter()
counter += 1
update_counter(counter)
while True:

  scelta = menu()
  if scelta == "1":
    IO_calcolo_tempo_produzione_unita()
  if scelta == "2":
    IO_monete_e_risorse_necessarie_per_n_nobili()

  elif scelta == "0":
    print("Arrivederci!")
    break
  else:
    print("Scelta non valida. Riprova.")
