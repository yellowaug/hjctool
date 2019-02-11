import os
def ip_list(addr1,addr2):
    ip_cupe =[]
    for ip_1 in addr1:
        for ip_2 in range(addr2):
            ip_cupe.append("192.168.%s.%s"%(ip_1,str(ip_2+1)))
    return ip_cupe
def cmd_command(ip):
    cmd = "ping %s -n 5" % (ip)
    shell = os.popen(cmd)
    info = shell.read()
    shell.close()
    return info
if __name__ == "__main__":
    ip1_list = (11,12,13)
    ip2_num = 255
    addr_list = ip_list(ip1_list,ip2_num)
    for ip_addr in addr_list:
        res_info = cmd_command(ip_addr)
        print(res_info)
