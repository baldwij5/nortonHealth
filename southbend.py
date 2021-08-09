import requests
import json
import pandas as pd

url = "https://apim.services.craneware.com/api-pricing-transparency/api/public/3ca922f1a0c5e2e558d1f47c5a663944/charges/standardCharges?page=0&limit=250&search=&codeType="

payload = {}
headers = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
    'Accept': 'application/json, text/plain, */*',
    'Content-Encoding': 'identity',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
    'Origin': 'https://www.cdmpricing.com',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://www.cdmpricing.com/',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cookie': 'ApplicationGatewayAffinity=28d3f836d72c113f3c64ba238c7a7bbf4d64bf76b299fd91f5fc559d5a278bd6; ApplicationGatewayAffinityCORS=28d3f836d72c113f3c64ba238c7a7bbf4d64bf76b299fd91f5fc559d5a278bd6'
}

r = requests.request("GET", url, headers=headers, data=payload)

# print(r.text)
southBendData = r.json()
df = pd.json_normalize(southBendData['response'], record_path=['payors'])
df.to_csv(r'Desktop\\southBend.csv', index=False)
print(df.head)
