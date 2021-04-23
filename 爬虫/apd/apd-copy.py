# This Python file uses the following encoding: utf-8
import os,sys
from json.encoder import JSONEncoder
import jsonpath 
from jsonpath_ng import parse
import requests
import json
import cx_Oracle
from requests.api import post, request
from decimal  import Decimal

class open_file():
    # def __init__(self) -> None:
    #     pass

    def resource_path(self,relative_path):
        if getattr(sys, 'frozen', False): #是否Bundle Resource
            base_path = sys._MEIPASS
        else:
            base_path = os.path.abspath(".")
        return os.path.join(base_path,relative_path)

    def open_txt(filename):
    # 打开报文文件，读取报文内容，并转换为字典（dict）型数据
        # path = 'C:/Users/ee54/Desktop/APD/5.0报文/' + filename
        curr_path=os.path.dirname(__file__)
        # curr_path = os.path.abspath(".") 
        # print(curr_path)
        path = os.path.join(curr_path,filename)
        with open(path,'r',encoding='utf-8') as f:
            data = f.read()
            return eval(data)

class claimPush():
    def __init__(self,claim_no):
        self.claim_no = claim_no

    def claim_push(self,data,nodeType,nextNodeType):
        url = 'http://192.168.200.161:10007/web-suite/services/restful/claim/pushClaim'
        headers = { 'authorization': 'gzqxW_sBQiaV0PlPKp5cG1QbduSclbAyx6QMtEXZcA07WLWk20bEx4vT',
        'content-type': 'application/json;charset=UTF-8'
        }

        if (nodeType == '01' and nextNodeType == '01') or (int(nodeType) > int(nextNodeType)):
            data['requestType'] = '2'
        else:
            pass

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
        try:
            data1 = data
            data2 = self.get_request()
            del data2['accidentNo']
            data1.update(data2)
            return data1
        except Exception as e:
            return data

    def change_loss(self,whole_data):
        # print(type(whole_data))
        data = self.new_message(whole_data)
        laborValue1 = jsonpath.jsonpath(data,expr='$.claimLabors[*].laborFeeAfterDiscount')
        laborValue2 = jsonpath.jsonpath(data,expr='$.claimLabors[*].operationType')
        partQuantity = jsonpath.jsonpath(data,expr='$.claimParts[*].partQuantity')
        unitPrice = jsonpath.jsonpath(data,expr='$.claimParts[*].unitPrice')
        repairLabors = jsonpath.jsonpath(data,expr='$.claimOuterRepairLabors[*].outerRepairFee')
        materialFee = jsonpath.jsonpath(data,expr='$.claimMaterials[*].materialFee')
        materialQuantity = jsonpath.jsonpath(data,expr='$.claimMaterials[*].materialQuantity')

        try:
            lenth = len(partQuantity)
            if lenth >= 1 :
                for i in range(1,lenth+1):
                    # print(i, i % 2)
                    if i % 2== 1:
                        path = '$.claimParts['+str(i-1)+'].partQuantity'
                        part_quantity = partQuantity[i-1]+2
                        jsonpath_expr  = parse(path)
                        jsonpath_expr.find(data)
                        updated_json = jsonpath_expr.update(data, part_quantity)
                    else :
                        path = '$.claimParts['+str(i-1)+'].unitPrice'
                        unit_Price = unitPrice[i-1]+1000
                        unit_Price = float(Decimal(unit_Price).quantize(Decimal("0.0000")))
                        jsonpath_expr  = parse(path)
                        jsonpath_expr.find(data)
                        updated_json = jsonpath_expr.update(data, unit_Price)
        except :
            pass

        try:
            for m in laborValue2:
                if m == '03':
                    # print(laborValue2.index(m))
                    path = '$.claimLabors['+str(laborValue2.index(m))+'].laborFee'
                    # print(path)
                    paint_fee = laborValue1[laborValue2.index(m)]+1000
                    jsonpath_expr  = parse(path)
                    jsonpath_expr.find(data)
                    updated_json = jsonpath_expr.update(data, paint_fee)
                    # list的值重复时，只能取到第一个index，所以改list中的值，才能取到符合条件的下一个值
                    laborValue2[laborValue2.index(m)] = '05'
                elif m == '02' or m == '04':
                    path = '$.claimLabors['+str(laborValue2.index(m))+'].laborFeeAfterDiscount'
                    # print(path)
                    labor_fee = laborValue1[laborValue2.index(m)]+1000
                    jsonpath_expr  = parse(path)
                    jsonpath_expr.find(data)
                    updated_json = jsonpath_expr.update(data, labor_fee)
                    laborValue2[laborValue2.index(m)] = '05'
        except :
            pass

        try:
            for m in repairLabors:
                path = '$.claimOuterRepairLabors['+str(repairLabors.index(m))+'].outerRepairFee'
                repairLabors = repairLabors[repairLabors.index(m)]+1000
                jsonpath_expr  = parse(path)
                jsonpath_expr.find(data)
                updated_json = jsonpath_expr.update(data, repairLabors)                
        except :
            pass

        try:
            lenth = len(materialQuantity)
            if lenth >= 1 :
                for i in range(1,lenth+1):
                    # print(i, i % 2)
                    if i % 2== 1:
                        path = '$.claimMaterials['+str(i-1)+'].materialQuantity'
                        material_quantity = materialQuantity[i-1]+2
                        jsonpath_expr  = parse(path)
                        jsonpath_expr.find(data)
                        updated_json = jsonpath_expr.update(data, material_quantity)
                    else :
                        path = '$.claimMaterials['+str(i-1)+'].materialFee'
                        material_Price = materialFee[i-1]+1000
                        material_Price = float(Decimal(materialFee).quantize(Decimal("0.0000")))
                        jsonpath_expr  = parse(path)
                        jsonpath_expr.find(data)
                        updated_json = jsonpath_expr.update(data, material_Price)
        except :
            pass
        return data

