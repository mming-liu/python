from typing import List
import cx_Oracle

class do_connect():
    def __init__(self,username,password) -> None:
        self.username = username
        self.password = password

    def get_data(self,sql):
        '''
        链接数据库，并执行sql
        '''
        conn = cx_Oracle.connect(self.username+"/"+self.password+"@192.168.200.25:1521/orcl")
        cursor = conn.cursor()
        # return 'Success'
        result = cursor.execute(sql)
        all_data=cursor.fetchall()
        return all_data

class do_data():
    def __init__(self) -> None:
        pass

    def do_data(self,datas):
        '''
        处理查出来的数据，从元组组成的list类型，改成由list组成的多维list
        '''
        data_list = []
        if len(datas) > 0 :
            for data in datas:
                if data != None:
                    data_list.append(str(data[0]))
            return data_list
        else:
            return None

    def longest_day(self,do_datas):
        '''
        只有一个诊断时取最高的诊断金额，或者是取诊断对应的最高天数
        '''
        max_data = 0
        if  do_datas != None:
            for data in do_datas:
                try:
                    max_data = max(int(float(data)),max_data)
                except Exception as e:
                    # print(e)
                    pass
        return  max_data   

    def most_money(self,do_datas):
        '''
        多个诊断时，取最高的金额和次高的金额
        '''
        max_data = []
        datas = 0
        if  do_datas != None:
            for data in do_datas:
                try:
                    datas = max(int(float(data)),datas)
                    # max_data.append(datas)
                except Exception as e:
                    print(e)
                    pass
            max_data.append(datas)
        return  max_data 


class get_sql():
    def __init__(self) -> None:
        pass
    
    def get_disease_id(self,casualty_id:str) -> str:
        '''
        根据casualty_id 查出来的诊断id列表
        '''
        sql = " select a.disease_id from T_DIAGNOSIS a where a.casualty_id = " + "'"+casualty_id+"'"
        return sql

    def get_longest_day(self,fee_type:int,data:list) -> str:
        '''
        fee_type == 1:伙食费上限
        fee_type == 2:护理费时长上限
        fee_type == 3:营养费时长上限
        fee_type == 4:误工费时长上限
        fee_type == 5:医疗费上限
        data : 根据casualty_id 查出来的disease_id列表
        '''
        if fee_type == 1:
            # 根据伤者的诊断，查询这些诊断对应的治疗时间区间，取这些时间中最大的作为该诊断对应的住院时长上限
            # 伙食费时长上限
            sql = "select n_period_max from  T_DISEASES_TREATMENT_PERIOD where c_del =0 and c_diss_id ="+ "'"+data+"'"
        elif fee_type == 2:
            # 根据伤者的诊断，查询这些诊断对应的三期时长，取这些三期时长中护理时长最大的作为该诊断对应的护理时长上限
            # 护理费时长上限
            sql = "select N_NURSING_MAX from T_DISEASES_THREE_PERIOD where c_del =0 and c_diss_id ="+ "'"+data+"'"
        elif fee_type == 3:
            # 根据伤者的诊断，查询这些诊断对应的三期时长，取这些三期时长中护理时长最大的作为该诊断对应的护理时长上限
            # 营养费时长上限
            sql = "select N_VEGETATIVE_MAX from T_DISEASES_THREE_PERIOD where c_del =0 and c_diss_id ="+ "'"+data+"'"
        elif fee_type == 4:
            # 根据伤者的诊断，查询这些诊断对应的三期时长，取这些三期时长中误工时长最大的作为该诊断对应的误工时长上限
            # 误工费时长上限
            sql = "select N_LOSS_WORKING_MAX from T_DISEASES_THREE_PERIOD where c_del =0 and c_diss_id ="+ "'"+data+"'"
        elif fee_type == 5:
            sql = 'select e.n_expenses_max from T_DISEASES_TREATMENT_EXPENSES e where e.c_diss_id =' + "'"+data+"'"
        return sql


if __name__ == '__main__':
    casualty_id = '11387F84BD1141B3ADF0622A32CFD9C8'
    sql = get_sql().get_disease_id(casualty_id)
    connect = do_connect('casualty_test','casualty_test')
    datas = connect.get_data(sql)
    do_datas = do_data().do_data(datas)
    # print(do_data)
    max_data = 0
    connect = do_connect('medical02','medical02')
    for data in do_datas:
        sql = get_sql().get_longest_day(4,data)
        
        datas = connect.get_data(sql)
        do_datas = do_data().do_data(datas)
        max_data = do_data().longest_day(do_datas)
    print(max_data)