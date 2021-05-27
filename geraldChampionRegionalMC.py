import json
import csv
import pandas as pd

json_data = 'C:\\Users\\jackb\\Desktop\\FileOpen\\geraldChampionRegionalMC\\GeraldChampionRegionalMedicalCenter_standardcharges.json'
csv_write = r'C:\\Users\\jackb\\Desktop\\FileOpen\\geraldChampionRegionalMC\\GeraldChampionRegionalMedicalCenter_standardchargesFIXED.csv'
# main_key = 'people'

# simple (flat) print json
with open(json_data) as json_file:
    data = json.load(json_file, strict=False)
    # for p in data:
    #     print(json.dumps(data, sort_keys=True, indent=4))


df = pd.read_json(json_data)

print(df)
print(df.info())
df.to_csv(csv_write)
