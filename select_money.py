import sys
import pymysql
from acc_crt import Mysql_crt
class SelectAllSql(Mysql_crt):
    def __init__(self):
        host = "192.168.15.251"
        user = "root"
        pw = "zzq"
        self.db = "oa_hj"
        try:
            self.sql_c=pymysql.connect(host,user,pw,self.db)
            self.cur=self.sql_c.cursor()
            print("连接成功。")
        except Exception as e:
            print("数据库连接失败")
            print(file=sys.stderr)
            print(e)
    def txt_open(self): #txt文件的逐行读取，并返回列表
        temp_list=[]
        tempsql=r'e:\tempsql.txt'
        file=open(tempsql,'r',encoding='utf-8')
        bs=file.readlines()
        for b in bs:
            value=b.strip()
            temp_list.append(value)
        file.close()
        return temp_list
    def text_write(self,info):#txt文件的逐写入
        file_sql=r'e:\sqldata.txt'
        file=open(file_sql,'a+',encoding='utf-8')
        file.writelines(info)
a=SelectAllSql()
cs = a.txt_open()
for c in cs:
    aa=a.select_data(c)
    print('表名称:%s'%c)
    print(aa)
    try:
        a.text_write(str(c))
        a.text_write(str(aa))
        print('写入文件成功')
    except Exception as e:
        print(e)
        print(sys.stderr)