import re
from itertools import combinations
import math
from typing import Tuple, List

import requests
from bs4 import BeautifulSoup


def distance(coord1: Tuple[int, int], coord2: Tuple[int, int]) -> float:
    x1, y1 = coord1
    x2, y2 = coord2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def find_best_villages(input_string: str, n: int = 5) -> List[Tuple[str, Tuple[int, int]]]:
    lines = input_string.split('\n')
    village_data = []

    for line in lines:
        coords_match = re.search(r'(\d+\|\d+)', line)
        if coords_match:
            coords_str = coords_match.group()
            coords = tuple(map(int, coords_str.split('|')))
            village_name = re.search(r'^(.+?)\s*\d+\|\d+', line).group(1).strip()
            village_data.append((village_name, coords))

    avg_distances = []

    for i, (name1, coords1) in enumerate(village_data):
        total_distance = sum(distance(coords1, coords2) for _, coords2 in village_data if coords1 != coords2)
        avg_distance = total_distance / (len(village_data) - 1)
        avg_distances.append((avg_distance, name1, coords1))

    avg_distances.sort()
    best_villages = [(name, coords) for _, name, coords in avg_distances[:n]]

    return best_villages



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
  
  
  best_villages = find_best_villages(villages_list)
  print("\n")
  print("Questi sono i migliori villaggi in cui coniare per distanza tra i restanti villaggi:")
  for name, coords in best_villages:
      print(f"{name} {coords}")
  print("\n")

  

