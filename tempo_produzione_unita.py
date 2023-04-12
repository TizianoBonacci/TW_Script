from utils import converti_tempo
from tabulate import tabulate


def tempo_di_produzione_parallela(n_asce, n_cavalli, n_arieti, n_spadaccini,
                                  n_lancieri, n_cavalleria_pesante):
  tempo_ascia = 2 * 60 + 51  # 2 minuti e 51 secondi
  tempo_cavallo = 5 * 60 + 12  # 5 minuti e 12 secondi
  tempo_ariete = 24 * 60 + 50  # 24 minuti e 50 secondi
  tempo_spadaccino = 3 * 60 + 15  # 3 minuti e 15 secondi
  tempo_lanciere = 2 * 60 + 13  # 2 minuti e 13 secondi
  tempo_cavalleria_pesante = 10 * 60 + 24  # 10 minuti e 24 secondi

  tempo_totale_asce = n_asce * tempo_ascia
  tempo_totale_cavalli = n_cavalli * tempo_cavallo
  tempo_totale_arieti = n_arieti * tempo_ariete
  tempo_totale_spadaccini_lancieri = n_spadaccini * tempo_spadaccino + n_lancieri * tempo_lanciere

  tempo_totale_spadaccini = n_spadaccini * tempo_spadaccino
  tempo_totale_lancieri = n_lancieri * tempo_lanciere
  tempo_totale_cavalleria_pesante = n_cavalleria_pesante * tempo_cavalleria_pesante

  tempo_asce = converti_tempo(tempo_totale_asce)
  tempo_cavalli = converti_tempo(tempo_totale_cavalli)
  tempo_arieti = converti_tempo(tempo_totale_arieti)
  tempo_spadaccini = converti_tempo(tempo_totale_spadaccini)
  tempo_lancieri = converti_tempo(tempo_totale_lancieri)
  tempo_lance_spade = converti_tempo(tempo_totale_spadaccini_lancieri)
  tempo_cavalleria_pesante = converti_tempo(tempo_totale_cavalleria_pesante)

  legno_asce = 60 * n_asce
  argilla_asce = 30 * n_asce
  ferro_asce = 40 * n_asce

  legno_cavalli = 125 * n_cavalli
  argilla_cavalli = 100 * n_cavalli
  ferro_cavalli = 250 * n_cavalli

  legno_arieti = 300 * n_arieti
  argilla_arieti = 200 * n_arieti
  ferro_arieti = 200 * n_arieti

  legno_spadaccini = 30 * n_spadaccini
  argilla_spadaccini = 30 * n_spadaccini
  ferro_spadaccini = 70 * n_spadaccini

  legno_lancieri = 50 * n_lancieri
  argilla_lancieri = 30 * n_lancieri
  ferro_lancieri = 10 * n_lancieri

  legno_cavalleria_pesante = 200 * n_cavalleria_pesante
  argilla_cavalleria_pesante = 150 * n_cavalleria_pesante
  ferro_cavalleria_pesante = 600 * n_cavalleria_pesante

  # Restituisci le risorse assieme ai tempi di produzione
  return tempo_asce, tempo_cavalli, tempo_arieti, tempo_lance_spade, tempo_cavalleria_pesante, \
           (legno_asce, argilla_asce, ferro_asce), \
           (legno_cavalli, argilla_cavalli, ferro_cavalli), \
           (legno_arieti, argilla_arieti, ferro_arieti), \
           (legno_spadaccini, argilla_spadaccini, ferro_spadaccini), \
           (legno_lancieri, argilla_lancieri, ferro_lancieri), \
           (legno_cavalleria_pesante, argilla_cavalleria_pesante, ferro_cavalleria_pesante)


def IO_calcolo_tempo_produzione_unita():
  while True:

    tipo_unita = input(
      "Vuoi addestrare unità offensive o difensive? (off/diff) ")
    if tipo_unita == "off":
      n_asce = int(input("Inserisci il numero di asce: "))
      n_cavalli = int(input("Inserisci il numero di cavalli: "))
      n_arieti = int(input("Inserisci il numero di arieti: "))
      n_spadaccini = 0
      n_lancieri = 0
      n_cavalleria_pesante = 0

    elif tipo_unita == "diff":
      n_spadaccini = int(input("Inserisci il numero di spadaccini: "))
      n_lancieri = int(input("Inserisci il numero di lancieri: "))
      n_cavalleria_pesante = int(
        input("Inserisci il numero di cavalleria pesante: "))
      n_asce = 0
      n_cavalli = 0
      n_arieti = 0


    else:
      print("Scelta non valida. Riprova.")
      continue

    tempo_asce, tempo_cavalli, tempo_arieti, tempo_lance_spade, tempo_cavalleria_pesante,risorse_asce, risorse_cavalli, risorse_arieti, risorse_spadaccini, risorse_lancieri, risorse_cavalleria_pesante = tempo_di_produzione_parallela(n_asce, n_cavalli, n_arieti, n_spadaccini, n_lancieri, n_cavalleria_pesante)

    headers = ["Unità", "Legno", "Argilla", "Ferro", "Giorni", "Ore", "Minuti"]
    table_data = []

    if tipo_unita == "off":
        table_data.append(["Asce"] + list(risorse_asce) + list(tempo_asce))
        table_data.append(["Cavalli"] + list(risorse_cavalli) + list(tempo_cavalli))
        table_data.append(["Arieti"] + list(risorse_arieti) + list(tempo_arieti))
    elif tipo_unita == "diff":
        risorse_lancie_spade = (
            risorse_spadaccini[0] + risorse_lancieri[0], 
            risorse_spadaccini[1] + risorse_lancieri[1], 
            risorse_spadaccini[2] + risorse_lancieri[2]
        )
        table_data.append(["Lancie/Spade"] + list(risorse_lancie_spade) + list(tempo_lance_spade))
        table_data.append(["Cavalleria Pesante"] + list(risorse_cavalleria_pesante) + list(tempo_cavalleria_pesante))

    # Stampa della tabella
    print("\n")
    print(tabulate(table_data, headers=headers))
    print("\n")



