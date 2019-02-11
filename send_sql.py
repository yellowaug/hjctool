import pymysql
from hjctool import get_ip
host = "192.168.13.230"
user = "hjc"
password = "zzq"
data = "ipdata"
ip_info = get_ip()
db = pymysql.connect(host,user,password,data)
cur = db.cursor()
ip = str(ip_info[1])
mac = str(ip_info[2])
dns = str(ip_info[3])
sql = """INSERT INTO ip_mac(ip_addr, dns,mac_addr) VALUES
(%s,%s,%s);"""
values = (ip,mac,dns)
try:
    # 执行sql语句
    cur.execute(sql,values)
    # 提交到数据库执行
    db.commit()
    print("IP信息写入数据库成功")
except Exception as e:
    # 如果发生错误则回滚
    db.rollback()
    print("IP信息无法写入数据")
# cur.execute("select * from ip_mac")
#
# results = cur.fetchall()
# print(results)
