import json
from sys import path
from jsonpath import jsonpath
from jsonpath_ng.jsonpath import JSONPath
import requests
from jsonpath_ng import parse
from bs4 import BeautifulSoup
import cx_Oracle

# def rule_info():
#     url = 'http://192.168.200.34:18014/rule-service/rule/api/auditClaimTreeDoc'
#     reponse = requests.get(url).text
#     all_paths = json.loads(reponse)
#     # json取值：https://www.cnblogs.com/x54256/p/7955204.html
#     fullpath = jsonpath(all_paths,expr= '$..fullJsonPath')
#     return fullpath

class check_date():
    def __init__(self,rule_no) -> None:
        self.rule_no = rule_no

    def rule_info(self):
        url = 'http://192.168.200.34:18014/rule-service/rule/api/ruleDoc/'+self.rule_no
        reponse = requests.get(url).text
        all_paths = json.loads(reponse)
        return all_paths

    def get_fullpath(self):
        all_paths = self.rule_info()
        fullpath = jsonpath(all_paths,expr= '$.fieldDocList[*].fullJsonPath')
        new_list = []
        for i in fullpath:
            if 'List' in i:
                i = i.replace('List','List[*]')
            new_list.append(i)
        return new_list
    
    def get_name (self):
        all_paths = self.rule_info()
        names = jsonpath(all_paths,expr='$.fieldDocList[*].fullName')
        return names

class get_message():
    def __init__(self,claim_no):
        self.claim_no = claim_no
    
    def get_message(self):
        conn = cx_Oracle.connect('apd_v50_test/apd_v50_test@192.168.200.25:1521/orcl')
        cursor = conn.cursor()
        if len(self.claim_no) < 36: 
            result = cursor.execute(" select data from t_rule_audit_report_clm_model a where a.claim_id in (select b.claim_id from t_claim b where b.claim_no = '"+self.claim_no+"') order by a.modify_date desc" )
        else:
            result = cursor.execute(" select data  from t_rule_audit_report_clm_model a where a.audit_report_id = '"+self.claim_no+"'")
        data=cursor.fetchone()
        try:
            data = json.loads(str(data[0]))
            return data
        except :
            return None
    
    def get_data(self,path):
        data = jsonpath.jsonpath(self.get_message(),expr=path)
        return data

class rule_date(check_date,get_message):
    def __init__(self, rule_no,claim_no) -> None:
        check_date.__init__(self,rule_no)
        get_message.__init__(self,claim_no)
    
    def rule_data(self):
        paths = check_date(self.rule_no).get_fullpath()
        names = check_date(self.rule_no).get_name()
        message = get_message(self.claim_no).get_message()
        datas = []

        for path in paths :
            data = jsonpath(message,expr= path)
            datas.append(data)

        return dict(zip(names,datas))

if __name__ == '__main__':
    '''
    claim_no的值为定损单号时,可以查该定损单最后一次报文的取值情况;
    claim_no的值为audit_report_id时,可以查该报文的取值情况
    '''
    a = rule_date('0104010003','acc_20210409_001')
    rule_values = a.rule_data()
    # print(len(rule_values))
    for i in rule_values:
        print(i+' : '+str(rule_values[i]))
