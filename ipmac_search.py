import pymysql
import sys
from acc_crt import Mysql_crt
class SearchSQL(Mysql_crt):
    def __init__(self):
        super().__init__()
        host = "192.168.15.251"
        user = "root"
        pw = "zzq"
        db='ipdata'
        try:
            self.sql_c=pymysql.connect(host,user,pw,db)
            self.cur=self.sql_c.cursor()
            # print("连接成功。")
        except Exception as e:
            print("数据库连接失败")
            print(file=sys.stderr)
            print(e)
    def select_allinfo(self,t_name="ip_mac",l_name="id",limit_value=None):
        #执行特定条线的查询语句
        #t_name是表格名称，l_name是条件的名称是where后面跟着要限定的哪一行，；limit_value是限定值
         # all_ipinfo=self.select_data(table_name="ip_mac")
         sql_com="select * from {t_name} where {limit_name}=%s".format(t_name=t_name,limit_name=l_name)
         values=(limit_value)
         try:
            self.cur.execute(sql_com,values)
            key_ip =self.cur.fetchall()
            # print("条件查询成功")
            return key_ip
         except Exception as e:
             print("条件查询失败")
             print(e)
             print(file=sys.stderr)
         # return all_ipinfo
    def select_username(self,t_name="ip_mac",l_name="id",limit_value=None):
        sql_com = "select user_name from {t_name} where {limit_name}=%s".format(t_name=t_name, limit_name=l_name)
        values = (limit_value)
        try:
            self.cur.execute(sql_com, values)
            key_name = self.cur.fetchall()
            # print("条件查询成功")
            return key_name
        except Exception as e:
            print("条件查询失败")
            print(e)
            print(file=sys.stderr)
ms=SearchSQL()
n8_list=[]
n9_list=[]
for n in range(28):
    n =n+801
    p = n%10
    # print(p)
    if p==4:
        pass
    else:
        n8_list.append(n)
for n in range(28):
    n = n+901
    p = n%10
    if p ==4:
        pass
    else:
        n9_list.append(n)
print(n8_list)
print(n9_list)
print("*"*20+"8楼"+"*"*20)
for n_ls in n8_list:
    a=ms.select_allinfo(l_name="room",limit_value=n_ls)
    n=ms.select_username(l_name='room',limit_value=n_ls)
    # print(a)
    print("房间号%s\t登记个数%s"%(n_ls,len(a)))
    print(n)
print("*"*20+"9楼"+"*"*20)
for n_ls in n9_list:
    a=ms.select_allinfo(l_name="room",limit_value=n_ls)
    n = ms.select_username(l_name='room', limit_value=n_ls)
    # print(a)
    print("房间号%s\t登记个数%s" % (n_ls, len(a)))
    print(n)

ms.close_con()