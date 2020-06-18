# -*-coding:UTF-8 -*-
import sqlite3
from LogMan import LogManager as logmanager
import settings as Settings

class DataManager():
    def __init__(self):
        dbpath= Settings.DATABASE
        self._conn = sqlite3.connect(dbpath,check_same_thread=False)
        self._cursor = self._conn.cursor()
        self.logmanager = logmanager("auto")

    def __new__(cls,*args,**kwargs):
        if not hasattr(cls,"_instance"):
            cls._instance = super().__new__(cls,*args,**kwargs)
        return cls._instance

    def exec_by_sql(self,sql):
        self._cc.execute(sql)
        self._conn.commit()
        return True

    def close_conn(self):
        self._conn.close()

    def query_users(self):
        table=self._cc.execute("select * from Users")
        self._conn.commit()
        return table

    def update_user(self,name,workid,role,project,telephone):
        try:
            table=self._cc.execute("update Users set workid='{1}', role='{2}',project='{3}',telephone='{4}'  \
            where name='{5}'".format(workid,role,project,telephone,name))
            self._conn.commit()
            return True
        except Exception as e:
            print(e)
            return e

    def add_user(self,name,workid,role,project,telephone):
        pass

    def delete_user(self,name):
        pass

    def save_api_case(self,apiresult):
        if ("re" in apiresult) and ("response" in apiresult["re"]):
            _caseid=apiresult["case"][1]
            _version = apiresult["case"][2]
            _apilink = apiresult["case"][6]
            _request_data = apiresult["case"][10]
            _response = apiresult["re"]["response"]
            _result = apiresult["re"]["test_result"]
            _spend = apiresult["spend"]
            _start_time = apiresult["start-time"]
            _end_time = apiresult["end-time"]
            try:
                table = self._cc.execute("insert into api_case_result (caseid,version,api_link,request_data,response,result,spend,start_time,end_time) \
	            values('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}')".format(_caseid,_version,_apilink,_request_data,_response,_result,_spend,_start_time,_end_time))
                self._conn.commit()
                return True
            except Exception as e:
                print("sql error----------------------")
                print(e)
                return e
        elif  ("re" in apiresult) and ("error" in apiresult["re"]):
            _caseid = apiresult["case"][1]
            _version = apiresult["case"][2]
            _apilink = apiresult["case"][6]
            _request_data = apiresult["case"][10]
            _response = apiresult["re"]["error"]
            _result = "error"
            _spend = apiresult["spend"]
            _start_time = apiresult["start-time"]
            _end_time = apiresult["end-time"]
            try:
                table = self._cc.execute("insert into api_case_result (caseid,version,api_link,request_data,response,result,spend,start_time,end_time) \
                	            values('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}')".format(
                _caseid, _version, _apilink, _request_data, _response, _result, _spend, _start_time, _end_time))
                self._conn.commit()
                return True
            except Exception as e:
                print("sql error----------------------")
                print(e)
                return e
        elif  ("error" in apiresult):
            _caseid = apiresult["case"][1]
            _version = apiresult["case"][2]
            _apilink = apiresult["case"][6]
            _request_data = apiresult["case"][10]
            _response = apiresult["error"]
            _result = "error"
            try:
                table = self._cc.execute("insert into api_case_result (caseid,version,api_link,request_data,response,result) \
                	            values({0},{1},{2},{3},{4},{5})".format(_caseid, _version, _apilink, _request_data, _response, _result))
                self._conn.commit()
                return True
            except Exception as e:
                print("sql error----------------------")
                print(e)
                return e


    def save_robot_suite_result(self,result):
        #suite文件结束后listener存储结果到DB
        try:
            table = self._cursor.execute("insert into ui_task_case_table(taskid,caseid,caseresult,starttime,endtime,elapsedtime) \
                                     values('{0}','{1}','{2}','{3}','{4}','{5}')".format(result["taskid"],result["caseid"],result["status"],result["starttime"],result["endtime"],result["elapsedtime"]))
            self._conn.commit()
        except Exception as e:
            self.logmanager.error(e)
            print("sql error:",e)

if __name__ == '__main__':
    dd=DataManager()
    # re=dd.query_Users()
    # for i in re:
    #     print(i)
    result = {"taskid": "111", "caseid": "eee", "status": "pass", "starttime": "12454e6757", "endtime": "676776767887",
              "elapsedtime": "122344"}
    ss= "insert into ui_task_case_table(taskid,caseid,caseresult,starttime,endtime,elapsedtime) \
                                     values('{0}','{1}','{2}','{3}','{4}','{5}')".format(result["taskid"],result["caseid"],result["status"],result["starttime"],result["endtime"],result["elapsedtime"])
    print(ss)
    
    dd.save_robot_suite_result(result)