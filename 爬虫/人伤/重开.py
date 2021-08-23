import json
import requests

url = 'http://192.168.200.165:10001/casualty/interface/task/reopen'


data  = {"taskNo":"acc_20210712_001","companyCode":"SH0103","userAccount":"sh"}

headers = {
            'content-type': 'application/json;charset=UTF-8'
            }

data = json.dumps(data, ensure_ascii=False)
response = requests.post(url, headers=headers, data=data.encode('utf-8'))

print(response.text)