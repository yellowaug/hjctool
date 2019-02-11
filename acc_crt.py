import pymysql
import sys
class Mysql_crt(object): #虚拟机账号登记数据库的增删改查
    def __init__(self): #初始化连接数据库
        host = "192.168.15.251"
        user = "root"
        pw = "zzq"
        db = "accesslist"
        try:
            self.sql_c=pymysql.connect(host,user,pw,db)
            self.cur=self.sql_c.cursor()
            print("连接成功。")
        except Exception as e:
            print("数据库连接失败")
            print(file=sys.stderr)
            print(e)
    def close_con(self): #关闭数据库连接
        self.cur.close()
    def insert_table(self,v_device=None,v_ip=None,v_acc=None,v_pass=None,v_note=None): #登记
        sql_com="insert into account_list(device,ip_addr,accuont,password,note) VALUES (%s,%s,%s,%s,%s)"
        values=(v_device,v_ip,v_acc,v_pass,v_note)
        try:
            self.cur.execute(sql_com,values)
            self.sql_c.commit()
            print("数据插入成功")
        except Exception as e:
            print("数据插入失败")
            print(e)
            print(file=sys.stderr)
    def updata_table(self,cou_name=None,new_values=None,cou_limit=None,limit_key=None):
        #定义修改数据的功能，以及变量
        #SQL语句用的参数用.format拼接，SQL语句的值用%s拼接，这样才不会报错
        #功能已经完成
        sql_com1 = "update account_list set {coume_name}=%s where {coume_limit}=%s" \
            .format(coume_name=cou_name, coume_limit=cou_limit)
        var = (new_values, limit_key)
        try:
            self.cur.execute(sql_com1,var)
            self.sql_c.commit()
            print("数据更新成功")
        except Exception as e:
            print("数据更新失败")
            self.sql_c.rollback()
            print(e)
            print(file=sys.stderr)
    def dele_data(self,limit_values=None):
        sql_com = "DELETE FROM account_list WHERE id=%s "
        print(sql_com)
        values = (limit_values)
        try:
            self.cur.execute(sql_com,values)
            self.sql_c.commit()
            print("数据删除成功")
        except Exception as e:
            print("数据删除失败")
            self.sql_c.rollback()
            print(e)
            print(file=sys.stderr)
    def select_data(self,table_name="account_list"):
        sql_com = "select * from %s" % table_name
        try:
            self.cur.execute(sql_com)
            info =self.cur.fetchall()
            print("数据查询成功")
            return info
        except Exception as e:
            print("数据查询失败")
            print(e)
            print(file=sys.stderr)


# ms=Mysql_crt()
# res =ms.select_data()
# ms.updata_table(cou_name="ip_addr",new_values="teteteet",cou_limit="id",limit_key="20")
# ms.close_con()
# print(res)