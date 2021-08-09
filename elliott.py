import requests

url = "https://api.hospitalpriceindex.com/itemList/list"

payload = "{\"defId\":7855,\"priceStatus\":\"published\",\"page\":{\"from\":1,\"size\":50000},\"sortInput\":[{\"reverse\":false,\"by\":\"description\"}],\"listName\":\"serviceList\",\"filters\":[{\"property\":\"description\",\"value\":\"**\",\"type\":\"all\"},{\"property\":\"payerId\",\"value\":\"0\",\"type\":\"match\"}]}"
headers = {
    'authority': 'api.hospitalpriceindex.com',
    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
    'accept': 'application/json, text/plain, */*',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
    'content-type': 'application/json',
    'origin': 'https://search.hospitalpriceindex.com',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://search.hospitalpriceindex.com/',
    'accept-language': 'en-US,en;q=0.9'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
