from json.encoder import JSONEncoder
import requests
import json
import cx_Oracle
from requests.api import post, request

class open_file():
    def open_txt(filename):
    # 打开报文文件，读取报文内容，并转换为字典（dict）型数据
        path = 'C:/Users/ccc/Desktop/APD/5.0报文/' + filename
        with open(path,'r',encoding='utf-8') as f:
            data = f.read()
            return eval(data)

class do_push():
    def __init__(self,claim_no):
        self.claim_no = claim_no

    def claim_push(self,data,nodeType,nextNodeType):
        url = 'http://192.168.200.161:10007/web-suite/services/restful/claim/pushClaim'
        headers = { 'authorization': 'gzqxW_sBQiaV0PlPKp5cG1QbduSclbAyx6QMtEXZcA07WLWk20bEx4vT',
        'content-type': 'application/json;charset=UTF-8'
        }

        if nodeType < nextNodeType:
            pass
        else:
            data['requestType'] = '2'

        # 替换值
        data['claimNo'] = self.claim_no
        data['accidentNo'] = self.claim_no
        data['nodeType'] = nodeType
        data['nextNodeType'] = nextNodeType
        
        data = json.dumps(data,ensure_ascii=False)
        response = requests.post(url,headers = headers,data = data.encode('utf-8') )
        return response

    def get_request(self):
        # print(claim_no)
        conn = cx_Oracle.connect('apd_v50_test/apd_v50_test@192.168.200.25:1521/orcl')
        # 使用cursor()方法获取操作游标
        cursor = conn.cursor()
        #使用execute方法执行SQL语句
        result=cursor.execute(" select  request_param from t_interface_log  where business_no = "+ "'"+self.claim_no+"'" + " and interface_code = 'ClaimInfoSync' order by start_date desc" )

        #使用fetchone()方法获取一条数据
        data=cursor.fetchone()

        #获取所有数据
        # all_data=cursor.fetchall()
        #获取部分数据，8条
        #many_data=cursor.fetchmany(8)
        #  data1 = json.load(data[0])     直接用文件流转换，json格式有问题
        try:
            data = json.loads(str(data[0]))
            return data
        except :
            return None

    def new_message(self,data):
        data1 = data
        data2 = self.get_request()
        del data2['accidentNo']
        data1.update(data2)
        return data1

class do_task():
    def __init__(self,claim_no):
        self.claim_no = claim_no

    def claim_task(self,data,nodeType,nextNodeType):
        url = 'http://192.168.200.161:10007/web-suite/services/restful/claimStatus/claimStatusSync'
        headers = {'Authorization':'gzqxW_sBQiaV0PlPKp5cG1QbduSclbAyx6QMtEXZcA07WLWk20bEx4vT',
        'Content-Type': 'application/json;charset=UTF-8'}

        data['claimNo'] = self.claim_no
        data['accidentNo'] = self.claim_no
        data['nodeType'] = nodeType
        data['nextNodeType'] = nextNodeType

        data = json.dumps(data,ensure_ascii=False)
        response = requests.post(url,headers = headers,data = data.encode('utf-8') )
        return response

class claim_push():
    def __init__(self,claim_no):
        self.message_a = open_file.open_txt('APD5.0报文.txt')
        self.message_b = open_file.open_txt('5.0状态同步接口.txt')
        self.a = do_push(claim_no)
        self.b = do_task(claim_no)
    
    def message_c(self):
        message = self.a.new_message(self.message_a)
        return message

    def push_task(self):
        response = self.a.claim_push(self.message_a,'01','01')
        return response.json()

    def push_audit(self):
        # 提交到核损
        self.b.claim_task(self.message_b,'01','03')
        response = self.a.claim_push(self.message_c(),'01','03')
        return response.json()
    
    def push_douAudit(self,type):
        if type == '1':
            self.push_audit()
            self.b.claim_task(self.message_b,'03','06')
            self.b.claim_task(self.message_b,'06','07')    
            response = self.a.claim_push(self.message_c(),'06','07')        
        elif type == '2':
            self.b.claim_task(self.message_b,'01','03')
            self.b.claim_task(self.message_b,'03','06')
            self.b.claim_task(self.message_b,'06','07')
            response = self.a.claim_push(self.message_c(),'06','07')
        return response.json()
    
    def task_done(self,type):
        try:
            if type == '1' :
                self.b.claim_task(self.message_b,'01','03')
                self.b.claim_task(self.message_b,'03','04')
            else :
                self.b.claim_task(self.message_b,'01','03')
                self.b.claim_task(self.message_b,'03','06')
                self.b.claim_task(self.message_b,'06','07')
                self.b.claim_task(self.message_b,'06','07')
            return "Done"
        except Exception as e:
            return e
           
    def back_push(self,nodetype,nextNodetype):
        self.b.claim_task(self.message_b,nodetype,nextNodetype)
        # print(self.message_b)
        response = self.a.claim_push(self.message_c(),nodetype,nextNodetype)
        # print(self.message_c())
        return response.json()
    
if __name__ == '__main__':
    claim_no = 'acc_20210325_002'
    push = claim_push(claim_no)

    # 推单子到定损
    # response = push.push_task()
    # print(response)

    # 单子提交到核损
    response = push.push_audit()
    print(response)

    # 单子提交到复勘审核
    # response = push.push_douAudit('1')
    # print(response)

    # 单子退回定损
    response = push.back_push('03','01')
    print(response)