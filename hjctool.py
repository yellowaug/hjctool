import wmi
import pymysql
import os
import re
def check_net():
    command = "ping 192.168.15.251 -n 2"
    match_command = "丢失 = 0"
    shell = os.popen(command)
    info = shell.read()
    shell.close()
    match_result = re.search(match_command,info,re.S)
    if match_result != None:
        code = 1
        print("局域网通信正常")
        return code
    else:
        code = 0
        print("局域网通信异常")
        return code
def check_sql():
    ip = get_ip()
    host = "192.168.15.251"
    user = "root"
    password = "zzq"
    data = "ipdata"
    db = pymysql.connect(host, user, password, data)
    cur = db.cursor()
    user_ip = str(ip[2])
    sql_com = "select ip_addr from ip_mac where mac_addr = %s"
    cur.execute(sql_com,user_ip)
    use_ip_info = cur.fetchall()
    res_len = len(use_ip_info)
    return res_len
def setip():
    info_list = []
    work =wmi.WMI()
    ip_config = work.Win32_NetworkAdapterConfiguration(IPEnabled=True)
    network=ip_config[0]
    ip_addr = network.IPAddress[0]
    ip_gateway = network.DefaultIPGateway[0]
    new_ip = [ip_addr]
    subnet = ["255.255.255.0"]
    gateway = [ip_gateway]
    dns = ["202.103.224.68", "114.114.114.114"]
    re_value_ip = network.EnableStatic(IPAddress=new_ip, SubnetMask=subnet)  # 设置ip地址以及子网掩码
    re_value_gateway = network.SetGateways(DefaultIPGateway=gateway)  # 设置网关
    re_value_dns = network.SetDNSServerSearchOrder(DNSServerSearchOrder=dns)  # 设置dns
    if re_value_ip[0] == 0:
        set_ip_info = "IP设置成功"
        info_list.append(set_ip_info)
    else:
        set_ip_info ="ip地址设置失败"
        info_list.append(set_ip_info)
    if re_value_gateway[0] == 0:
        set_gate_info = "网关设置成功"
        # info_list.append(set_gate_info)
    else:
        set_gate_info = "网关设置失败"
        # info_list.append(set_gate_info)
    if re_value_dns[0] == 0:
        set_dns_info = "DNS设置成功"
        # info_list.append(set_dns_info)
    else:
        set_dns_info ="DNS设置失败"
        # info_list.append(set_dns_info)
    return info_list
def instersql(ip_info,user_name,room,class_name):
    inste_info = []
    host = "192.168.15.251"
    user = "root"
    password = "zzq"
    data = "ipdata"
    db = pymysql.connect(host, user, password, data)
    cur = db.cursor()
    ip = str(ip_info[1])
    mac = str(ip_info[2])
    dns = str(ip_info[3])
    mac_name = str(ip_info[4])
    sql = """INSERT INTO ip_mac(ip_addr,dns,mac_name,mac_addr,user_name,room,class_name) VALUES
    (%s,%s,%s,%s,%s,%s,%s);"""
    values = (ip,dns,mac_name,mac,user_name,room,class_name)
    try:
        # 执行sql语句
        cur.execute(sql, values)
        # 提交到数据库执行
        db.commit()
        inste_info.append("IP信息写入数据库成功")
    except Exception as e:
        # 如果发生错误则回滚
        db.rollback()
        inste_info.append("IP信息无法写入数据")
        print(e)
    return inste_info
def get_ip():
    ip_info = []
    work =wmi.WMI()
    ip_config = work.Win32_NetworkAdapterConfiguration(IPEnabled=True)
    network=ip_config[0]
    net_card = network.Description
    ip = network.IPAddress[0]
    mac = network.MACAddress
    dns = network.DNSServerSearchOrder
    mac_name = network.DNSHostName
    ip_info.append(net_card)
    ip_info.append(ip)
    ip_info.append(mac)
    ip_info.append(dns)
    ip_info.append(mac_name)
    return ip_info
def reset():
    reset_info=[]
    ip = get_ip()
    host = "192.168.15.251"
    user = "root"
    password = "zzq"
    data = "ipdata"
    db = pymysql.connect(host, user, password, data)
    cur = db.cursor()
    user_ip = str(ip[2])
    sql_com = "select ip_addr from ip_mac where mac_addr = %s"
    cur.execute(sql_com,user_ip)
    use_ip_info = cur.fetchall()
    work =wmi.WMI()
    ip_config = work.Win32_NetworkAdapterConfiguration(IPEnabled=True)
    network=ip_config[0]
    ip_addr = use_ip_info[0]
    for use_ip in ip_addr:
        res_ip = use_ip
    new_ip = [res_ip]
    subnet = ["255.255.255.0"]
    gateway = ["192.168.13.1"]
    dns = ["202.103.224.68", "114.114.114.114"]
    re_value_ip = network.EnableStatic(IPAddress=new_ip, SubnetMask=subnet)  # 设置ip地址以及子网掩码
    re_value_gateway = network.SetGateways(DefaultIPGateway=gateway)  # 设置网关
    re_value_dns = network.SetDNSServerSearchOrder(DNSServerSearchOrder=dns)  # 设置dns
    if re_value_ip[0] == 0:
        reset_info.append("IP重置成功")
    else:
        reset_info.append("IP重置失败")
    if re_value_gateway[0] == 0:
        reset_info.append("网关重置成功")
    else:
        reset_info.append("网关重置失败")
    if re_value_dns[0] == 0:
        reset_info.append("DNS重置成功")
    else:
        reset_info.append("DNS重置失败")
    return reset_info
# if __name__ == "__main__":
    # setip()
    # ip = get_ip()
    # instersql(ip)
    # reset()
    # print(a)
    # print(ip)
    # check_net()
    # check_sql()