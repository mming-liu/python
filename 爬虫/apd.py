import requests
import os
import time
import json

def claim_push(data):
    url = 'http://192.168.200.161:10007/web-suite/services/restful/claim/pushClaim'
    headers = {'Authorization':''}
    response = requests.post(url,headers = headers,json = data)
    return response.json()

def claim_no(str):
    date = time.strftime('%y%m%d',time.localtime())
    claim_no = 'acc_'+date +'_00' +str
    return claim_no

def open_txt(filename):
    path = 'C:/Users/ccc/Desktop/APD/5.0报文/' + filename
    # with os.open(path,'r',encoding='utf-8') as f:
    #     data = f.read()
    #     data = json.dumps(data)
    # return data
    f = open(path,'r',encoding='utf-8')
    # data = json.dumps(f.read())
    data = f.read()
    return data


if __name__ == '__main__':
    data = open_txt('APD5.0报文.txt')
    a = claim_push(data)
    print(a)
