import wmi
def net_desc():
    '''
    读取网卡信息的模块
    '''
    # net_list=[]
    work = wmi.WMI()
    ip_config = work.Win32_NetworkAdapterConfiguration(IPEnabled=True)
    # n = len(ip_config)
    # for net_desc in range(n):
    #     network = ip_config[net_desc]
    #     # print("%s.%s"%(net_desc,network.Description))
    #     net_list.append(network.Description)
    # return ip_config,net_list
    network=ip_config[0]
    ip = network.IPAddress[0]
    mac = network.MACAddress
    # ip_gateway = network.DefaultIPGateway[0]
    # dns = network.DNSServerSearchOrder
    # subnet = network.IPSubnet
    # print("%s,\n%s,\n%s,\n%s,\n%s,"%(ip,mac,ip_gateway,dns,subnet))
    return ip,mac
def set_ip(ip_config):
    network = ip_config
    new_ip = [ip_config[0].IPAddress]
    subnet = ["255.255.255.0"]
    gateway = ["192.168.13.1"]
    dns = ["202.103.224.68","114.114.114.114"]
    re_value_ip = network.EnableStatic(IPAddress=new_ip,SubnetMask=subnet) #设置ip地址以及子网掩码
    re_value_gateway = network.SetGateways(DefaultIPGateway=gateway)#设置网关
    re_value_dns = network.SetDNSServerSearchOrder(DNSServerSearchOrder=dns)#设置dns
    if re_value_ip[0] == 0:
        print("IP设置成功")
    if re_value_gateway[0] == 0:
        print("网关设置成功")
    if re_value_dns[0] == 0:
        print("DNS设置成功")
if __name__ == "__main__":
    # ipconfig,net_list = net_desc()
    # ip_address = input("输入IP地址：\n")
    # set_ip(ipconfig[0])
    # print(net_list)
    net_desc()