class claimStatus():
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

class do_task():
    def __init__(self,claim_no):
        self.message_a = open_file.open_txt('claimPush.txt')
        self.message_b = open_file.open_txt('ClaimInfoSync.txt')
        self.a = claimPush(claim_no)
        self.b = claimStatus(claim_no)
    
    def message_c(self):
        message = self.a.new_message(self.message_a)
        return message
    
    def change(self):
        message = self.a.change_loss(self.message_c())
        return message

    def push_task(self):
        # 定损单推送
        response = self.a.claim_push(self.message_a,'01','01')
        return response.json()
    
    def push_priceCheck(self):
        '''提交到核价'''
        response = self.b.claim_task(self.message_b,'01','02')
        return response.json()

    def push_audit(self,type):
        '''#提交到核损：
            01,先提交核价，再提交到核损。
            02,不经过核价，直接提交到核损
        '''
        if type == '01':
            response = self.b.claim_task(self.message_b,'01','02')
            response = self.b.claim_task(self.message_b,'02','03')
        elif type == '02':
            response = self.b.claim_task(self.message_b,'01','03')
        # response = self.a.claim_push(self.message_c(),'01','03')
        return response.json()
    
    def pre_audit(self):
        # 核损预审核
        response = self.a.claim_push(self.message_c(),'03','03')
        return response.json()
    
    def push_douAudit(self,type):
        '''
        type = 1,从核损提交到复勘审核
        type = 2,从定损提交到复勘审核
        '''
        if type == '1':
            self.push_audit()
            self.b.claim_task(self.message_b,'03','06')
            response = self.b.claim_task(self.message_b,'06','07')    
            # response = self.a.claim_push(self.message_c(),'06','07')        
        elif type == '2':
            self.b.claim_task(self.message_b,'01','03')
            self.b.claim_task(self.message_b,'03','06')
            response = self.b.claim_task(self.message_b,'06','07')
            # response = self.a.claim_push(self.message_c(),'06','07')
        return response.json()
    
    def task_done(self,type):
        '''
        适用于从定损直接到定核损结束。要想从其他环节提交到定核损结束，使用 back_push().
        type = 1 ,从核损提交到定核损结束;
        type = 2 ,从复勘审核提交到定损单结束
        '''
        try:
            if type == '1' :
                self.b.claim_task(self.message_b,'01','03')
                self.b.claim_task(self.message_b,'03','04')
            else :
                self.b.claim_task(self.message_b,'01','02')
                self.b.claim_task(self.message_b,'02','03')
                self.b.claim_task(self.message_b,'03','06')
                self.b.claim_task(self.message_b,'06','07')
                self.b.claim_task(self.message_b,'07','04')
            return "Done"
        except Exception as e:
            return e
           
    def back_push(self,type,nodetype,nextNodetype):
        '''
        主要是退回，也可以用于指定环节的提交.
        type = '01',不做修改，直接退回;type = '02',修改损失项目再退回
        '''
        if type == '01':
            self.b.claim_task(self.message_b,nodetype,nextNodetype)
            response = self.a.claim_push(self.message_c(),nodetype,nextNodetype)
        elif type == '02':
            self.b.claim_task(self.message_b,nodetype,nextNodetype)
            response = self.a.claim_push(self.change(),nodetype,nextNodetype)
            # print(self.change())
        return response.json()
    
if __name__ == '__main__':
    # try:
        claim_no = input('请输入定损单号：')

        '''
        1：新增定损单
        2：定损单推送到核价
        3：定损单推送到核损，不经过核价
        4：定损单推送到核价，经过核价
        5：定损单从定损推送到复勘审核
        6：定损单从核损推送到复勘审核
        7：定损单退回到定损，且修改损失项目
        8：定损单退回到定损，不修改损失项目
        9：定损单从核损推送到定核损结束
        10：定损单从复勘审核推送到定核损结束
        11：核损预审核
        '''
        a = input('请输入你要进行的操作,多个操作时，请用英文逗号隔开：')
        try:
            list = a.split(',')
        except :
            print('请检查是否输入正确')

        push = do_task(claim_no)
        for i in list:
            if i == '1':
                response = push.push_task()
            elif i == '2':
                response = push.push_priceCheck()
            elif i == '3':
                response = push.push_audit('02')
            elif i == '4':
                response = push.push_audit('01')
            elif i == '5':
                response = push.push_douAudit('2')
            elif i == '6':
                response = push.push_douAudit('1')
            elif i == '7':
                response = push.back_push('02',input('请输入目前环节：'),'01')
            elif i == '8':
                response = push.back_push('01',input('请输入目前环节：'),'01')
            elif i == '9':
                response = push.task_done('1')
            elif i == '10':
                response = push.task_done('2')
            elif i == '11':
                response = push.pre_audit()

        print(response)
    # except Exception as e:
    #     curr_path=os.path.dirname(__file__)
    #     logger = logging.getLogger(__name__)
    #     logger.info(curr_path)
    #     print(e)
