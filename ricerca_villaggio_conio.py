import re
from itertools import combinations
import math
from typing import Tuple, List
from tabulate import tabulate
import requests
from bs4 import BeautifulSoup


def distance(coord1: Tuple[int, int], coord2: Tuple[int, int]) -> float:
    x1, y1 = coord1
    x2, y2 = coord2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def find_best_villages(input_string, n=5):
    lines = input_string.strip().split('\n')
    village_data = []

    for line in lines[3:]:
        if '|' in line:
            name, coords = line[:-7], line[-7:]
            x, y = coords.split('|')
            village_data.append((name, (int(x), int(y))))

    distances = []
    for i, village1 in enumerate(village_data):
        for j, village2 in enumerate(village_data[i + 1:]):
            dist = distance(village1[1], village2[1])
            distances.append((village1, village2, dist))

    avg_distances = []
    for village in village_data:
        total_distance = sum(dist for v1, v2, dist in distances if village in (v1, v2))
        num_connections = sum(1 for v1, v2, dist in distances if village in (v1, v2))
        avg_distance = total_distance / num_connections
        avg_distances.append((village, avg_distance))

    avg_distances.sort(key=lambda x: x[1])
    return avg_distances[:n]


def IO_ricerca_villaggio_conio():

  url = input("Inserisci l'URL del profilo in modalità ospite: ")


  response = requests.get(url)
  
  if response.status_code == 200:
      soup = BeautifulSoup(response.text, 'html.parser')
      villages_list = soup.find(id="villages_list").text.replace("\n\n","")
  
      # if villages_list:
      #     print(villages_list)
      # else:
      #     print("L'elemento con l'ID 'villages_list' non è stato trovato nella pagina.")
  else:
      print(f"Errore durante il recupero della pagina. Codice di stato: {response.status_code}")
  
  
  best_villages = find_best_villages(villages_list, 5)
  print("\n")
  print("Questi sono i migliori villaggi in cui coniare per distanza tra i restanti villaggi:")
  table_data = []
  for village, avg_distance in best_villages:
      table_data.append([village[0], village[1][0], village[1][1], f"{avg_distance:.3f}"])
  
  # Creiamo la tabella usando tabulate
  table = tabulate(table_data, headers=["Village Name", "X", "Y", "Avg Distance"],   tablefmt="pretty")
  print(table)
  print("\n")
  

