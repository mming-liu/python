import json
import cx_Oracle
import requests
from jsonpath import jsonpath


class check_date():
    def __init__(self, rule_no) -> None:
        self.rule_no = rule_no

    def rule_info(self):
        url = 'http://192.168.200.34:28014/rule-service/rule/api/ruleDoc/' + self.rule_no
        reponse = requests.get(url)
        all_paths = reponse.json()
        return all_paths

    def get_fullpath(self):
        all_paths = self.rule_info()
        fullpaths = jsonpath(all_paths, expr='$.fieldDocList[*].fullJsonPath')
        paths = []
        for i in fullpaths:
            if 'List' in i:
                i = i.replace('List', 'List[*]')
            paths.append(i)
        return paths

    def get_name(self):
        all_paths = self.rule_info()
        names = jsonpath(all_paths, expr='$.fieldDocList[*].fullName')
        return names


class get_message():
    def __init__(self, claim_no):
        self.claim_no = claim_no

    def get_message(self):
        conn = cx_Oracle.connect('china_life_test/china_life_test@192.168.200.25:1521/orcl')
        cursor = conn.cursor()
        if len(self.claim_no) < 36:
            result = cursor.execute(
                "select data from t_rule_audit_report_clm_model a where a.claim_id in (select b.claim_id from t_claim "
                "b where b.claim_no = '" + self.claim_no + "') order by a.modify_date desc")
        else:
            result = cursor.execute(
                " select data  from t_rule_audit_report_clm_model a where a.audit_report_id = '" + self.claim_no + "'")
        data = cursor.fetchone()
        try:
            data = json.loads(str(data[0]))
            return data
        except:
            return None

    def get_data(self, path):
        data = jsonpath.jsonpath(self.get_message(), expr=path)
        return data


class cl_object():
    def __init__(self, claim_no):
        self.claim_no = claim_no

    def get_message(self):
        url_login = "http://9.1.186.199:7001/web-suite/j_spring_security_check"
        data = {
            'j_username': 'picc_hesun',
            'j_password': 'aA123456',
            'captchaStr': 1
        }
        response = requests.post(url_login, data=data)
        # print(response.cookies.get_dict())
        cookies = response.cookies.get_dict()
        url_interface = 'http://9.1.186.199:7001/web-suite/interfacelog/findInterfaceLogs'
        data = {
            'take': '1',
            'skip': '0',
            'page': '1',
            'pageSize': '1',
            'dir': 'asc nulls first',
            'field': '',
            'interfaceCode': 'ClaimRule',
            'operatorAccountName': '',
            'businessNo': self.claim_no,
            'dateRange': 'THIS_MONTH'
        }
        responses = requests.post(url_interface, cookies=cookies, data=data)
        request = str(jsonpath(responses.json(), expr='$.data..requestParam'))
        request = request.replace("['", '').replace("']", '').replace('false', '"false"').replace('true', '"true"')
        # request = json.loads(request)
        request = eval(request)
        # print(request)
        return request


# class rule_date(check_date, get_message):
#     def __init__(self, rule_no, claim_no) -> None:
#         check_date.__init__(self, rule_no)
#         get_message.__init__(self, claim_no)
#
#     def rule_data(self):
#         check = check_date(self.rule_no)
#         data = check.rule_info()
#         paths = check.get_fullpath()
#         names = check.get_name()
#         message = get_message(self.claim_no).get_message()
#         datas = []
#
#         for path in paths:
#             data = jsonpath(message, expr=path)
#             datas.append(data)
#
#         return dict(zip(paths, datas))

class rule_date(check_date, cl_object):
    def __init__(self, rule_no, claim_no) -> None:
        check_date.__init__(self, rule_no)
        cl_object.__init__(self, claim_no)

    def rule_data(self):
        check = check_date(self.rule_no)
        data = check.rule_info()
        paths = check.get_fullpath()
        names = check.get_name()
        message = cl_object(self.claim_no).get_message()
        datas = []

        for path in paths:
            data = jsonpath(message, expr=path)
            datas.append(data)

        return dict(zip(paths, datas))


if __name__ == '__main__':
    '''
    claim_no的值为定损单号时,可以查该定损单最后一次报文的取值情况;
    claim_no的值为audit_report_id时,可以查该报文的取值情况
    '''
    # claim_no = '62021320000000030_95717','62021320000000020_95357','62021320000000031_95719'
    a = rule_date('0105010002', '80052021330000000147_2058066')
    rule_values = a.rule_data()
    for i in rule_values:
        print(i + ' : ' + str(rule_values[i]))