import requests
import json
import pandas as pd

csv_write = r'C:\\Users\\jackb\Desktop\\FileOpen\\json_data_Norton.csv'
url = "https://api.hospitalpriceindex.com/itemList/list"

payload = "{\"defId\":8160,\"priceStatus\":\"published\",\"page\":{\"from\":1,\"size\":50},\"sortInput\":[{\"reverse\":false,\"by\":\"description\"}],\"listName\":\"priceList\",\"filters\":[{\"property\":\"description\",\"value\":\"\",\"type\":\"all\"}]}"
headers = {
    'authority': 'api.hospitalpriceindex.com',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    'accept': 'application/json, text/plain, */*',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'content-type': 'application/json',
    'origin': 'https://search.hospitalpriceindex.com',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://search.hospitalpriceindex.com/',
    'accept-language': 'en-US,en;q=0.9'
}

r = requests.request("POST", url, headers=headers, data=payload)


NortonData = r.json()

df = pd.json_normalize(NortonData['result'], record_path=['items'])
# df2 = pd.json_normalize(df["items"])

df.to_csv(csv_write, index=False)
print(df.head)
