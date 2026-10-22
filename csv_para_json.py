"""Converte o data.csv oficial do Hubble (NASA) em hubble-birthday.json.
Uso:  python3 csv_para_json.py data.csv      ->  gera hubble-birthday.json
Baixe o CSV em: https://imagine.gsfc.nasa.gov/hst_bday/data.csv
Depois coloque hubble-birthday.json na MESMA pasta do index.html."""
import csv, json, sys
rows = list(csv.DictReader(open(sys.argv[1], encoding='utf-8-sig')))
json.dump(rows, open('hubble-birthday.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(rows), 'datas gravadas em hubble-birthday.json')
