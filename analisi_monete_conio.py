from tabulate import tabulate

def monete_e_risorse_necessarie_per_n_nobili(n_monete_esistenti, n_nobili_da_produrre):
    # Calcola il numero di nobili esistenti e le monete in eccesso
    n_nobili_esistenti = 0
    while n_monete_esistenti >= n_nobili_esistenti + 1:
        n_nobili_esistenti += 1
        n_monete_esistenti -= n_nobili_esistenti

    # Calcola il numero di monete necessarie per produrre ulteriori N nobili
    monete_necessarie = 0
    for i in range(n_nobili_esistenti + 1, n_nobili_esistenti + n_nobili_da_produrre + 1):
        monete_necessarie += i

    # Sottrai le monete in eccesso esistenti
    monete_necessarie -= n_monete_esistenti

    # Calcola le risorse necessarie
    legno_necessario = monete_necessarie * 28000
    argilla_necessaria = monete_necessarie * 30000
    ferro_necessario = monete_necessarie * 25000

    return n_nobili_esistenti, n_monete_esistenti, monete_necessarie, legno_necessario, argilla_necessaria, ferro_necessario

def IO_monete_e_risorse_necessarie_per_n_nobili():
  n_monete_esistenti = int(input("Totale monete attuale: (numero) "))
  n_nobili_da_produrre = int(input("Quanti nobili ulteriori vuoi produrre? (numero): "))


  n_nobili_esistenti, monete_in_eccesso, monete_necessarie, legno_necessario, argilla_necessaria, ferro_necessario = monete_e_risorse_necessarie_per_n_nobili(n_monete_esistenti, n_nobili_da_produrre)


  legno_necessario = "{:,.0f}".format(legno_necessario).replace(',', ' ').replace('.', ',')
  argilla_necessaria = "{:,.0f}".format(argilla_necessaria).replace(',', ' ').replace('.', ',')
  ferro_necessario = "{:,.0f}".format(ferro_necessario).replace(',', ' ').replace('.', ',')

  
  headers = ["Limite nobili", "Già risparmiate per il limite di nobili: "+str(n_nobili_esistenti+1)]
  table_data = [[n_nobili_esistenti, monete_in_eccesso]]


  headers_2 = ["Monete", "Legno", "Argilla", "Ferro"]
  table_data_2 = [[monete_necessarie, legno_necessario, argilla_necessaria, ferro_necessario]]


  
  # Stampa della tabella
  print("\n")
  print("Limite nobili: "+str(n_nobili_esistenti))
  print("Già risparmiate per il limite di nobili: "+str(monete_in_eccesso))

  #print(tabulate(table_data, headers=headers))
  print("\n")
  print("PER ALZARE DI "+str(n_nobili_da_produrre)+" IL LIMITE DEI NOBILI SARANNO NECESSARI:")
  print("\n")
  print(tabulate(table_data_2, headers=headers_2))

  print("\n")
