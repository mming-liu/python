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

class sql():
    def __init__(self) -> None:
        pass

    def sql(self,str:str):
        sql = "select b.vehicle_sub_model_id,a.part_no from t_md_part_cn" +str+ " a, t_md_part_cn"+str+"_rel b where a.part_id = b.part_id and b.part_model_type  != '1'"
        # print(sql)
        return sql

if __name__ == '__main__':
    connect = do_connect('china_life_meta','china_life_meta')
    for i in range(1,628):
        try:
            i = '%03d'%i
            sql = sql().sql(str(i))
            data = connect.get_data(sql)
            print(data)
        except :
            pass