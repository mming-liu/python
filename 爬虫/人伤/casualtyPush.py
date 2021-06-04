import json
from jsonpath_ng import parse
import requests
from requests.models import Response


class open_file():
    def __init__(self) -> None:
        pass

    def open_txt(self,filename = '推单子报文-最新.txt'):
        # 打开报文文件，读取报文内容，并转换为字典（dict）型数据
        path = 'D:/git/python/爬虫/人伤/' + filename
        with open(path, 'r', encoding='utf-8') as f:
            data = f.read()
            global false, null, true
            false = null = true = ''
            return eval(data)

class casualtyPush():
    def __init__(self, accidentNo):
        self.accidentNo = accidentNo

    def claim_push(self, data = open_file().open_txt()):
        url = 'http://192.168.200.165:10001/casualty/interface/task/dispatch'
        headers = {
                   'content-type': 'application/json;charset=UTF-8'
                   }
        
        path = '$.accidentInfo.accidentNo'
        accidentNo = self.accidentNo
        jsonpath_expr = parse(path)
        jsonpath_expr.find(data)
        updated_json = jsonpath_expr.update(data, accidentNo)
        # print(data)
        data['taskNo'] = self.accidentNo
        data['lightInquiryUniqueId'] = self.accidentNo

        # # accidentType ： AccidentType002 多车事故，AccidentType001 单车事故
        # path = '$.accLossInfo.accidentType'
        # accidentType = 'AccidentType001'
        # jsonpath_expr = parse(path)
        # jsonpath_expr.find(data)
        # data = jsonpath_expr.update(data, accidentType)

        data = json.dumps(data, ensure_ascii=False)
        response = requests.post(url, headers=headers, data=data.encode('utf-8'))
        return response

if __name__ == '__main__':
    # a = open_file()
    # data = a.open_txt('推单子报文-最新.txt')
    # print(data)

    accidentNo = 'acc_20210602_001'
    response = casualtyPush(accidentNo).claim_push()
    print(response.text)