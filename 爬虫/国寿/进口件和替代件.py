from typing import List
import cx_Oracle


class do_connect():
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password

    def get_data(self, sql):
        '''
        链接数据库，并执行sql
        '''
        conn = cx_Oracle.connect(self.username + "/" + self.password + "@192.168.200.25:1521/orcl")
        cursor = conn.cursor()
        # return 'Success'
        result = cursor.execute(sql)
        all_data = cursor.fetchall()
        return all_data


class sql():
    def __init__(self) -> None:
        pass

    def target_sql(self, str: str):
        sql = "select b.vehicle_sub_model_id,b.part_id,a.part_no,a.part_name\
                from t_md_part_cn006 a, t_md_part_cn006_rel b\
                where a.vehicle_series_id = b.vehicle_series_id\
                and a.part_id = b.part_id\
                and a.part_id in (select distinct c.replace_part_id\
                from t_md_part_cn006 c, t_md_part_cn006_rel d\
                where c.vehicle_series_id = d.vehicle_series_id\
                and c.part_id = d.part_id\
                and d.vehicle_sub_model_id = '{}'\
                and c.replace_part_no is not null)\
                and a.import_flag = '1'\
                and a.discontinued_flag = '0'\
                and b.vehicle_sub_model_id = '{}'".format(str, str)
        # print(sql)
        return sql

    def model_sql(self):
        sql = "select a.vehicle_sub_model_id from t_md_vehicle_model a where a.vehicle_sub_model_id like 'CN006%'"
        return sql


if __name__ == '__main__':
    connect = do_connect('china_life_meta', 'china_life_meta')
    model_sql = sql().model_sql()
    # print(model_sql)
    models = connect.get_data(model_sql)
    # print(models)
    for model in models:
        try:
            # print(type(model[0]))
            sql = sql().target_sql(model[0])
            # print(sql)
            parts = connect.get_data(sql)
        except:
            pass
