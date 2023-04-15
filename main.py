from tempo_produzione_unita import IO_calcolo_tempo_produzione_unita
from analisi_monete_conio import IO_monete_e_risorse_necessarie_per_n_nobili
from ricerca_villaggio_conio import IO_ricerca_villaggio_conio
from replit import db
import requests
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
# Inizializza l'applicazione Firebase con le tue credenziali di progetto
cred = credentials.Certificate("contatoretw-firebase-adminsdk-mzqnw-6fcec2f4a2.json")
firebase_admin.initialize_app(cred, {'databaseURL': 'https://contatoretw-default-rtdb.firebaseio.com/'})

# Ottieni l'indirizzo IP pubblico dell'utente
def get_public_ip():
    response = requests.get("https://api.ipify.org?format=json")
    ip_data = response.json()
    return ip_data["ip"]

# Salva l'indirizzo IP su Firebase e ritorna il numero di utilizzatori unici
def save_unique_ip(ip):
    unique_ips_ref = db.reference("unique_ips")
    unique_ips = unique_ips_ref.get()
    if unique_ips is None:
        unique_ips = {}

    ip_key = ip.replace('.', '-')
    if ip_key not in unique_ips:
        unique_ips[ip_key] = True
        unique_ips_ref.set(unique_ips)

    return len(unique_ips)
def count_unique_users():
    unique_ips_ref = db.reference("unique_ips")
    unique_ips = unique_ips_ref.get()
    if unique_ips is None:
        num_unique_users = 0
    else:
        num_unique_users = len(unique_ips)
    return num_unique_users
    print(f"Il numero di utilizzatori unici è {num_unique_users}.")


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
    print("3. Ricerca migliore villaggio per conio")


    #print("0. Esci")
    scelta = input("Inserisci il numero corrispondente all'azione desiderata: ")
    return scelta
  
counter = read_counter()
unique_users=count_unique_users()

counter = read_counter()
counter += 1
update_counter(counter)
ip = get_public_ip()
num_unique_users = save_unique_ip(ip)
print(f"Questo script è stato utilizzato {counter} volte!. Da {unique_users} utenti")
print("\n")
while True:

  scelta = menu()
  if scelta == "1":
    IO_calcolo_tempo_produzione_unita()
  if scelta == "2":
    IO_monete_e_risorse_necessarie_per_n_nobili()
  if scelta == "3":
    IO_ricerca_villaggio_conio()

  elif scelta == "0":
    print("Arrivederci!")
    break
  else:
    print("Scelta non valida. Riprova.")
