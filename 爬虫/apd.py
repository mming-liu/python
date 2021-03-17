import requests
import json
import cx_Oracle

def claim_push(data,claim_no,nodeType,nextNodeType):
    url = 'http://192.168.200.161:10007/web-suite/services/restful/claim/pushClaim'
    headers = {'Authorization':'gzqxW_sBQiaV0PlPKp5cG1QbduSclbAyx6QMtEXZcA07WLWk20bEx4vT'}

    # 替换值
    data['claimNo'] = claim_no
    data['accidentNo'] = claim_no
    data['nodeType'] = nodeType
    data['nextNodeType'] = nextNodeType
    
    response = requests.post(url,headers = headers,json = data)
    return response.json()

def get_loss(claim_no):
    conn = cx_Oracle.connect('apd_v50_test/apd_v50_test@192.168.200.25:1521/orcl')
    # 使用cursor()方法获取操作游标
    cursor = conn.cursor()
    #使用execute方法执行SQL语句
    result=cursor.execute(" select  request_param from t_interface_log  where business_no = "+ claim_no + " and interface_log = 'ClaimInfoSync' order by a.start_date desc" )

    #使用fetchone()方法获取一条数据
    data=cursor.fetchone()

    #获取所有数据
    # all_data=cursor.fetchall()

    #获取部分数据，8条
    #many_data=cursor.fetchmany(8)

def open_txt(filename):
    # 打开报文文件，读取报文内容，并转换为字典（dict）型数据
    path = 'C:/Users/ccc/Desktop/APD/5.0报文/' + filename
    # with os.open(path,'r',encoding='utf-8') as f:
    #     data = f.read()
    #     data = json.dumps(data)
    # return data
    f = open(path,'r',encoding='utf-8')
    # data = f.read()
    data = json.load(f)
    return data

if __name__ == '__main__':
    claim_no = 'acc_20210317_002'
    # data = open_txt('APD5.0报文.txt')
    # a = claim_push(data,claim_no,'01','01')
    loss = get_loss(claim_no)
    print(loss)